from quoraBrowser import quoraBrowser
from quoraParser import quoraParser
from questionHistory import questionHistory
import pickle 

#This is the main driver for the scraper, run it once a day to update the Twitter accound

#Visit your own profile on Quora and enter its URL below:
# URL = "http://www.quora.com/Jay-Shah-1"

# #Instantiate a quoraBrowser object
# visitor = quoraBrowser(URL)

# #Retrieve the source code
# source = visitor.getSource()

#Find all questions 

#TEST METHOD, USE WHEN YOU DO NOT WANT TO WAIT FOR FIREFOX DRIVER
with open ("sampleSource.txt") as myfile:
	source=myfile.read().replace('\n','')

#Find all questions
parser = quoraParser(source)

#Create lists of all questions and categories from source
allQuestions = parser.findQuestions()

#Find only the questions which are new
newQuestionFinder = questionHistory(allQuestions)
newQuestions = newQuestionFinder.getNewQuestions()

print str(newQuestions)




