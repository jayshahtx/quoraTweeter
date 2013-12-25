from BeautifulSoup import BeautifulSoup

#Class which parses Quora source using BeautifulSoup and returns list of lists, each object in lists contains, category of question, question, and URL suffix to question

class quoraParser():
	def __init__(self,data):
		#save the source code as a variable
		self.source = data + ""

	def findQuestions(self):
		#Store category, text, and links in this array list
		allText = []

		#instantiate a BS object
		soup = BeautifulSoup(self.source)

		#find all the questions and their respective categories and URLs
		questions = soup.findAll(attrs = {"class":"question_link"})
		for q in questions:

			#Store the category, text, and link for each Quora question in this array list
			tweetText = []

			#find the category
			category = q.find(text=True, attrs = {"class":"question_context"})
			tweetText.append(category)

			#find actual question, it is always the last strip of text in a table - this is a hack and could break if the formatting of Quora changes
			question = q.findAll(text=True, attrs = {"class":"link_text"})
			size = len(question)
			tweetText.append(question[size-1])

			#find the link to post
			link = q['href']
			tweetText.append(link)

			#add all content for this tweet into the list of all tweet content
			allText.append(tweetText)

		return allText