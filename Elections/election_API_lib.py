from Elections.election_lib import *


def run_key_value_split(source_dir, dest_dir, key_value):
    return key_value_split(source_dir, dest_dir, key_value)


def run_generate_tweet_bow(tweet_file):

    df = pd.read_csv(tweet_file)

    tweet_bow = generate_tweet_bow(df)

    return tweet_bow


def run_generate_tweet_corpus(file_list):

    return generate_corpus(file_list)
