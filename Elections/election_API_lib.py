from Elections.election_lib import *


def run_key_value_split(source_dir, dest_dir, key_value):
    key_value_split(source_dir, dest_dir, key_value)
    return


def generate_tweet_bow(tweet_file):

    df = pd.read_csv(tweet_file)

    tokens = tokenize_tweets(df)
    processed_tokens = preprocess_tweet_tokens(tokens)

    return Counter(processed_tokens)
