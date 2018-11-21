from Elections.election_API_lib import run_generate_tweet_corpus_for_user_list
from Elections.election_lib import top_results_for_doc, top_results_across_corpus
import pandas as pd

DIRECTORY = 'C:/dev/data/twitter_election_integrity/ira_tweets_csv_hashed/ira_tweets_by_userid/'

file_list = [
    f'{DIRECTORY}989d8fcf7bbd11f24f19be3f7aeb7c948ab80de022b2a25d05bf2d5ffe362ac4.csv',
    f'{DIRECTORY}6e2acff4faf83788753943be48d271fb730f906f326837e2c3b8dbdc9107aea5.csv',
    f'{DIRECTORY}1d0631b283947a738df603e051b60c02bdca983db03c95dd0bf5bce597329bd2.csv',
    f'{DIRECTORY}42889f988600ddfe9c3bd28ec5a87338a06018c94b1c2ddf79f25adffe63431f.csv'
]

dictionary, corpus = run_generate_tweet_corpus_for_user_list(file_list)

top_results = top_results_for_doc(corpus[2], dictionary, count_results=10)

words = []
counts = []

for word, count in top_results:
    words.append(word)
    counts.append(count)

top_result_df = pd.DataFrame({'Word': words, 'Count': counts})

print(top_result_df)
