from selenium import webdriver

driver = webdriver.Firefox()
print "Launching Jay's Quora Page"
driver.get('http://www.quora.com/Jay-Shah-1?share=1')

print "Populating page by scrolling down"
#scroll down a few times to make sure we are looking at all of Jay's most recent content
for i in range(0,5):
	print "Number of scrolls %s", i
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

html_source = driver.page_source
html_source = html_source.encode("ascii","ignore")
print html_source 

# driver.close()