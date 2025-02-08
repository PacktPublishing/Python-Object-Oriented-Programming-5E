"""
Python 3 Object-Oriented Programming Case Study

Chapter 7, Python Type Hints.
"""
from collections.abc import Iterator
import json
from pathlib import Path
from typing import Annotated, Any
from pydantic import TypeAdapter

from pydantic import field_validator, Field
from pydantic.dataclasses import dataclass


@dataclass
class Result:
    success: bool
    exit_code: int
    duration: float

    @field_validator('exit_code')
    @classmethod
    def must_be_non_negative(cls, v: int) -> int:
        if v < 0:
            raise ValueError('must be non-negative')
        return v


test_result = """
>>> r1 = Result(success=True, exit_code=0, duration=1.23)
>>> r2 = Result(success=False, exit_code=-2, duration=2.34)
Traceback (most recent call last):
...
pydantic_core._pydantic_core.ValidationError: 1 validation error for Result
exit_code
  Value error, must be non-negative [type=value_error, input_value=-2, input_type=int]
    For further information visit https://errors.pydantic.dev/2.10/v/value_error

"""


from typing import Annotated
from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class Result2:
    success: bool
    exit_code: Annotated[int, Field(ge=0)]
    duration: float


test_result_2 = """
>>> r1 = Result2(success=True, exit_code=0, duration=1.23)
>>> r2 = Result2(success=False, exit_code=-2, duration=2.34)
Traceback (most recent call last):
...
pydantic_core._pydantic_core.ValidationError: 1 validation error for Result2
exit_code
  Input should be greater than or equal to 0 [type=greater_than_equal, input_value=-2, input_type=int]
    For further information visit https://errors.pydantic.dev/2.10/v/greater_than_equal

"""


@dataclass
class Test:
    command: list[str]
    output: str
    err: str
    retcode: int | None
    elapsed: float
    show_on_standard: bool
    run_id: str
    start: float
    end: float


@dataclass
class Environment:
    result: Result2 | None
    test: list[Test] = Field(default_factory=list)

    def summary(self) -> str:
        if self.result and self.result.success:
            return "success"
        elif self.result and not self.result.success:
            return "failure"
        else:
            return "not run"


def env_detail(json: dict[str, Any]) -> Iterator[tuple[str, Environment]]:
    testenvs = json['testenvs']
    for env_name, details in testenvs.items():
        if env_name.startswith("."):
            continue
        if details:
            result = TypeAdapter(Result2).validate_python(details['result'])
            test = [
                TypeAdapter(Test).validate_python(t)
                for t in details['test']
            ]
            env = Environment(result=result, test=test)
        else:
            env = Environment(result=None)
        yield env_name, env


def main() -> None:
    result_dir = Path.cwd().parent / "ch_01" / "data"
    for file in result_dir.glob("*.json"):
        # 1. Load file
        print(file.name)
        result = json.loads(file.read_text())
        for env_name, env in env_detail(result):
            print(env_name, env.summary())

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}

if __name__ == "__main__":
    main()

