"""
Python 3 Object-Oriented Programming, 5th ed.

Chapter 1, Object-Oriented Design
"""
import json
from pathlib import Path
import shlex

def main():

    optional = {"type"}

    result_dir = Path.cwd() / "data"
    for file in result_dir.glob("*.json"):
        # 1. Load file
        result = json.loads(file.read_text())
        # 2. Set Outcome
        app_name = file.stem
        env_outcome = None
        # 3. Examine environments
        for env_name, env in result['testenvs'].items():
            # 2a. Skip special names
            if env_name.startswith("."):
                continue
            # 2b. Accumulate outcomes
            if env:
                if env['result']['success']:
                    if env_outcome is None:
                        env_outcome = "ok"
                else:
                    for step in env['test']:
                        if step['retcode'] != 0:
                            command = Path(step['command'][0]).stem
                            args = shlex.join(step['command'][1:])
                            message = f"{env_name} failed {command} {args}"
                            if env_outcome is None or env_outcome == "ok":
                                env_outcome = message
                            else:
                                env_outcome = f"{env_outcome}, {message}"
            else:
                if env_outcome is None:
                    env_outcome = f"{env_name} did not run"
                elif env_outcome == "ok" and env_name in optional:
                    env_outcome = f"ok (except {env_name})"
                else:
                    env_outcome = f"{env_outcome}, {env_name} did not run"
        # 4. Write summary
        print(f"{app_name:20s} {env_outcome}")

if __name__ == "__main__":
    main()
