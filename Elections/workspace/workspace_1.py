from Elections.election_API_lib import generate_tweet_bow

DIRECTORY = 'C:/dev/data/twitter_election_integrity/Search/'

bow_simple = generate_tweet_bow(f'{DIRECTORY}retweet_each_other.csv')

# Print the 10 most common tokens
print(bow_simple.most_common(20))
