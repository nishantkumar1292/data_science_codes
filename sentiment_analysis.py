import tweepy
from textblob import TextBlob
import sys

consumer_key = 'ewiauWV6ezigxwtP5Dt51bkSm'
consumer_secret = '6zVCLZEjlIf3W8WNaljuE7o5Tcq14KKX1VnHTaLG7VkBk1KG8g'

access_token = '286648158-Mok7WE4uvROkcUGkdmOurdiYJhQ7GO3qCbYzUghf'
access_token_secret = 'gTQwPuRGEeQ1Km6ULaNJigSkixIMNmLeVa59hgQlScMBe'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Dhoni')

print(sys.stdout.encoding)
print('\n-------------------\n')

for tweet in public_tweets:
	print(tweet.text.encode(sys.stdout.encoding, errors='replace'))
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print('\n-------------------\n')
