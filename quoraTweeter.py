import time
from twitter import *

class quoraTweeter():

	#initialize twitter connection
	def __init__(self,a,b,c,d):
		self.t = Twitter(auth=OAuth(a,b,c,d))

	#method which shortens a question to fit 140 char limit	
	def shortenTweet(self,tweet):

		#Text of actual question ctual question
		text = tweet[1] + " "
		
		#Check if category is too long/same as question, these words will be hashtags
		if (tweet[1] == tweet[0] or len(tweet[0]) > 100):
			category = ""
		else:
			category = "#" + tweet[0].replace(" ", " #")
			category = category.replace("#and","")

		#Actual link to the question
		link = " " + tweet[2]

		#String manipulation to ensure tweet is < 140 cahrs
		textSize = len(text)
		catSize = len(category)
		linkSize = len(link)

		fixSize = catSize + linkSize + 2
		maxText = 140 - fixSize 

		#is the tweet going to be too long? If so, shorten the question
		if (textSize > maxText):
			reduction = textSize - maxText + 4
			newText = tweet[1][:(len(tweet[1])-reduction)] + "... "
			tweet = newText + category + link
			
		else:
			tweet = text + category + link

		if (len(tweet) > 140):
			raise Exception("Tweet is longer than 140 chars")
		else:
			return tweet


		

	def scheduleTweets(self,allTweets,hours):
		finalTweets = []

		#Shorten tweets and add to queue
		for t in allTweets:
			try: 
				completed = self.shortenTweet(t)
				finalTweets.append(completed)
			except Exception as e:
				print "Unexpected error: " + str(e) + ", cannot tweet this question, skipping..."

		#Duation of period to submit tweets
		totalTweetTime = hours*3600

		#Number of seconds in between each tweet
		timePerTweet = totalTweetTime/len(finalTweets)
		
		for item in finalTweets:
			try: 
				self.t.statuses.update(status=item)
				print "Tweeted: " + item
				print
				time.sleep(timePerTweet)
			except Exception as e:
				print "Unexpected error occur posting this to twitter, " + str(e) + ", skipping..."
			
			


