#
# OpenCorpus/frequent_nouns.py
# Joseph Bergman
#
# Download the most frequent nouns from frequencylists.blogspot.com
from bs4 import BeautifulSoup
import requests
import re

# Get the URL
url = "http://frequencylists.blogspot.com.br/2015/12/the-2000-most-frequently-used-korean.html"
r = requests.get(url)
soup = BeautifulSoup(r.content)

# Select the table
div = soup.find('div', attrs={'class': 'post-body'})
words = div.findAll('p')

# Create a regex for matching the words
paragraph = re.compile(r'^\n?(\d+)\.\s+(\w+) – (.+) ')

# For each column, extract the words
frequency_list = []
for word in words:
    result = paragraph.match(word.get_text())
    if result:
        number = result.group(1)
        english = result.group(2)
        korean = result.group(3)
    else:
        continue

    # Add to the frequency list (#,Korean,English)
    frequency_list.append((number,korean,english))

# Write the result to a CSV
output_file = open("frequent_nouns.csv", "w+")
for (num,kor,eng) in frequency_list:
    output_file.write("{},{},{}\n".format(num,kor,eng))
output_file.close()

print(frequency_list)
