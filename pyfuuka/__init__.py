#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# the LICENSE file for more details.

import basc_py4chan

"""FoolFuuka Python Library.

pyFuuka is a Python library that gives access to the FoolFuuka API
and an object-oriented way to browse and get board and thread
information quickly and easily.
"""

__version__ = '0.1.0'

from .board import Board, board, get_boards, get_all_boards
from .thread import Thread
from .post import Post
from .file import File
from .url import Url
