#!/usr/bin/env python
# coding: utf-8


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt
import cufflinks as cf

# from google.colab import drive
# drive.mount('/content/drive')

# cd drive/'My Drive'/'Drive Files'/'Colab Notebooks'/'FYP'

df = pd.read_csv('Raabta_dataset - donations.csv')
# print(df.info())

print(df.head())
df = df[['Label', 'body']]
df.Label.value_counts()
df['Label'].unique()
# !pip install cufflinks

# cf.go_offline()
# cf.set_config_file(offline=False, world_readable=True)
# df['Label'].value_counts().sort_values(ascending=False).iplot(kind='bar', yTitle='Number of Complaints', title='Number complaints in each product')
def print_plot(index):
    example = df[df.index == index][['body', 'Label']].values[0]
    if len(example) > 0:
        print(example[0])
        print('Label:', example[1])
print_plot(10)

print_plot(100)

import nltk
nltk.download('stopwords')

df = df.reset_index(drop=True)
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
    text = BAD_SYMBOLS_RE.sub('', text) # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing. 
    text = text.replace('x', '')
#    text = re.sub(r'\W+', '', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove stopwors from text
    return text
df['body'] = df['body'].apply(clean_text)
df['body'] = df['body'].str.replace('\d+', '')

print_plot(10)
print_plot(100)

# The maximum number of words to be used. (most frequent)
MAX_NB_WORDS = 50000
# Max number of words in each complaint.
MAX_SEQUENCE_LENGTH = 250
# This is fixed.
EMBEDDING_DIM = 100
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(df['body'].values)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

X = tokenizer.texts_to_sequences(df['body'].values)
X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
print('Shape of data tensor:', X.shape)

Y = pd.get_dummies(df['Label']).values
print('Shape of label tensor:', Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.10, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)


model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
# model.add(tf.keras.layers.SpatialDropout1D(0.2))
model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(500, dropout=0.1, recurrent_dropout=0.1)))

# model.add(tf.keras.layers.LSTM(50)) #, dropout=0.2, recurrent_dropout=0.2
model.add(tf.keras.layers.Dense(7, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

epochs = 18
batch_size = 128

history = model.fit(X_train, Y_train, epochs=epochs, validation_split= 0.10, batch_size=batch_size) 


# ##### Test Accuracy

accr = model.evaluate (X_test,Y_test)
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))


# ##### Train Accuracy

accr = model.evaluate (X_train, Y_train)
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))

plt.title('Loss')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show();


plt.title('Accuracy')
plt.plot(history.history['acc'], label='train')
plt.plot(history.history['val_acc'], label='test')
plt.legend()
plt.show();


new_request = ['I havent taken any classes since forever, and my university is lagging because of that']
seq = tokenizer.texts_to_sequences(new_request)
padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
pred = model.predict(padded)
labels = ['basicneeds', 'loan', 'medical', 'misc', 'bills', 'education',
       'pets']
print(pred, labels[np.argmax(pred)])

model.save_weights('./checkpoints/my_checkpoint')
model.save('init.md5')

# model.load_weights('./checkpoints/my_checkpoint')