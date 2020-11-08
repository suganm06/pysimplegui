from nltk.corpus import wordnet as wn

def get_meaning(word):
    synset = wn.synsets(word)
    if synset:
        return synset[0].definition()
    else:
        return None

def get_synonyms(word):
    synonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma:
                synonyms.append(lemma.name())
    return set(synonyms) 

def get_antonyms(word):
    antonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())                
    return set(antonyms)          