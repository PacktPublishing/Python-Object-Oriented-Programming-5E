"""
Python 3 Object-Oriented Programming

Chapter 8. The Intersection of Object-Oriented and Functional Programming
"""
import contextlib
from typing import TextIO, Any
from pathlib import Path


def doctest_everything(
    output: TextIO,
    *directories: Path,
    verbose: bool = False,
    **stems: str,
) -> None:
    if verbose:
        log = print
    else:
        def log(*args: Any, **kwars: Any) -> None:
            pass

    with contextlib.redirect_stdout(output):
        for directory in directories:
            log(f"Searching {directory}")
            for dirpath, dirnames, filenames in directory.walk():
                remove_excluded(dirnames)

                for name in filenames:
                    if not name.endswith('.py'):
                        continue
                    path = (dirpath / name).relative_to(Path.cwd())
                    log(
                        f"File {path}, "
                        f"{path.stem=}"
                    )
                    options = stems.get(path.stem, "")
                    if options.upper() == "SKIP":
                        log("Skipped")
                        continue
                    doctest_opts = (options.upper().split(",") if options else [])
                    r = run_test(path, doctest_opts )
                    if r.returncode:
                        log(r.stderr)


def remove_excluded(dirnames: list[str]) -> None:
    if ".tox" in dirnames:
        dirnames.remove(".tox")
    if ".venv" in dirnames:
        dirnames.remove(".venv")
    egg_info = [d for d in dirnames if d.endswith('.egg-info')]
    for e in egg_info:
        dirnames.remove(e)


import subprocess
import sys


def run_test(path: Path, options: list[str]) -> subprocess.CompletedProcess[str]:
    working_directory = path.parent
    source_path = working_directory.parent / "src"
    option_args = (
        ["-o", ",".join(options)] if options else []
    )
    result = subprocess.run(
        [sys.executable, "-m", "doctest", "-v"]
        + option_args
        + [str(path)],
        cwd=working_directory,
        env={"PYTHONPATH": str(source_path)},
        check=True,
        text=True,
    )
    return result


if __name__ == "__main__":
    # Example 1
    doctest_everything(
        sys.stdout,
        Path.cwd() / "ch_02",
        Path.cwd() / "ch_03",
        # exceptions...
        first_class="ELLIPSIS",
        test_ecommerce="SKIP",
        vendors="SKIP",
        __init__="SKIP",
        products="SKIP",
        main="SKIP",
        square="SKIP",
        stripe="SKIP",
    )

    # Example 2
    print()
    print("---REDIRECT---")
    doctest_log = Path("doctest.log")
    with doctest_log.open("w") as log:
        doctest_everything(
            log,
            Path.cwd() / "ch_04",
            Path.cwd() / "ch_05",
            verbose=True,
            colors="SKIP",
        )
    print(doctest_log.read_text())
