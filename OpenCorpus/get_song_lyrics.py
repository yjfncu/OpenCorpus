#
# OpenCorpus/get_song_lyrics.py
# Joseph Bergman
#
# Scrapes song lyrics from https://kpopquote.wordpress.com/
import re
import os.path
import requests
from bs4 import BeautifulSoup

regexes = [
    re.compile(r'\n?\[Lyric\] .* \(([^-–]*)\) – (.*) \['),
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
    #
    result = None
    for regex in regexes:
        result = regex.match(head)
        if result: break
        #
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
    if paragraphs[0].get_text().lower() != "hangul":
        return []
        #
    # Select only the Korean paragraphs
    korean = []
    for paragraph in paragraphs[1:]:
        text = paragraph.get_text().lower()
        if text == "romanization" or text == "english": break
        if text.startswith("credit: "): break
        text = text.rstrip('\n')
        korean.append(text + '\n')
        #
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
    filename = "{}.{}.txt".format(song, artist)
    if os.path.isfile(filename) and overwrite is False:
        return False
    #
    output = open(filename, 'w+')
    for paragraph in paragraphs:
        output.write(paragraph)
    #
    output.close()
    return True

def get_all_songs(url):
    soup = get_soup(url)
    posts = soup.find_all('div', attrs={'class': 'post'})
    #
    for post in posts:
        song, artist = get_song_and_artist(post)
        korean = get_korean_paragraphs(post)
        write_to_file(song, artist, korean)



soup = get_soup("https://kpopquote.wordpress.com/page/1")
