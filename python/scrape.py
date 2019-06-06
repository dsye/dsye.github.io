#I mporting libraries needed for web scraping
import nltk
from bs4 import BeautifulSoup
from urllib import request

# stored url we are using
url = "https://github.com/humanitiesprogramming/scraping-corpus"

# using that url, get the HTML from it
html = request.urlopen(url).read()

# took url and turned it into a soup object
soup = BeautifulSoup(html, 'lxml')
our_text= soup.text
links = soup.find_all('a')[0:10]

# print(our_text[0:2000])
# replace the lne breaks with spaces
#print(soup.text.replace('\n', ' '))

links_html = soup.select('td.content a')
this_link = links_html[0]
# href = hypertext reference; next step creates a list of url extensions
#print(this_link['href'])
urls = []
# take each link and make a new list w/ processed urls
for link in links_html:
    to_append = link['href'].replace('blob/','')
    urls.append("https://raw.githubusercontent.com" + to_append)

test_url = urls[3]
#looping through texts from each url
corpus_texts = []

for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)
    print("Scraping " + url)
# print(len(corpus_texts))
# print(len(corpus_texts[0]))

this_text = corpus_texts[0]
process_this_text = nltk.word_tokenize(this_text)
# print(process_this_text[0:20])
# print(nltk.FreqDist(process_this_text).most_common(50))
import csv
with open('scrapetext.csv', 'w', newline= '') as fout:
    data = csv.writer(fout)
    data.writerow(['Word', 'Word Count'])
    for row in nltk.FreqDist(process_this_text):
        data.writerow(nltk.FreqDist(process_this_text).most_common(50))
