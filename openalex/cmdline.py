"""
This module creates a RIS and BibTex command line interface.
"""

#!/usr/bin/env python3

import click
from .works import Works


@click.command()
@click.argument("doi")
@click.option(
    "--citeformat",
    default="bibtex",
    type=click.Choice(["bibtex", "ris"]),
    help="Output format (default: bibtex)",
)
def cite(doi, citeformat):
    """
    Outputs RIS or BibTeX for a given DOI. ChatGPT 4 assisted
    me in writing this function.
    """
    w_0 = Works(doi)
    if citeformat == "bibtex":
        print(w_0.bibtex())
    elif citeformat == "ris":
        print(w_0.ris())
