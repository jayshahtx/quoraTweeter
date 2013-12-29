from quoraBrowser import quoraBrowser
from quoraParser import quoraParser
from questionHistory import questionHistory
from bitlyLinks import bitlyLinks
from quoraTweeter import quoraTweeter
from datetime import datetime as dt
import time
import pickle 


'''This is the main driver for the scraper, 
	runs once a day to update the Twitter account'''

#This is the URL for your Quora page
URL = "[Your Quora profile's URL]"

#Bitly username and API key
bUser = '[Your Bitly account username[]]'
bAPI = '[Your Bitly account API key]'

#Twitter Oauth token, Oauth secret, consumer key, and consumer secret
Oauth_token = '[Your Twitter OAuth Token]'
Oauth_secret = '[Your Twitter Secret Token]'
consumer_key = '[Your Twitter Consumer Key'
consumer_secret = '[Your Twitter Consumer Secret'

#Number of hours across which to schedule tweetes
tweetHours = 8
maxDailyTweets = 8

def runDaily():

	#Instantiate a quoraBrowser object
	visitor = quoraBrowser(URL)

	#Retrieve the source code
	source = visitor.getSource()

	#Find all questions
	parser = quoraParser(source)

	#Create lists of all questions and categories from source
	allQuestions = parser.findQuestions()

	#Select only the questions which are new
	newQuestionFinder = questionHistory(allQuestions,maxDailyTweets)
	newQuestions = newQuestionFinder.getNewQuestions()

	#Set up Bitly Links, takes in username and API key as arguments
	linky = bitlyLinks(bUser,bAPI)
	newQuestions = linky.shortenAll(newQuestions)

	#Access twitter
	t = quoraTweeter(Oauth_token,Oauth_secret,consumer_key,consumer_secret)
	t.scheduleTweets(newQuestions,tweetHours)

#Run the script once a day between 8 and 10 AM
while True:
	if dt.now().hour in range(8,10):
		print "Running script for today at " + str(dt.now())
		runDaily()
		print "---------------------------------------------"
		print
		#wait 12 hours to check if its time
		time.sleep(3600*12)
	#If it's not time, wait another hour and check again
	else:
		time.sleep(3600)

