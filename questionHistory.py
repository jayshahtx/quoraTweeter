import pickle
import os

#check if a dictionary exists, create new one if does not exist
class questionHistory():
	def __init__(self,questionList,m):
		#First check if dictionary is already in file
		self.todaysQuestions = questionList
		self.maxQuestions = m

	#Returns list of questions that have not been seen before	
	def getNewQuestions(self):
		if os.path.isfile("history.p"):
			print "Dictionary found"
			history = pickle.load(open("history.p","rb"))
		else:
			history = {}
			pickle.dump(history,open("history.p","wb"))
			print "Dictionary not found, created new one and saved to file"

		#list of new questions
		newQList = []
		for question in self.todaysQuestions:
			concat = question[0]+question[1]

			#Check if this is a new question
			if (concat in history)==False:
				newQList.append(question)
				history[concat] = True

			if len(newQList) > self.maxQuestions:
				break

		#Write new dictionary back to file and return list of new questions
		pickle.dump(history,open("history.p","wb"))
		return newQList



