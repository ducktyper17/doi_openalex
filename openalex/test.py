"""
Tests to ensure both RIS and BibTex version.
"""
import re
from .works import Works

ref_bibtex = """author = {John R. Kitchin},
 journal = {ACS Catalysis},
 title = {Examples of Effective Data Sharing in Scientific Publishing},
 volume = {5},
 issue = {6},  
 pages = {3894-3899},
 year = {2015}"""

title = 'Examples of Effective Data Sharing in Scientific Publishing'
volume = 5
issue = 6

def test_bibtex():
 w = Works("https://doi.org/10.1021/acscatal.5b00538")
 assert title == w.new()

   

