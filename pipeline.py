# scrape post from a group and pass it through the trained model to generate a prediction

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from facebook_scraper import get_posts
import tensorflow as tf
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

group_posts = []
for post in get_posts(group= 1259852177422636, credentials= (), pages=1):
    group_posts.append(post)

my_post = group_posts[2]['text']
model = tf.keras.models.load_model('Model Design/init.md5')

# print(model.summary())
df = pd.read_csv('Model Design/Raabta_dataset - donations.csv')
request = [my_post]

# The maximum number of words to be used. (most frequent)
MAX_NB_WORDS = 50000
# Max number of words in each complaint.
MAX_SEQUENCE_LENGTH = 250
EMBEDDING_DIM = 100
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(df['body'].values)
word_index = tokenizer.word_index


seq = tokenizer.texts_to_sequences(request)
padded = pad_sequences(seq, maxlen = MAX_SEQUENCE_LENGTH)
pred = model.predict(padded)
labels = ['basicneeds', 'loan', 'medical', 'misc', 'bills', 'education',
       'pets']
print("\n\nPost #1", my_post)
print(pred, labels[np.argmax(pred)])