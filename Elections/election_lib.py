from Crawler.crawler_API_lib import files_from_directory
from Crawler.buffer import Buffer

from collections import defaultdict
import itertools

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#nltk.download('punkt')

from collections import Counter
from polyglot.text import Text, Word
#from polyglot.downloader import downloader
#downloader.download(["sentiment2.nl"])

from gensim.corpora.dictionary import Dictionary
from dateutil.parser import parse
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

    for tweet in df['tweet_text']:
        combine_tweets = '{}\n{}'.format(combine_tweets, tweet)

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


def generate_tweet_bow(df):

    tokens = tokenize_tweets(df)
    processed_tokens = preprocess_tweet_tokens(tokens)

    return Dictionary([processed_tokens])


def generate_corpus_from_file_list(file_list):

    token_list_master = []

    for filename in file_list:
        print(filename)
        df = pd.read_csv(filename)
        file_tokens = tokenize_tweets(df)
        processed_tokens = preprocess_tweet_tokens(file_tokens)
        token_list_master.append(processed_tokens)

    dictionary = Dictionary(token_list_master)
    corpus = [dictionary.doc2bow(token_list) for token_list in token_list_master]

    return (dictionary, corpus)


def generate_corpus_for_user(df):
    token_list_master = []

    df['tweet_year'] = [parse(tweet_time).year for tweet_time in df['tweet_time']]

    for year in np.unique(df['tweet_year']):
        file_tokens = tokenize_tweets(df.query('tweet_year == @year'))
        processed_tokens = preprocess_tweet_tokens(file_tokens)
        token_list_master.append(processed_tokens)

    dictionary = Dictionary(token_list_master)
    corpus = [dictionary.doc2bow(token_list) for token_list in token_list_master]

    return dictionary, corpus


def top_results_across_corpus(dictionary, corpus, count_results=10):
    # Create the defaultdict: total_word_count
    total_word_count = defaultdict(int)
    for word_id, word_count in itertools.chain.from_iterable(corpus):
        total_word_count[word_id] += word_count

    # Create a sorted list from the defaultdict: sorted_word_count
    sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True)

    # Identify the top N words across all documents alongside the count
    top_results = [(dictionary.get(key), value) for key, value in sorted_word_count[:count_results]]

    return top_results


def top_results_for_doc(doc, dictionary, count_results):

    # Sort the doc for frequency: bow_doc
    bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

    # Identify the top 5 words of the document alongside the count
    top_results = [(dictionary.get(key), value) for key, value in bow_doc[:count_results]]

    return top_results
