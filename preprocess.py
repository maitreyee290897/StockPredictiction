import nltk
#tokenize document
def preprocess(document):
   sentences = nltk.sent_tokenize(document)
   sentences = [nltk.word_tokenize(sent) for sent in sentences]
   sentences = [nltk.pos_tag(sent, tagset='universal') for sent in sentences]
   return sentences

sentences = preprocess('The little yellow dog barked at the cat.')
print(sentences)

#TODO Now group these tokens into chunks(Noun + verb)
