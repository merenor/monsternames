from bs4 import BeautifulSoup as bs
import requests
import re
import string
import time
import codecs
from random import choice

def load_attributes(file):
    attributes = []

    with codecs.open('attributes-sorted.txt', 'r', 'utf-8') as f:
        for line in f:
            attributes.append(line.strip())

    return attributes

def get_names(fms):
    all = []

    for l in list(string.ascii_uppercase):
    #for l in ['O']:
        BASE_URL = "https://www.mithrilandmages.com/utilities/MedievalBrowse.php?"
        ARGUMENT = "letter={letter}&fms={fms}".format(letter=l, fms=fms)
        print("Search ", BASE_URL + ARGUMENT)

        r = requests.get(BASE_URL + ARGUMENT)
        soup = bs(r.text)

        medNameColumns = soup.find("div", {"id": "medNameColumns"})

        names = re.findall('([A-Z][^< ]*)', str(medNameColumns))
        for n in names:
            if n.startswith(l):
                all.append(n)
        time.sleep(2)

    return all

monster_attributes = load_attributes('attributes-sorted.txt')

all_male_names = get_names('M')

with codecs.open('male-names.txt', 'w', 'utf-8') as f:
    for n in all_male_names:
        f.write("{},der,{},\n".format(n, choice(monster_attributes)))
