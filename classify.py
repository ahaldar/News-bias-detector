import csv

text = []

replace_words = ["the ", "a ", "an ", "this ", "that "]

with open('/home/triya/Desktop/Link to 2017-RedHen GSoC/detect-bias/data.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
	for row in spamreader:
		#print '...'.join(row)
		row[3] = row[3].lower()
		for word in replace_words:
			row[3] = row[3].replace(word, '')
		#print row[3]
		row[3] = row[3].replace(" ", "_")
		#print row[3]
		row_out = row[3][1:].split(',')
		text.append(row_out)

text_flat = [item for sublist in text for item in sublist]
print text_flat


import os
import sys
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model


BASE_DIR = '/home/triya/Desktop/'
GLOVE_DIR = BASE_DIR + '/glove.6B/'
TEXT_DATA_DIR = BASE_DIR + '/20_newsgroup/'
MAX_SEQUENCE_LENGTH = 1000
MAX_NB_WORDS = 20000
EMBEDDING_DIM = 100
VALIDATION_SPLIT = 0.2


print('Indexing word vectors.')

embeddings_index = {}
f = open(os.path.join(GLOVE_DIR, 'glove.6B.100d.txt'))
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))


tokenizer = Tokenizer(nb_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(text_flat)
sequences = tokenizer.texts_to_sequences(text_flat)

word_index = tokenizer.word_index
print word_index
print('Found %s unique tokens.' % len(word_index))

#print embeddings_index['middle_class']
#print embeddings_index['first_lady']
#print embeddings_index['white_house']
print embeddings_index['candidates']
print embeddings_index['republicans']


import gensim

# Load Google's pre-trained Word2Vec model.
model = gensim.models.Word2Vec.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)  

print model.wv['middle_class']
print model.wv['first_lady']
print model.wv['white_house']
print model.wv['candidates']
print model.wv['republicans']
