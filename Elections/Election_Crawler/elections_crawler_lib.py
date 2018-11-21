from Crawler.crawler_lib import *
from googletrans import Translator
import pandas as pd
import time
import os


def crawler_translate_tweet_text(file, crawler, dest_dir):

    print(file)

    crawler.reader = pd.read_csv(file)

    translated_tweets = []
    translation_confidence = []

    for tweet in crawler.reader['tweet_text']:
        trans = Translator()

        translation = trans.translate(tweet)

        print(translation.text)

        translated_tweets.append(translation.text)
        translation_confidence.append(translation.extra_data['confidence'])

        time.sleep(1)

    crawler.reader['translated_tweet_text'] = translated_tweets
    crawler.reader['translation_confidence'] = translation_confidence

    dest_file = '{}{}'.format(dest_dir, os.path.basename(file))

    crawler.reader.to_csv(dest_file, index=False)

    return


def crawler_parquet_query_from_file(file, crawler, query, value_list_file='', value_column=''):
    """ Crawler job that reads in parquet files and aggregates query results

    :param file: string file path/ filename that is being operated on
    :param crawler: Crawler object, attributes used-
                reader: DataFrame of the current file read into memory
                query_return: list of DataFrames holding query results
    :param pandas_query: string that follows pandas query syntax
    :param value_list_file: string filename for csv to be read into @crawler.filter,
                            and will be used to query against the data
    :param value_column: string for the column name of the data you want read from the file
    :return: None
    """

    print(file)

    crawler.reader = pd.read_parquet(file, engine='pyarrow')

    if crawler.filter is None:
        crawler.filter = pd.read_csv(value_list_file)[value_column]

    pandas_query(crawler=crawler, query=query, value_list=crawler.filter)

    return
