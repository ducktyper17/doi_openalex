"""
This file enables a user to pass in a DOI
and get both the RIS and Bibtex citations
printed.
"""

import requests

class Works:
    """
    This class prints out RIS or BibTex format citation.
    """

    def __init__(self, doi):
        self.doi = doi
        self.url = f"https://doi.org/{doi}"

    def bibtex(self):
        """
        Outputs BibTeX for a given DOI. ChatGPT 4 assisted
        me in writing this function.
        """
        headers = {"Accept": "application/x-bibtex"}
        response = requests.get(self.url, headers=headers)
        with open('ref.bib', 'w') as bibfile:
            bibfile.write(bibtex) 

        with open('ref.bib') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            entries = bib_database.entries
        return response.text

    def ris(self):
        """
        Outputs RIS for a given DOI. ChatGPT 4 assisted
        me in writing this function.
        """
        headers = {"Accept": "application/x-research-info-systems"}
        response = requests.get(self.url, headers=headers)
        return response.text
    
        
