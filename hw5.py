import unittest
import tweepy
import requests
import json

## SI 206 - W17 - HW5
## COMMENT WITH:
## Your section day/time: Thursday 3-4pm
## Any names of people you worked with on this assignment:

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets about "rock climbing", when we run your code, the code should use CACHED data, and should not need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.

## The lecture notes and exercises from this week will be very helpful for this. 
## Because it is dependent on user input, there are no unit tests for this -- we will run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
consumer_key = "O8jQO7fbS71DN9OaL1vJ0QTOB" 
consumer_secret = "TFKwkPLHjLDU2WnOA5d0slhc4PzyJypACQ8yuf48c5owotdXBb"
access_token = "832292756273917953-bN7YYLLlSABTiFHoEkSqZjRDh6TUiRK"
access_token_secret = "EUejQduR5wn1Ey8QNK9VTI3miX3tCB9KmB6uybbDJZjXL"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except statement shown in class.
## 2. Write a function to get twitter data that works with the caching pattern, so it either gets new data or caches data, depending upon what the input to search for is. You can model this off the class exercise from Tuesday.
## 3. Invoke your function, save the return value in a variable, and explore the data you got back!
## 4. With what you learn from the data -- e.g. how exactly to find the text of each tweet in the big nested structure -- write code to print out content from 3 tweets, as shown above.

twitter_cache_data = 'twitter_info.json'

try:
	twitter_cache_file = open(twitter_cache_data, 'r')
	twitter_cache_contents = twitter_cache_file.read()
	twitter_cache_diction = json.loads(twitter_cache_contents)

except:
	twitter_cache_diction = {}
	
search_guy = input("Enter something you want to search for on Twitter: ")


def twitter_data(search_guy):
	user_search = search_guy
	
	if user_search in twitter_cache_diction:
		results = twitter_cache_diction[user_search]
		

	
	else:
		results = api.search(q = search_guy)
		twitter_cache_diction[user_search] = results
		new_data = open(twitter_cache_data, 'w')
		new_data.write(json.dumps(twitter_cache_diction))
		new_data.close
		
	list_of_tweets = results['statuses']

	return list_of_tweets

for items in twitter_data(search_guy)[0:3]:
	print(items['text'])
	print(items['created_at'])
	print("\n")









