import codecs
from random import sample


def monsterchoice(amount):

    allmonsters = []
    choicelist = []
    indexes = []

    with codecs.open('all-names.txt', 'r', 'utf-8') as f:
        for line in f:
            allmonsters.append(line.strip())

    indexes = sample(range(len(allmonsters)-1), amount)
    for i in indexes:
        choicelist.append(allmonsters[i])

    with codecs.open('monsternames_' + str(amount) + '.txt', 'w', 'utf-8') as f:
        f.write("name,gender,attribute,id\n")
        for c in choicelist:
            f.write(c + '\n')


monsterchoice(250)
