import json
import requests
import time
from random import sample
import codecs

def get_synonyms(wort):
""" Uses the openthesaurus.de API to get a list of unique synonyms """

    URL = 'https://www.openthesaurus.de/synonyme/search?q={wort}&format=application/json'
    response = []

    r = requests.get(URL.format(wort=wort))
    print("... Waiting ...")
    # be gentle to the server, dude
    time.sleep(10)

    data = json.loads(r.text)

    for synset in data['synsets']:
        for term in synset['terms']:
            if ' ' not in term['term'] and term['term'] not in response:
                print(">", term['term'])
                response.append(term['term'])

    return response


def create_syn_list(wort):
""" Creates a list of synonyms to a given word. The first list of given
    synonyms is used to search deeper in the database. """

    syn_list = get_synonyms(wort)
    first_syn_list = list(syn_list)

    print(">>> Einträge:", len(first_syn_list))
    for syn in first_syn_list:
        print(">>", syn)
        new_syn = get_synonyms(syn)
        for new in new_syn:
            if new not in syn_list:
                syn_list.append(new)

    return syn_list


if __name__ == '__main__':
    master_list = create_syn_list('grausam')

    with codecs.open("synlist.txt", "w", encoding="utf-8") as f:
        for word in master_list:
            f.write(word + '\n')
