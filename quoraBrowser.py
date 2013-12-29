from selenium import webdriver

#Class which accesses user's Quora page to find its source - navigation is handled by Selenium
#Returns string with source formatting
class quoraBrowser():
	def __init__(self,URL):

		#Append "?share=1" to the end of URL to bypass login popup
		self.pageURL = URL + "?share=1"

	def getSource(self):
		#Launch Firefox Driver
		driver = webdriver.Firefox()
		print "Launching User's Quora Page"
		
		#Acess webpage and scroll down to generate most recent content
		driver.get(self.pageURL)
		print "Populating page by scrolling down"
		
		for i in range(0,4):
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

		#Get page source code
		html_source = driver.page_source
		html_source = html_source.encode("ascii","ignore")
		driver.close()	
		return html_source 

