# OpenCorpus
Exploring Korean via OpenSubtitles and Lyrics.

This Project Has Several Components: 
1. [Overview](https://github.com/JosephBergman/OpenCorpus/blob/master/README.md#overview) 
2. [Data Collection](https://github.com/JosephBergman/OpenCorpus/blob/master/README.md#data-collection)
3. [Data Analysis](https://github.com/JosephBergman/OpenCorpus/blob/master/README.md#data-analysis)
4. [Future Work](https://github.com/JosephBergman/OpenCorpus/blob/master/README.md#future-work)
5. [Sources](https://github.com/JosephBergman/OpenCorpus/blob/master/README.md#sources)


## Overview
The purpose of this project is to analyze Korean subtitles and lyrics to gain insight about the language. 
+ What are the most frequent words and phrases?
  + ... most frequent nouns
  + ... most frequent verbs 
  + ... most frequent adjectives
+ How long is the average word/sentence? 
  + ... are the first 1000 words shorter than the next 1,000? 
  + ... which syllables are the most common? 
  
Based on those results, we can answer more meaningful questions.
+ Which words should be taught first?
  + ... which nouns
  + ... which verbs
  + ... which phrases 
+ Which songs are easiest for a beginner?
  + ... based on their average word frequency 
  + ... based on their average word length 
  + ... based on the number of unique words 

Ultimately, we want to create a Korean curriculum to emphasize the following. 
+ Teach the most frequents words, nouns, verbs, phrases first 
+ Present songs that are at the user's level
+ Present movie dialogues that are at the user's level 


## Data Collection 
This project relies on having subtitles, song lyrics, and other word frequency lists. Check out the [sources](https://github.com/JosephBergman/OpenCorpus/blob/master/README.md#sources) page to see what we used. The sources are not provided in this Git repository, but we've provided a number of tools you can use to get them. If any of these sources go offline, send me a message and I can provide you with a backup. 

The necessary download files are: 
+ `wikipedia.py` for downloading the Wikipedia korean frequency list 
+ `frequent_nouns.py` for downloading the most frequent Korean nouns 
+ `get_song_lyrics.py` for downloading lyrics for ~250 songs
+ `srt_to_txt.py` for converting subtitle files to plaintext 

Running all of these files would be tedious and error prone. Instead, use the interactive installer!
```python 
from OpenCorpus import interactive 

# Run the file
# 1. change your cwd to a directory where you want to save the files 
# 2. create a new directory to hold the downloads 
# 3. wait while the installer runs
interactive.run() 
```

Next, we are going to want to clean our data 
```python 
from OpenCorpus import datacleaner 

# Convert all the subtitles to plaintext
# 1. download the subtitles (this must be done manually, see sources section)
# 2. run the converter 
datacleaner.convert_all_subtitles(<subtitle-directory-name>) 

# Aggregate all the subtitles into one large file 
datacleaner.generate_subtitle_corpus(<plaintext-directory-name>, output="all_subtitles.txt", korean_only=False)
datacleaner.generate_subtitle_corpus(<plaintext-directory-name>, output="all_subtitles_ko.txt", korean_only=True)

# Aggregate all the song lyrics into one large file
datacleaner.generate_song_corpus(<lyrics-directory-name>, output="all_lyrics.txt", korean_only=False)
datacleaner.generate_song_corpus(<lyrics-directory-name>, output="all_lyrics_ko.txt", korean_only=True)
```


## Data Analysis 
Expected completion April 1, 2018 (no joke!). 


## Future Work 
The ultimate goal of this project is to create a curriculum for learning Korean based on data. Because of this we plan to use the results to create a Korean language learning app. We also hope to automate our scripts to the point we can pass in a desired language (e.g. Spanish, French, Japanese) and have it repeat the entire research process in one go. 

Expected Projects 
+ iOS App for Learning Korean 
+ Web App for Learning Korean 

Expected Features 
+ Korean Chatbots that adjust to user's level
+ Speech recognition for testing pronounciation
+ Spaced-Repetition System based on word frequency
+ Present songs to users that they are most capable of learning
+ Present movie dialogues to users that they are most capable of learning


## Sources 
A number of sources were used for this project. 

Subtitles: 
+ [OpenSubtitles](https://www.opensubtitles.org/en/search/subs) Provided 28 Korean movie subtitles.

Lyrics: 
+ [Kpop Quote](https://kpopquote.wordpress.com/) This blog provided Korean lyrics for over 200 songs. 
+ [A-Z Lyrics](https://www.azlyrics.com/) A-Z lyrics provided my initial set of lyrics (~15 songs).

Other: 
+ [Wikipedia](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800) Provided the 5,800 most frequent Korean words.
+ [Frequency Lists](http://frequencylists.blogspot.com.br/2015/12/the-2000-most-frequently-used-korean.html) Provided the 2,000 most frequent nouns.
