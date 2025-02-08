"""
Python 3 Object-Oriented Programming, 5th ed.

Chapter 1, Object-Oriented Design
"""
import json

import pytest

import pydantic_example

@pytest.fixture
def mock_json_1(tmp_path, monkeypatch):
    (tmp_path / "ch_01" / "data").mkdir(parents=True)
    (tmp_path / "ch_07").mkdir(parents=True)
    path = tmp_path / "ch_01" / "data" / "case_1.json"
    doc = {
        "testenvs": {
            ".skip": {},
            "3.12": {
                "result": {"success": True, "exit_code": 0, "duration": 1.23},
                "test": [
                    {
                        "retcode": 0,
                        "command": ["/path/to/command", "arg"],
                        "output": "",
                        "err": "",
                        "elapsed": 1.23,
                        "show_on_standard": True,
                        "run_id": "SomeId",
                        "start": 2.34,
                        "end": 4.56,
                    },
                ]
            }
        }
    }
    with path.open('w') as sample_file:
        json.dump(doc, sample_file)
    monkeypatch.chdir(tmp_path / "ch_07")

def test_one_feature(mock_json_1, capsys):
    pydantic_example.main()
    out, err = capsys.readouterr()
    assert err == ""
    assert out == "case_1.json\n3.12 success\n"

