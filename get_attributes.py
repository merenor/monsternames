from bs4 import BeautifulSoup as bs
import requests
import re
import codecs

def get_attributes_from_url():
    words = []
    URL = "https://synonyme.woxikon.de/synonyme/grausam.php"

    r = requests.get(URL)
    soup = bs(r.text)

    synonyms = soup.find_all("div", {"class": "synonyms-list-content"})

    with codecs.open('attributes-raw.txt', 'w', 'utf-8') as f:
        for s in synonyms:
            cur_words = re.findall('([a-zäüöß]*)\,', s.text.strip())
            for w in cur_words:
                f.write(w + '\n')

def sort_attributes():
    attributes_list = []

    with codecs.open('attributes-raw.txt', 'r', 'utf-8') as f:
        for line in f:
            if line not in attributes_list:
                attributes_list.append(line)

    with codecs.open('attributes-sorted.txt', 'w', 'utf-8') as f:
        for a in attributes_list:
            f.write(a)


sort_attributes()
