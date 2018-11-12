import nltk
from nltk.corpus import stopwords
import string

def extractNounVerbCouples(tokenizedSentences):
    nouns = []
    verbs = []
    nounVerbCouples = []
    #removing punctuations from sentences
    punctuations = [p for p in string.punctuation]
    punctuations.append('“')
    punctuations.append('”')
    punctuations.append('’')
    #stop words
    stop_words = set(stopwords.words('english'))
    for sentence in tokenizedSentences:
        nouns = [word for (word, pos) in sentence if (pos == "NOUN" and (word not in punctuations) and (word not in stop_words))]
        verbs = [word for (word, pos) in sentence if (pos == "VERB") and (word not in stop_words)]
        for noun in nouns:
            for verb in verbs:
                couple = (noun, verb)
                nounVerbCouples.append(couple)
        #print("noun verb couples:")
        #print(nounVerbCouples)
    return nounVerbCouples
