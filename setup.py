#!/usr/bin/env python3

from distutils.core import setup
from curseradio import __version__

setup(name="curseradio",
      version=__version__,
      description="Curses interface for browsing and playing internet radio",
      author="Gordon Ball",
      author_email="gordon@chronitis.net",
      url="https://github.com/chronitis/curseradio",
      packages=["curseradio"],
      license="MIT",
      requires=["lxml", "requests"],
      scripts=["scripts/curseradio"])
