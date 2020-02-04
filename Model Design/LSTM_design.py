#!/usr/bin/env python
# coding: utf-8
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
import nltk
nltk.download('stopwords')

# Constants 
epochs = 18
batch_size = 128

### Preprocessing of Dataset

df = pd.read_csv('RDS.csv')
df = df[['Label', 'body']]

df.replace({'Label': {'Basic needs': 'basicneeds', 
                      'basic needs': 'basicneeds', 
                      'Basic needs/medical?': 'basicneeds',
                      'Basic Needs': 'basicneeds',
                      'baaic needs': 'basicneeds',
                      'loans': 'loan', 
                      'Loans': 'loan', 
                      'Loan': 'loan',
                      'Misc': 'misc', 
                      'MIsc': 'misc',
                      'misc/education?':'misc',
                      'Pets': 'pets', 
                      'Animals': 'pets',
                      'pets ':'pets',
                      'Bills': 'bills',
                      'bils':'bills',
                      'Medical': 'medical',
                      'Education': 'education'
                      }}, inplace = True)

df.dropna(inplace=True)
# Saving preprocessed Dataset

df.to_csv(r'RDS_processed.csv')

# loading processed dataset
df = pd.read_csv('RDS_processed.csv')

# preprocessing
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

# split dataset into training and testing set
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.10, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

# Model Design

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
# model.add(tf.keras.layers.SpatialDropout1D(0.2))
model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(500, dropout=0.1, recurrent_dropout=0.1)))

# model.add(tf.keras.layers.LSTM(50)) #, dropout=0.2, recurrent_dropout=0.2
model.add(tf.keras.layers.Dense(7, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])


# Training the model
history = model.fit(X_train, Y_train, epochs=epochs, validation_split= 0.10, batch_size=batch_size) 

# Accuracy on Test Set
accr = model.evaluate (X_test,Y_test)
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))

# Accuracy on Train Set
accr = model.evaluate (X_train, Y_train)
print('Train set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))

model.save('init.md5')