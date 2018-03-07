#
# OpenCorpus/get_song_lyrics.py
# Joseph Bergman
#
# Scrapes song lyrics from https://kpopquote.wordpress.com/
from random import randint
from time import sleep
import os.path
import re

from bs4 import BeautifulSoup
import requests



regexes = [
    # Match: [Lyric] <Korean Name> (<English Name>) - Artist ...
    re.compile(r'\n?\[Lyric\] .* \(([^-–]*)\) – (.*) \['),
    # Match: [Lyric] <Name> - Artist ...
    re.compile(r'\n?\[Lyric\] ([^-–]*) – (.*) \[')
]


def get_soup(url):
    """Returns a soup from a given URL."""
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


def get_song_and_artist(post):
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


def get_korean_paragraphs(post):
    """Return all the Hangul paragraphs from a given post."""
    content = post.find('div', attrs={'class': 'p-con'})
    paragraphs = content.find_all('p')

    # Find the initial pagraph
    has_korean = False
    index = -1
    for i,paragraph in enumerate(paragraphs):
        text = paragraph.get_text().lower()
        if text == "hangul":
            has_korean = True
            index = i+1
            break

    # If no Korean is found, return an empty list
    if not has_korean: return []

    # Select only the Korean paragraphs
    korean = []
    for paragraph in paragraphs[index:]:
        text = paragraph.get_text().lower()
        if text == "romanization" or text == "english": break
        if text.startswith("cr: ") or text.startswith("credit:"): break
        text = text.rstrip('\n')
        korean.append(text + '\n')

    return korean


def write_to_file(song, artist, paragraphs, overwrite=False):
    """Given a song, artist, and paragraphs write the song to a file.

    Given a song (title), artist name, and a list of Korean paragraphs
    write the song to a .txt file. The file name is "artist.song.txt".
    By default, if a file already exists with that name nothing will be
    done. Setting overwrite to true will overwrite existing files.

    Args:
        song (str): The song title
        artist (str): The artist name
        paragraphs (List<str>): A list of lines to write to the file.
        overwrite (optional, bool): Whether or not to overwrite files

    Returns:
        True if the file was successfully created and written
        False if there was an error or the file exists (and overwrite=False)
    """
    filename = "{}.{}.txt".format(artist, song)
    if os.path.isfile(filename) and overwrite is False:
        return False

    output = open(filename, 'w+')
    for paragraph in paragraphs:
        output.write(paragraph)

    output.close()

    return True


def get_all_songs(url):
    soup = get_soup(url)
    posts = soup.find_all('div', attrs={'class': 'post'})

    for post in posts:
        try:
            song, artist = get_song_and_artist(post)
            korean = get_korean_paragraphs(post)
            if korean:
                write_to_file(song, artist, korean)
            else:
                print("Nothing Found: {}, {}, {}".format(song, artist, url))
        except:
            print("Exception: {}".format(url))
            continue

#
# Run as main to get all songs. When last run (Mar 06, 18), there were 36 pages.
#
if __name__ == '__main__':

    # Note: We sleep a random amount of time between requests
    # to be good netizens. Also, so we don't get blocked :D.
    for i in range(1,37):
        sleep(randint(10,20))
        url = "https://kpopquote.wordpress.com/page/{}".format(i)
        get_all_songs(url)
