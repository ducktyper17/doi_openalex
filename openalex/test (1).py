"""
Tests to ensure both RIS and BibTex versions
of CitationShark are working properly.
"""
import re
from .works import Works


def test_bibtex():
    """
    Test to see if bibtex returns a bibtex file. ChatGPT 4 assisted
    me in writing this function.
    """
    w_0 = Works("https://doi.org/10.1021/jp047349j")
    bibtex_entry = w_0.bibtex()
    # Define a simple pattern to check if the
    # returned string is a BibTeX entry
    bibtex_pattern = re.compile(r"@\w+\{[^}]+\,[\s\S]*\}", re.MULTILINE)

    # Check if the returned string matches the pattern
    assert (
        bibtex_pattern.match(bibtex_entry) is not None
    ), "The returned string is not a valid BibTeX entry"


def test_ris():
    """
    Test to see if bibtex returns a bibtex file. ChatGPT 4 assisted
    me in writing this function.
    """
    # Call the function you want to test
    w_0 = Works("https://doi.org/10.1021/jp047349j")
    ris_citation = w_0.ris()

    # Define a simple pattern to check if the
    # returned string is an RIS citation
    ris_pattern = re.compile(
        r"^TY\s+-\s+\w+(\n[A-Z0-9]{2}\s+-\s+[\s\S]+?)*\nER\s+-", re.MULTILINE
    )

    # Check if the returned string matches the pattern
    assert (
        ris_pattern.match(ris_citation) is not None
    ), "The returned string is not a valid RIS citation"