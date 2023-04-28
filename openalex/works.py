import time
import pytest
import requests
import base64
import matplotlib.pyplot as plt
from IPython.core.pylabtools import print_figure
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase


class Works:
    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def __str__(self):
        return "str"

    def bibtex(self):
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors[0:-1]) + " and" + _authors[-1]

        title = self.data["title"]

        journal = self.data["host_venue"]["display_name"]
        volume = self.data["biblio"]["volume"]

        issue = self.data["biblio"]["issue"]
        if issue is None:
            issue = ", "
        else:
            issue = ", " + issue

        pages = "-".join(
            [self.data["biblio"]["first_page"], self.data["biblio"]["last_page"]]
        )
        year = self.data["publication_year"]
        citedby = self.data["cited_by_count"]

        oa = self.data["id"]
        s = f"\nauthor = {authors},\ntitle = {title},\nvolume = {volume},\nnumber = {issue},\npages = {pages},\nyear = {year},\ndoi = {self.data['doi']},\nurl = {self.oaid},\nDATE_ADDED = {self.data['updated_date']}"
        # s = f'author = {authors},\n title = {title},\n volume = {volume},\n number = {issue},\n pages = {pages},\n year = {year},\n doi = {self.data["doi"]},\n url = {self.oaid}, \n DATE_ADDED = {self.data['updated_date']}'
        return s

    def related_works(self):
        rworks = []
        for rw_url in self.data["related_works"]:
            rw = Works(rw_url)
            rworks += [rw]
            time.sleep(0.101)
        return rworks

    def references(self):
        ref_works = []
        for rw_url in self.data["referenced_works"]:
            rw = Works(rw_url)
            ref_works += [rw]
            time.sleep(0.101)
        return ref_works

    def citing_works(self):
        url = self.data["cited_by_api_url"]
        cited_works = requests.get(url).json()
        res = cited_works["results"]
        count = 0
        for i in res:
            count += 1
            print(i["display_name"])

    def ris(self):
        fields = []
        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        ris = "\n".join(fields)
        ris64 = base64.b64encode(ris.encode("utf-8")).decode("utf8")
        uri = f'<pre>{ris}<pre><br><a href="data:text/plain;base64,{ris64}" download="ris">Download RIS</a>'
        from IPython.display import HTML

        return HTML(uri)
