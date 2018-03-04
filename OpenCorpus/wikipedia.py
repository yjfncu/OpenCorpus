#
# OpenCorpus/wikipedia.py
# Joseph Bergman
#
# Download the Korean word frequency list from Wikipedia
from bs4 import BeautifulSoup
import requests

# Get the URL
url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

# Select the table
table = soup.find('table', attrs={'class': 'prettytable'})
columns = table.findAll('td')

# For each column, extract the words
frequency_list = []
for column in columns:
    words = column.findAll('dd')
    for word in words:
        text = word.find('a').contents[0]
        frequency_list.append(text)

# Write the result to a CSV
output_file = open("sources/frequent_wikipedia.csv", "w+")
for (index,word) in enumerate(frequency_list):
    output_file.write("{},{}\n".format(index+1,word))
output_file.close()
