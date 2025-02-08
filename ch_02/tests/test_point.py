from pathlib import Path
import runpy


def test_point_0(capsys):
    script = Path.cwd() / "src" / "point_0.py"
    expected = """\
5 4
3 6
"""

    runpy.run_path(script)
    out, err = capsys.readouterr()
    assert out == expected

def test_point_1(capsys):
    script = Path.cwd() / "src" / "point_1.py"
    expected = """\
0 0
"""

    runpy.run_path(script)
    out, err = capsys.readouterr()
    assert out == expected
