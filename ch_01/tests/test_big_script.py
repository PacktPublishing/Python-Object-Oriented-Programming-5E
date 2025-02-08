"""
Python 3 Object-Oriented Programming, 5th ed.

Chapter 1, Object-Oriented Design
"""
import json

import pytest

import big_script

@pytest.fixture
def mock_json_1(tmp_path, monkeypatch):
    (tmp_path / "data").mkdir()
    path = tmp_path / "data" / "case_1.json"
    doc = {
        "testenvs": {
            ".skip": {},
            "3.12": {
                "result": {"success": True},
                "test": [
                    {"retocde": 0},
                    {"command": ["/path/to/command", "arg"]}
                ]
            }
        }
    }
    with path.open('w') as sample_file:
        json.dump(doc, sample_file)
    monkeypatch.chdir(tmp_path)

def test_one_feature(mock_json_1, capsys):
    big_script.main()
    out, err = capsys.readouterr()
    assert err == ""
    assert out == "case_1               ok\n"

