"""
Tests to ensure pacakge is working.
"""
import re
from .works import Works


title = "Examples of Effective Data Sharing in Scientific Publishing"

def test_bibtex():
    """
    Tests to check working function in package.
    """
    won = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert title == won.new()
