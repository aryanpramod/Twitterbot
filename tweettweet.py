import tweepy
import time


auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

user = api.me()
print (user.name) 
print (user.screen_name)
print (user.followers_count)

search = "python"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(200)

for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Username':
    print(follower.name)
    follower.follow()


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break