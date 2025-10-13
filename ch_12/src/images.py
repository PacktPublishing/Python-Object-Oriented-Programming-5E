"""
Python 3 Object-Oriented Programming

Chapter 12. Advanced Python Design Patterns

Default setup is this:

1.  Download Java Runtime (JRE) for your platform.
    https://www.java.com/en/download/manual.jsp

2.  Download the latest ``plantuml-1.yyyy.m.jar``.
    https://plantuml.com/download
    It can be left in the project's top-level directory.
    Or, it can be stuffed down into a virtual environment.

3.  Update this script with the path to the JAR file.

"""
import re
from pathlib import Path
from typing import Iterator


class FindUML:
    def __init__(self, base: Path) -> None:
        self.base = base
        self.start_pattern = re.compile(r"@startuml *(.*)")

    def uml_file_iter(self) -> Iterator[tuple[Path, Path]]:
        for source in self.base.glob("**/*.uml"):
            if any(n.startswith(".") for n in source.parts):
                continue
            body = source.read_text()
            for output_name in self.start_pattern.findall(body):
                if output_name:
                    target = source.parent / output_name
                else:
                    target = source.with_suffix(".png")
                yield (source.relative_to(self.base), target.relative_to(self.base))


from pathlib import Path
import subprocess


class PlantUML:
    local_dir = Path.cwd()

    def __init__(
        self,
        plantjar: str | Path = "plantuml-1.2024.7.jar",
        venv_name: str = ".venv"
    ) -> None:
        def find_first(name: str | Path) -> Path:
            places = [
                self.local_dir,
                self.local_dir / venv_name,
            ]
            places += Path.cwd().parents
            for place in places:
                if (path := place / name).exists():
                    return path
            raise FileNotFoundError(f"could not find {plantjar}")

        match plantjar:
            case Path() as path if path.is_absolute():
                self.plantjar = path
            case Path() as path if not path.is_absolute():
                self.plantjar = find_first(path)
            case str() as name:
                self.plantjar = find_first(name)

    def process(self, source: Path) -> None:
        env: dict[str, str] = {
            # Rarely needed...
            # "GRAPHVIZ_DOT": str(Path("/")/"to"/"graphviz"/"dot"),
        }
        command = ["java", "-jar", str(self.plantjar), "-progress", str(source)]
        subprocess.run(command, env=env, check=True)




class GenerateImages:
    def __init__(self, base: Path, verbose: int = 0) -> None:
        self.finder = FindUML(base)
        self.painter = PlantUML()
        self.verbose = verbose

    def make_all_images(self) -> None:
        for source, target in self.finder.uml_file_iter():
            if not target.exists() or source.stat().st_mtime > target.stat().st_mtime:
                print(f"Processing {source} -> {target}")
                self.painter.process(source)
            else:
                if self.verbose > 0:
                    print(f"Skipping {source} -> {target}")


def main() -> None:
    g = GenerateImages(Path.cwd())
    g.make_all_images()


if __name__ == "__main__":
    main()
