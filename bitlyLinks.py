import bitly_api

#Class which takes in list of new questions and returns with modified links

class bitlyLinks():
	def __init__(self,user,APIkey):
		self.api = bitly_api.Connection(user,APIkey)
	
	def shortenAll(self,newQuestionList):
		for q in newQuestionList:
			suffix = q[2]
			fullLink = "http://quora.com" + suffix + "?share=1"
			data =  self.api.shorten(fullLink)
			q[2] = data['url']
		return newQuestionList
