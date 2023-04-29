"""
Module for working with scholarly works from the OpenAlex API.
"""

import base64
import requests

class Works:
    """
    A class representing a scholarly work.

    Attributes:
        oaid (str): The OpenAlex identifier of the work.
        data (dict): The JSON data for the work obtained from the OpenAlex API.
    """

    def __init__(self, oaid):
        """
        Constructs a new Works object.

        Args:
            oaid (str): The OpenAlex identifier of the work.
        """
        self.oaid = oaid
        self.req = requests.get(f'https://api.openalex.org/works/{oaid}')
        self.data = self.req.json()
        
    def new(self):
        titles = self.data['title']
        volume = self.data['biblio']['volume']
        issue = self.data['biblio']['issue']
        return titles

    def bibtex(self):
        """
        Returns the BibTeX string for the work.

        Returns:
            str: The BibTeX string.
        """
        _authors = [au['author']['display_name'] for au in self.data['authorships']]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ', '.join(_authors[0:-1]) + ' and' + _authors[-1]

        title = self.data['title']

        volume = self.data['biblio']['volume']

        issue = self.data['biblio']['issue']
        if issue is None:
            issue = ', '
        else:
            issue = ', ' + issue

        pages = '-'.join([self.data['biblio']['first_page'], self.data['biblio']['last_page']])
        year = self.data['publication_year']

        seq = (
            f'\nauthor = {authors},\n'
            f'title = {title},\n'
            f'volume = {volume},\n'
            f'number = {issue},\n'
            f'pages = {pages},\n'
            f'year = {year},\n'
            f'doi = "{self.data["doi"]}",\n'
            f'url = "{self.oaid}",\n'
            f'DATE_ADDED = {self.data["updated_date"]}'
        )

        return seq
