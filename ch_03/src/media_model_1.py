"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 3, When Objects Are Alike
"""

from pathlib import Path
import abc


class AudioFile(abc.ABC):
    ext: str

    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError(f"invalid file format {filepath.suffix!r}")
        self.filepath = filepath

    @abc.abstractmethod
    def play(self) -> None:
        ...


class MP3File(AudioFile):
    ext = ".mp3"

    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")


class WavFile(AudioFile):
    ext = ".wav"

    def play(self) -> None:
        print(f"playing {self.filepath} as wav")


class OggFile(AudioFile):
    ext = ".ogg"

    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")


class FlacFile:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == ".flac":
            raise ValueError("Not a .flac file")
        self.filepath = filepath

    def play(self) -> None:
        print(f"playing {self.filepath} as flac")


test_audio_2 = """
>>> p_1 = MP3File(Path("Heart of the Sunrise.mp3"))
>>> p_1.play()
playing Heart of the Sunrise.mp3 as mp3
>>> p_2 = WavFile(Path("Roundabout.wav"))
>>> p_2.play()
playing Roundabout.wav as wav
>>> p_3 = OggFile(Path("Heart of the Sunrise.ogg"))
>>> p_3.play()
playing Heart of the Sunrise.ogg as ogg
>>> error = MP3File(Path("The Fish.mov"))
Traceback (most recent call last):
...
ValueError: invalid file format '.mov'
"""

test_flac = """
>>> f_1 = FlacFile(Path("Long Distance Runaround.flac"))
>>> f_1.play()
playing Long Distance Runaround.flac as flac
>>> error = FlacFile(Path("The Fish.mov"))
Traceback (most recent call last):
...
ValueError: Not a .flac file

"""

type Playable = AudioFile | FlacFile

class Entertainment:
    def __init__(self, play_list: list[Playable]) -> None:
        self.queue = play_list

    def play(self) -> None:
        for song in self.queue:
            song.play


def fragile() -> None:
    s1 = WavFile(Path("Roundabout.wav"))
    s2 = MP3File(Path("Cans and Brahms.mp3"))
    s3 = OggFile(Path("We Have Heaven.ogg"))
    s4 = FlacFile(Path("South Side of the Sky.flac"))
    side_1 = Entertainment([s1, s2, s3, s4])
    side_1.play()


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
