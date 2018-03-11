#
# OpenCorpus/wikipedia.py
# Joseph Bergman
#
# Download the Korean word frequency list from Wikipedia
from bs4 import BeautifulSoup
import requests

URL = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"



#
# Functions for getting data from the web
#
def get_soup(url):
    """Returns the Beautiful soup from the Wikipedia page."""
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    return soup



#
# Functions for working with the BeautifulSoup
#
def get_word_table(soup):
    """Returns the words table as a list of the columns."""
    table = soup.find('table', attrs={'class': 'prettytable'})
    columns = table.findAll('td')
    return columns


def get_all_cells(soup):
    """Returns all the table cells in order of frequency."""
    all_cells = []
    for column in get_word_table(soup): all_cells += column.findAll('dd')
    return all_cells



#
# Functions for extracting data from the cells
#
def get_word(cell):
    """Given a table cell, extract the Korean word from it."""
    return cell.find('a').contents[0]


def get_url(cell):
    """Given a cell, extract the link to the Wiktionary page."""
    a = cell.find('a')
    url = None
    if not a['title'].endswith("(page does not exist)"):
        url = "https://en.wiktionary.org" + a['href']
    return url



#
# Functions for extracting all data
#
def get_all_words(soup):
    """Given the page soup, return all of the words in order."""
    cells = get_all_cells(soup)
    words = []
    for cell in cells:
        words.append(get_word(cell))
    return words


def get_all_urls(soup):
    """Given the page soup, return all of the URLs (None if page DNE)."""
    cells = get_all_cells(soup)
    urls = []
    for cell in cells:
        urls.append(get_url(cell))
    return urls



# # Write the result to a CSV
# output_file = open("sources/frequent_wikipedia.csv", "w+")
# for (index,word) in enumerate(frequency_list):
#     output_file.write("{},{}\n".format(index+1,word))
# output_file.close()
