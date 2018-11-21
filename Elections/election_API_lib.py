from Elections.election_lib import *


def run_key_value_split(source_dir, dest_dir, key_value):
    return key_value_split(source_dir, dest_dir, key_value)


def run_generate_tweet_bow_from_file(tweet_file):

    df = pd.read_csv(tweet_file)

    tweet_bow = generate_tweet_bow(df)

    return tweet_bow


def run_generate_tweet_corpus_from_file_list(file_list):

    return generate_corpus_from_file_list(file_list)


def run_generate_tweet_corpus_for_user(filename):
    df = pd.read_csv(filename)
    return generate_corpus_for_user(df)


def run_generate_tweet_corpus_for_user_list(file_list):

    buff = Buffer()
    buff.value = []

    for file in file_list:
        buff.value.append(pd.read_csv(file))

    buff.value = pd.concat(buff.value)

    return generate_corpus_for_user(buff.value)
