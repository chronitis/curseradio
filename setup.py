#!/usr/bin/env python3

from setuptools import setup
import os

__version__ = None

with open(os.path.join(os.path.dirname(__file__), "curseradio", "__init__.py")) as f:
    for line in f.readlines():
        if line.startswith("__version__"):
            exec(line)

setup(name="curseradio",
      version=__version__,
      description="Curses interface for browsing and playing internet radio",
      author="Gordon Ball",
      author_email="gordon@chronitis.net",
      url="https://github.com/chronitis/curseradio",
      packages=["curseradio"],
      license="MIT",
      requires=["lxml", "requests", "pyxdg"],
      scripts=["scripts/curseradio"])
