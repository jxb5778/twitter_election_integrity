from Crawler.crawler_API_lib import files_from_directory
from Crawler.buffer import Buffer

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#nltk.download('punkt')

from collections import Counter
from polyglot.text import Text, Word
#from polyglot.downloader import downloader
#downloader.download(["sentiment2.nl"])
import pandas as pd
import numpy as np
import os


def key_value_split(source_dir, dest_dir, key_value):
    reader = Buffer()
    filter = Buffer()

    print("Starting transformation")

    for file in files_from_directory(source_dir):
        print(file)
        reader.value = pd.read_csv(file)
        for key in np.unique(reader.value[key_value]):
            filter.value = reader.value.query('{} == @key'.format(key_value))

            dest_file = '{}{}.csv'.format(dest_dir, key)

            if os.path.isfile(dest_file):
                filter.value = pd.concat([filter.value, pd.read_csv(dest_file)])
                filter.value.to_csv(dest_file, index=False)
            else:
                filter.value.to_csv(dest_file, index=False)

    print("Finished transformation!")

    return


def tokenize_tweets(df):
    combine_tweets = ''

    for index in range(1000):
        tweet_text = df.iloc[index]['tweet_text']
        combine_tweets = '{}\n{}'.format(combine_tweets, tweet_text)

    return word_tokenize(combine_tweets)


def preprocess_tweet_tokens(tokens):

    token_buff = Buffer()

    # Lowercase tokens
    token_buff.value = [t.lower() for t in tokens]

    # Alpha only tokens
    token_buff.value = [t for t in token_buff.value if t.isalpha()]

    # Remove Russian Stopwords
    token_buff.value = [t for t in token_buff.value if t not in stopwords.words('russian')]

    # Remove English Stopwords
    token_buff.value = [t for t in token_buff.value if t not in stopwords.words('english')]

    # Remove Retweet, http, and https
    token_buff.value = [t for t in token_buff.value if t not in ['rt', 'http', 'https']]

    wordnet_lemmatizer = WordNetLemmatizer()
    token_buff.value = [wordnet_lemmatizer.lemmatize(t) for t in token_buff.value]

    # Remove tokens that are length 1
    token_buff.value = [t for t in token_buff.value if len(t) > 1]


    return token_buff.value
