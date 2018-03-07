# OpenCorpus
Exploring the Korean language via OpenSubtitles and Lyrics.


## Getting Started
All source code for the project can be found [here](https://github.com/JosephBergman/OpenCorpus/tree/master/OpenCorpus).

Getting Started:
1. Check out the README in the [sources](https://github.com/JosephBergman/OpenCorpus/tree/master/OpenCorpus/sources) directory
2. If you want to recreate this project, download those files, or contact me for my backups

Downloading the Sources:
1. Use `srt_to_txt.py` to convert a single srt file or a directory of srt files to raw text files.  
2. Use `get_song_lyrics` to download over 200 song lyrics.
3. `wikipedia.py` can be used to download [Wikipedia's Korean Frequency List](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800) as a CSV.
4. `frequent_nouns.py` can be used to download this [Korean Noun Frequency List](http://frequencylists.blogspot.com.br/2015/12/the-2000-most-frequently-used-korean.html) as a CSV.


## Downloading the Sources

### Convert .srt to .txt
Suppose we have a file named movie.srt and want to convert it to movie.txt with just the raw text.
```python
import srt_to_txt

# This will create a file movie.txt in our current directory
srt_to_txt.convert_srt_to_txt("path/to/desired/file/movie.srt")

# This will create a file movie.txt in desired/path/movie.txt (the directory must exist)
srt_to_txt.convert_srt_to_txt("path/to/desired/file/movie.srt", "desired/path")
```

### Convert a directory of .srt to .txt
Suppose we have a directory "inputs" and want to convert all .srt files to .txt files
```python
import srt_to_txt

# All output files will be in desired/path/inputTxt
srt_to_txt.convert_directory_to_txt("desired/path/input")
```

### Downloading the Song Lyrics
Some song lyrics were downloaded manually, but most were scraped from [this wonderful blog](https://kpopquote.wordpress.com/). You can find a script for downloading all of these songs in `get_song_lyrics.py`. Run the script and it will convert all the lyrics to .txt files for you. However, this will take 3-5 minutes since we wait 10 - 20 seconds between each request to avoid getting blocked. Files are saved as <artist.song.txt>. 

### Downloading the Wikipedia Frequency List
Just run `python wikipedia.py`. This will create a file called "frequent_wikipedia.csv" in the sources directory.

The format of the CSV is "rank,word\n".

### Downloading the Noun Frequency List
Just run `python frequent_nouns.py`. This will create a file called "frequent_nouns.csv" in the sources directory.

The format of the CSV is "rank,korean_word,english_word\n"
