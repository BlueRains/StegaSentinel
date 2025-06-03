"""Gives the needed context for the tests.

This means that tests can import the source code easily.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
