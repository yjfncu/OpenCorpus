#
# OpenCorpus/srt_to_txt.py
# Joseph Bergman
#
# Get the raw text from a .srt file and write it to a .txt file
import re


def convert_srt_to_txt(filepath):
    """Convert the .srt file to a .txt file keeping only the subtitles.

    Args:
        filepath (str): The path to the .srt file to convert

    Returns:
        Bool: True is successful, False if there was an error
    """
    # Open the input file, create the output file
    input_file = open(filepath, "r")
    output_file = open(filepath[:-3] + ".txt", "w+")

    # Common regex patters
    sequence = re.compile(r'^\d+$')
    times = re.compile(r'^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d$')

    # Iterate through all the lines in the .srt file
    for line in input_file:

        # If the line is metadata, ignore it
        if sequence.match(line) or times.match(line):
            continue

        # Remove artifacts from beginning and end of the line
        line = line.strip("'\"")
        output_file.write(line)

    # Close the files and return True
    input_file.close()
    output_file.close()
    return True
