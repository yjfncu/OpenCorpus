#
# OpenCorpus/word_frequency.py
# Joseph Bergman
#
# Given a .txt file provide statistics on the most frequent words.


def get_word_frequency(filepath):
    """Return a dictionary of word => frequency.

    This word counter is based on spaces not NLTK or KoNLPy tokenization.

    Args:
        filepath (str): Filepath to a .txt file

    Return:
        dict: A dictionary mapping the word to its frequency.
    """
    # Open the input file
    input_file = open(filepath, "r")

    # Read each line and count the words
    count = {}
    for line in input_file:
        words = line.split()
        words = [w.strip(" ,.?") for w in words]
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

    # Close the input file
    input_file.close()
    return count
