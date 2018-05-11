import tweepy
import csv
from textblob import TextBlob

consumer_key="Ax7Vmc6OUDfeYg2rIO4bwheTM"
consumer_secret="QFlpYxceHm2pkI6rykBsIP4sT3jdwmqiRYdLYBhhlv2KQHGkSc"
token="182812117-hrF4HMDkkKGYf9nD9HoI5nzU0Zaynce3ZVBzfoxq"
token_secret="4naahpGFQydJYVvAMaVkfq5ojdpg8gOkWhddNvvUiAcYa"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)

api = tweepy.API(auth)

public_tweets = api.search('love')

with open("csvfile.csv", "w") as file:
    writer = csv.writer(file)
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        sentiment = 'positive' if analysis.sentiment.polarity > 0 else 'negative'
        writer.writerow([tweet.text, sentiment])