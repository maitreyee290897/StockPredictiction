import nltk
from nltk.corpus import stopwords
import string
from parser import extractNounVerbCouples

#tokenize document
def preprocess(document):
    #splitting document into sentences
   sentences = nltk.sent_tokenize(document)

    #tokenize each of the sentences
   tokenizedSentences = [nltk.word_tokenize(sent) for sent in sentences]
   tokenizedSentences = [nltk.pos_tag(sent, tagset='universal') for sent in tokenizedSentences]

   #extract noun verb couples
   nounVerbCouples = extractNounVerbCouples(tokenizedSentences)
   print("noun verb couples:")
   print(nounVerbCouples)
   return

sentences = preprocess('“X Company’s sales increased by 20 percent in the second quarter. This is second\'s sentence.”')
