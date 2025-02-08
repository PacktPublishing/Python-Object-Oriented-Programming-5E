# Python-Object-Oriented-Programming 5th-edition

Code Repository for Python Object-Oriented Programming - 5th edition, Published by Packt

## Testing the code base

This was tested using **uv**.

See https://docs.astral.sh/uv/ for how to install **uv**.

Each chapter is a separate mini-project.
Most a scripts, a few are libraries.

Generally, it's possible to use terminal commands like the following to confirm the chapter's code works:

```bash
cd ch_1
uvx tox run
```

This will install a copy of ``tox`` and run it to confirm the various virtual environments work.

## The project structure

Each chapter's code is in a separate directory, `ch_01`, `ch_02`, etc.

Within the chapter, there's some combination of `src`, and `tests` folders.
There will also be a `pyproject.toml` file with parameters used to control tools
like **tox**.


## Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781801077262">https://packt.link/free-ebook/9781801077262 </a> </p>
