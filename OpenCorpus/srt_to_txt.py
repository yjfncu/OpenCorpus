#
# OpenCorpus/srt_to_txt.py
# Joseph Bergman
#
# Get the raw text from a .srt file and write it to a .txt file
import sys
import os
import re


def convert_srt_to_txt(filepath, output=""):
    """Convert the .srt file to a .txt file keeping only the subtitles.

    Args:
        filepath (str): The path to the .srt file to convert
        output (str) (optional): The name of an output directory

    Returns:
        Bool: True if successful, False otherwise
    """
    # Open the input file, create the output file
    input_file = open(filepath, "r")
    output_file_name = os.path.basename(filepath)
    output_file = open(output + output_file_name[:-3] + "txt", "w+")

    # Common regex patters
    sequence = re.compile(r'^\d+$')
    times = re.compile(r'^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d$')
    tags = re.compile(r'(<\w+>)?([^<]*)(</\w+>)?')

    # Iterate through all the lines in the .srt file
    try:
        for line in input_file:

            # If the line is metadata, ignore it
            if sequence.match(line) or times.match(line):
                continue

            # Remove HTML tags
            result = tags.match(line)
            if result:
                line = result.group(2)

            # Remove artifacts from beginning and end of the line
            line = line.lstrip("' \" - - . ♪ ? ~")
            line = line.rstrip("' \" - - . ♪ ? ~ \n")

            # Write the line to file
            output_file.write(line + '\n')

    except UnicodeDecodeError:
        # If there is an error, remove the file, report error, return False
        input_file.close()
        output_file.close()
        os.remove(output_file.name)
        print("UnicodeDecodeError: {}".format(input_file.name))
        return False

    # Close the files and return True
    input_file.close()
    output_file.close()
    return True


def convert_directory_to_txt(directory):
    """Convert all srt files in a directory to txt files.

    Creates a new directory with the same name + Txt.
    Stores all the txt files in the new directory.

    Args:
        directory (str): The name a directory containing srt files

    Returns:
        Bool: True if successful, False otherwise.
    """
    # Get all the files in the given directory
    files = [f for f in os.listdir(directory) if f.endswith(".srt")]

    if files is None:
        print("Error: No files found.")
        return False

    # For each file, convert it to a Txt
    output = directory + "Txt"
    if not os.path.exists(output):
        os.makedirs(output)
    for f in files:
        convert_srt_to_txt(os.path.join(directory,f), output)

    return True



if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Error: not enough arguments")
        print("srt_to_txt.py <input_file_path>")
        sys.exit(0)

    filepath = sys.argv[1]
    if filepath[-4:] != ".srt":
        print("Error: input file must be a .srt file")
        sys.exit(0)

    print("Converting to .txt")
    if convert_srt_to_txt(filepath):
        print("Success")
    else:
        print("Error")
