from Elections.election_API_lib import run_generate_tweet_corpus
from collections import defaultdict
import itertools

DIRECTORY = 'C:/dev/data/twitter_election_integrity/ira_tweets_csv_hashed/ira_tweets_by_userid/'

file_list = [
    f'{DIRECTORY}1632f91e0f4babb60c389a9771e4f654a908c6426ea991058034df340490f27b.csv',
    f'{DIRECTORY}721aa2b2e71abb90376266778b217c7b6a04ab1a46902dd1faf3fd8f9d960c41.csv',
    f'{DIRECTORY}0c0ff15cd51357a516a60b05c14f74282a4cea55cc89ef3d35900c64a5f1ad1c.csv',
    f'{DIRECTORY}17516dfc0b243ce62b79a6de311af239f5c448b65ed113305616d74350c7cb66.csv',
]

dictionary, corpus = run_generate_tweet_corpus(file_list)
'''
doc = corpus[2]

# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:5]:
    print(dictionary.get(word_id), word_count)
'''
# Create the defaultdict: total_word_count
total_word_count = defaultdict(int)
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count

# Create a sorted list from the defaultdict: sorted_word_count
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True)

# Print the top 5 words across all documents alongside the count
for key, value in sorted_word_count[:10]:
    print(dictionary.get(key), value)