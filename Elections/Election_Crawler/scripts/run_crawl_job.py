from Elections.Election_Crawler.elections_crawler_lib import *
from Crawler.crawler_API_lib import *
from Crawler.crawler_lib import *

# result_filename needs to be provided to provide query results

if __name__ == '__main__':

    run_crawl_job(
        input_files=files_from_directory('C:/dev/data/twitter_election_integrity/ira_tweets_csv_hashed/ira_tweets_parquet/'),
        apply_func=crawler_parquet_query_from_file,
        apply_func_args={
            'query': 'retweet_userid in @value_list',
            'value_list_file': 'C:/dev/data/twitter_election_integrity/Search/userids.csv',
            'value_column': 'UserIDs'
        },
        result_filename='C:/dev/data/twitter_election_integrity/Search/retweet_each_other.csv',
        count_processes=2
    )
