"""
This module command line interface.
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
    wrk = Works(doi)
    if citeformat == "bibtex":
        print(wrk.bibtex())
    elif citeformat == "ris":
        print(wrk.ris())
