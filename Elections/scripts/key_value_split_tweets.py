from Elections.election_API_lib import run_key_value_split

run_key_value_split(
    source_dir= 'C:/dev/data/twitter_election_integrity/ira_tweets_csv_hashed/ira_tweets_csv_chunked/',
    dest_dir= 'C:/dev/data/twitter_election_integrity/ira_tweets_csv_hashed/ira_tweets_by_userid/',
    key_value= 'userid'
)

