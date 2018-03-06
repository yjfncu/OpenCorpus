#
# OpenCorpus/get_song_lyrics.py
# Joseph Bergman
#
# Scrapes song lyrics from https://kpopquote.wordpress.com/
import re
import requests
from bs4 import BeautifulSoup

regexes = [
    re.compile(r'\n?\[Lyric\] .* \((.*)\) – (.*) \['),
    re.compile(r'\n?\[Lyric\] (.*) – (.*) \[')
]

def get_soup(url):
    """Returns a soup from a given URL."""
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    return soup

def get_post_data(post):
    """Return the song and artist for a given post."""
    head = post.find('div', attrs={'class': 'p-head'}).find('h2').text

    result = None
    for regex in regexes:
        result = regex.match(head)
        if result: break

    song = urlify(result.group(1))
    artist = urlify(result.group(2))
    return song, artist

def urlify(text):
    """URLify some text by lowercasing and replacing spaces with dashes."""
    text = re.sub(r"[^\w\s]", '', text.strip())
    text = re.sub(r"\s+", '-', text)
    text = text.lower()
    return text



#
# SCRIPT FOR RETRIEVING SONG FILES
#

soup = get_soup("https://kpopquote.wordpress.com/page/1")
posts = soup.find_all('div', attrs={'class': 'post'})

for post in posts:
    song, artist = get_post_data(post)
    print(song, artist)
