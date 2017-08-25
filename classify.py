import csv
import os
import sys
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
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


# first, build index mapping words in the embeddings set
# to their embedding vector

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

#print embeddings_index['donald']
#print embeddings_index['trump']
#print embeddings_index['clinton']
#print embeddings_index['politics']


# second, prepare text samples and their labels
print('Processing text dataset')

text = []  # list of text samples
labels = [] # list of label ids

replace_words = ["the ", "a ", "an ", "this ", "that "] #cause glitches such as "russian intelligence" -> "russiintelligence"
replace_words = []

with open('/home/triya/Desktop/Link to 2017-RedHen GSoC/detect-bias/data.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
	for row in spamreader:
		#print '...'.join(row)
		row[3] = row[3].lower()
		for word in replace_words:
			row[3] = row[3].replace(word, '')
		#print row[3]
		#row[3] = row[3].replace(" ", "_")
		#print row[3]
		row_out = row[3][1:].split(',')
		text.append(row_out)
		labels.append(int(float(row[0])*10))	
	
text_flat = [item for sublist in text for item in sublist]
#print text_flat


# finally, vectorize the text samples into a 2D integer tensor
tokenizer = Tokenizer(nb_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(text_flat)
sequences = tokenizer.texts_to_sequences(text_flat)

word_index = tokenizer.word_index
#print word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)[:300]

labels = to_categorical(np.asarray(labels), 11)[:300]
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)


# split the data into a training set and a validation set
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
nb_validation_samples = int(VALIDATION_SPLIT * data.shape[0])

x_train = data[:-nb_validation_samples]
y_train = labels[:-nb_validation_samples]
x_val = data[-nb_validation_samples:]
y_val = labels[-nb_validation_samples:]

print('Preparing embedding matrix.')


# prepare embedding matrix
num_words = len(word_index) + 1
embedding_matrix = np.zeros((num_words, EMBEDDING_DIM))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector


# load pre-trained word embeddings into an Embedding layer
# note that we set trainable = False so as to keep the embeddings fixed
#embedding_layer = Embedding(num_words,
#                            EMBEDDING_DIM,
#                            weights=[embedding_matrix],
#                            input_length=MAX_SEQUENCE_LENGTH,
#                            trainable=False)

embedding_layer = Embedding(num_words,
                            EMBEDDING_DIM,
                            input_length=MAX_SEQUENCE_LENGTH)

print('Training model.')

# train a 1D convnet with global maxpooling
sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedded_sequences = embedding_layer(sequence_input)
x = Conv1D(128, 5, activation='relu')(embedded_sequences)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(35)(x)  # global max pooling
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
preds = Dense(11, activation='softmax')(x)

model = Model(sequence_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])

model.fit(x_train, y_train, validation_data=(x_val, y_val),
          batch_size=128)
