from Elections.election_API_lib import run_generate_tweet_corpus_from_file_list
from Elections.election_lib import *


DIRECTORY = 'C:/dev/data/twitter_election_integrity/ira_tweets_csv_hashed/ira_tweets_by_userid/'

file_list = [
    f'{DIRECTORY}1632f91e0f4babb60c389a9771e4f654a908c6426ea991058034df340490f27b.csv',
    f'{DIRECTORY}721aa2b2e71abb90376266778b217c7b6a04ab1a46902dd1faf3fd8f9d960c41.csv',
    f'{DIRECTORY}0c0ff15cd51357a516a60b05c14f74282a4cea55cc89ef3d35900c64a5f1ad1c.csv',
    f'{DIRECTORY}17516dfc0b243ce62b79a6de311af239f5c448b65ed113305616d74350c7cb66.csv',
]

dictionary, corpus = run_generate_tweet_corpus_from_file_list(file_list)

print(top_results_across_corpus(dictionary, corpus, count_results=10))

print(top_results_for_doc(doc=corpus[3], dictionary=dictionary, count_results=5))
