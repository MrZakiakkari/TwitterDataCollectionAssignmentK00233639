#!/usr/bin/env python
# coding: utf-8

# # Twitter Data Collection Assignment

# ## Setup

# Assessment 1: Collecting Data
# 
# 
# This assessment is a practical assessment that evaluates your understanding of metrics and value, and your ability to use Python and its libraries to locate and extract data.  In this assessment you will be extracting data using an API.  The API to be used is the Twitter API.    You are to assume the role of a data analyst for a software company that has made a software product, such as Discord, Wordle, or Tinder for example. 
# You will first identify what metric the Twitter stream will be used for, and describe the data.  
# You will then write a python program that collects data from across multiple twitter accounts (in class we looked at one account that of a named Twitter account, in this example you will have to extend your code to look at the tweet database from a keyword perspective).  The tweets collected should be about one software or consumer product that your company has made.
# 
# 
# Weighting
# 
# This assessment is worth 25% of your final grade.
# 
# Deliverable
# 
# You are to submit three files:-
# 
# (1) A word/pdf document answering questions 1, 2 and the screen shot from Q3.
# 
# (2) a labelled .py python program file, using extensive use of comments.  Clearly indicate where code has been used from other sources.
# 
# (3) a one page print screen or preview of sample data/output collected in (2) above
# 
# 
# 
# Question 1
# 
# What metric would you use this data for?  In your answer name the metric, and explain the value it will bring.
# 
# Question 2
# 
# Document the meta-data for this metric, i.e. data source, data type, volume, velocity, variety, ethical or legislative considerations.
# 
# Question 3
# 
# You are to write a python program to extract data from Twitter.
# 
# The key attributes of the tweets (at the time of writing - this may change - check online for up to date attributes or better still check your dataset collected) pulled out are :
# 
# text: the text of the tweet itself
# created_at: the date of creation
# favorite_count, retweet_count: the number of favourites and retweets
# favorited, retweeted: boolean stating whether the authenticated user (you) have favourited or retweeted this tweet
# lang: acronym for the language (e.g. “en” for english)
# id: the tweet identifier
# place, coordinates, geo: geo-location information if available
# user: the author’s full profile
# entities: list of entities like URLs, @-mentions, hashtags and symbols
# in_reply_to_user_id: user identifier if the tweet is a reply to a specific user
# in_reply_to_status_id: status identifier id the tweet is a reply to a specific status
# In this extraction, we are interested in the favorite_count and retweet_count.  Pull off all tweets, sort by favorite_count and retweet_count, and print/output to screen the tweet text and the counts of the top 10 favourited tweets.
# 
# There is a lot of help online, for example https://fcpython.com/blog/scraping-twitter-tweepy-python. ;
# 
# Note: it is assumed that you will use code shared openly online, in tutorials and on GitHub.  You may use this code, however at least 25% of the program must be your own code.  Clearly distinguish your code from that found online.  You should properly attribute the copyright to its author.   You must not copy code from your classmates.  You should fully understand all code submitted, and be able to explain each line of code.
# 
# Sources: https://github.com/markcrowe-com/data-analytics-project-template/blob/master/notebooks/notebook-1-02-dc-twitter-api.ipynb , https://github.com/mehranshakarami/AI_Spectrum/blob/main/2021/Twitter_API/twitter_api.py ,  https://realpython.com/pandas-sort-python/

# Local
#!pip install -r requirements.txt
# Remote option
#!pip install -r https://raw.githubusercontent.com/mrzakiakkari/reposiroty-name/requirements.txt
#Options: --quiet --user


from configparser import ConfigParser
from pandas import DataFrame
import tweepy
# packages needed for the project


config_filepath = "config.ini"
config_parser = ConfigParser()


config_parser.read(config_filepath)


