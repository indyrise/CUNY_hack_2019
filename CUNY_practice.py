#WITH NLP YOU CAN DO MORE MEANINGGUL TEXT PROCESSING, SUCH AS UNDERSTANDING THE PARTS OF SPEECH FOR THE PARSED WORDS
#download the spacy library using 'pip install spacy'
#download a language model, in this case for English using python3 -m spacy download en_core_web_sm

#import the spacy library

import spacy


fname = input("Enter file name: ")

if len(fname) < 1: fname = 'words.txt'
fh = open(fname)
#load the language model that you downloaded

nlp = spacy.load("en_core_web_sm")

#find the tokens/parts of speech and the types using the spacy library

words = [] #new list called words
wordtype = dict() #this defines a new dictionary called wordtype to contain the words and the POS type that we find after NLP analysis

for line in fh:
    data = nlp(line)
    for token in data:
        word = token.text
        type = token.pos_

        if word in wordtype: continue
        else: wordtype.update({word:type})

        if word in words: continue
        else: words.append(word)

print('\n***This is the list of words that were parsed using NLP***\n')

print(words)

print('\n***This is the dictionary of words and their POS types we get using NLP***\n')

print (wordtype)


#count how many times each token type appears in the text

counts = dict() #define a dictionary called counts that will hold the number of times each POS type shows up in the wordtype dictionary

for v in wordtype.values():
    counts[v] = counts.get(v,0) + 1

print('\n***These are the counts for the different parts of speech encountered in this text***\n')
print(counts)


#for token in data:
    #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #        token.shape_, token.is_alpha, token.is_stop)

#list = []

#for line in fh:
#    words = (line.rstrip()).split()
#    for word in words:
#        if word in list:
#            continue
#        else:
#            list.append(word)

#list.sort()

#print(list)
