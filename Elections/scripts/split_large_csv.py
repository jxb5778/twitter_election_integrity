import pandas as pd

DIRECTORY = 'C:/dev/data/twitter_election_integrity/ira_tweets_csv_hashed/'

for index, chunk in enumerate(pd.read_csv('{0}{1}'.format(DIRECTORY, 'ira_tweets_csv_hashed.csv'), chunksize=500000)):
    print(chunk.head())
    chunk.to_csv('{0}{1}_{2}.csv'.format(DIRECTORY, 'ira_tweets/tweets', index), index=False)