access_token = config_parser["Twitter"]["AccessToken"]
access_token_secret = config_parser["Twitter"]["AccessTokenSecret"]
consumer_key = config_parser["Twitter"]["ApiKey"]
consumer_secret = config_parser["Twitter"]["ApiKeySecret"]


o_auth_handler = tweepy.OAuthHandler(consumer_key, consumer_secret)
o_auth_handler.set_access_token(access_token, access_token_secret)
tweepy_api = tweepy.API(o_auth_handler, wait_on_rate_limit=True)
# authenticate with Tweepy (the twitter API) using 'ApiKey', 'ApiKeySecret', 'AccessToken' and 'AccessTokenSecret' from the config.ini file.


screen_name = "Discord"


tweets = tweepy_api.user_timeline(
    screen_name=screen_name,
    count=200,  # 200 is the maximum allowed count
    include_rts=False,
    tweet_mode="extended"
)  # Necessary to keep full_text otherwise only the first 140 words are extracted

#tweets needed tp get other users data.


for info in tweets[:3]:
    print("ID: {}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")
#to extract the tweets from the screen_name and print the first 3 tweets./For testing purposes.


len(tweets)
#to get the number of tweets/to double check on the tweets collected


all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id


screen_names = ["discord", "tinder","playstation", "Fiserv","Nintendo","HP","Intel","AMD","NVIDIA","Microsoft","Apple","Google","Dell","Cisco", "Meta"]
#to get the screen names of the users

for screen_name in screen_names:
    while True:
        tweets = tweepy_api.user_timeline(
            screen_name=screen_name,
            count=200,# 200 is the maximum allowed count
            include_rts=False,
            max_id=oldest_id - 1,
            # Necessary to keep full_text
            # otherwise only the first 140 words are extracted
            tweet_mode='extended')
        if len(tweets) == 0:
            break
        oldest_id = tweets[-1].id
        all_tweets.extend(tweets)
        print(f'{len(tweets)} of tweets downloaded till now {len(all_tweets)}')
#to get the tweets of the users


#to get the screen names of the users

for screen_name in screen_names:
    while True:
        tweets = tweepy_api.user_timeline(
            screen_name=screen_name,
            count=200,# 200 is the maximum allowed count
            include_rts=False,
            max_id=oldest_id - 1,
            # Necessary to keep full_text
            # otherwise only the first 140 words are extracted
            tweet_mode='extended')
        if len(tweets) == 0:
            break
        oldest_id = tweets[-1].id
        all_tweets.extend(tweets)
        print(f'{len(tweets)} of tweets downloaded till now {len(all_tweets)}')
#to get the tweets of the users


tweets_list: list = [[
    tweet.id_str, 
    tweet.user.screen_name, 
    tweet.created_at,
    tweet.favorited,
    tweet.retweeted,
    tweet.lang,
    tweet.place,
    tweet.coordinates, 
    tweet.geo,
    tweet.user,
    tweet.entities,
    tweet.in_reply_to_user_id,
    tweet.in_reply_to_status_id,
    tweet.favorite_count, 
    tweet.retweet_count,
    tweet.full_text.encode("utf-8").decode("utf-8")
] for _, tweet in enumerate(all_tweets)]


tweet_columns: list = [
    "id", "screen_name", "created_at", "favourited", "retweeted", "language",
    "place", "coordinates", "geo", "user", "entities", "user identifier",
    "status identifier", "favorite_count", "retweet_count", "text"
]
dataframe: DataFrame = DataFrame(tweets_list, columns=tweet_columns)
dataframe.to_csv('./assets/twitter-data.csv', index=False)
dataframe.head(3)
#to get the dataframe of the tweets


dataframe


dataframe=dataframe[["text", "favorite_count", "retweet_count"]]


dataframe.sort_values(
    by=["text", "favorite_count", "retweet_count"],
    ascending=[False, True, True])[["text", "favorite_count"]].head(10)
#to get the top 10 of the most favourited tweets and sort them by the text and the favourite count and retweet count




