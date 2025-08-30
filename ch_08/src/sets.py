"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures

Expects HASHSEED=42
"""

test_set_1 = """
>>> song_library = [
...     ("Phantom Of The Opera", "Sarah Brightman"),
...     ("Knocking On Heaven's Door", "Guns N' Roses"),
...     ("Captain Nemo", "Sarah Brightman"),
...     ("Patterns In The Ivy", "Opeth"),
...     ("November Rain", "Guns N' Roses"),
...     ("Beautiful", "Sarah Brightman"),
...     ("Mal's Song", "Vixy and Tony"),
... ]
>>> artists = set()
>>> for song, artist in song_library:
...     artists.add(artist)

>>> artists
{'Opeth', "Guns N' Roses", 'Vixy and Tony', 'Sarah Brightman'}

>>> "Opeth" in artists
True
>>> alphabetical = list(artists)
>>> alphabetical.sort()
>>> alphabetical
["Guns N' Roses", 'Opeth', 'Sarah Brightman', 'Vixy and Tony']

>>> for artist in artists:
...     print(f"{artist} plays good music")
...
Opeth plays good music
Guns N' Roses plays good music
Vixy and Tony plays good music
Sarah Brightman plays good music

>>> dusty_artists = {
...     "Sarah Brightman",
...     "Guns N' Roses",
...     "Opeth",
...     "Vixy and Tony",
... }
>>> steve_artists = {"Yes", "Guns N' Roses", "Genesis"}

>>> all = dusty_artists | steve_artists
>>> all
{'Genesis', 'Vixy and Tony', 'Sarah Brightman', 'Opeth', "Guns N' Roses", 'Yes'}

>>> both = dusty_artists.intersection(steve_artists)
>>> both
{"Guns N' Roses"}

>>> not_both = dusty_artists ^ steve_artists
>>> not_both 
{'Genesis', 'Sarah Brightman', 'Opeth', 'Vixy and Tony', 'Yes'}

"""

test_set_extra = """
>>> song_library = [
...     ("Phantom Of The Opera", "Sarah Brightman"),
...     ("Knocking On Heaven's Door", "Guns N' Roses"),
...     ("Captain Nemo", "Sarah Brightman"),
...     ("Patterns In The Ivy", "Opeth"),
...     ("November Rain", "Guns N' Roses"),
...     ("Beautiful", "Sarah Brightman"),
...     ("Mal's Song", "Vixy and Tony"),
... ]
>>> artists = set(artist for _, artist in song_library)
>>> artists == {'Opeth', "Guns N' Roses", 'Vixy and Tony', 'Sarah Brightman'}
True
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
