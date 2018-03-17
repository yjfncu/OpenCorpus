#
# OpenCorpus/ttmik_iyagi.py
# Joseph Bergman
#
# Download scripts of Iyagi from Korean Wiki Project
import requests
from bs4 import BeautifulSoup


#
# Getting the webpage
#
URL = "http://www.koreanwikiproject.com/wiki/index.php?title=TTMIK_Iyagi"


def get_soup(url=URL):
    """Get the BeautifulSoup of the entire webpage."""
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    return soup



#
# Parsing the webpage
#
def get_table_rows(soup):
    """Returns the non-header rows from the table (soup objects)."""
    table = soup.find('table', attrs={'class': 'wikitable'})
    rows = table.find_all('tr', recursive=False)
    return rows[1:]


def get_iyagi_links(soup):
    """Returns a list of links to the TTMIK Iyagis."""
    iyagi_links = []
    for row in get_table_rows(soup):
        row_data = row.find_all('td', recursive=False)
        iyagi_link = row_data[1].find('a')['href']
        iyagi_links.append(iyagi_link)
    return iyagi_links


def get_transcript_links(soup):
    """Returns a list of links to the TTMIK Iyagi English Transcripts."""
    transcript_links = []
    for row in get_table_rows(soup):
        row_data = row.find_all('td', recursive=False)
        link_table = row_data[2].find('table', attrs={'class': 'languageTable'})
        english_row = link_table.find_all('tr')[1]
        english_link_anchor = english_row.find_all('td')[0].find_all('a')[1]
        url = 'http://www.koreanwikiproject.com/' + english_link_anchor['href']
        transcript_links.append(url)
        if english_link_anchor.get_text() != 'English':
            print("WARNING: May be non-English link. Check if source changed.")
    return transcript_links


#
# Getting the transcripts
#
def get_transcripts(transcipts):
    """Given a list of links, download and save all the transcripts."""
    pass
