#QuoraTweeter 
quoraTweeter is a collection of Python scripts which help you scrape, parse, and tweet a user's Quora activity to Twitter. For a sample output, visit http://twitter.com/quoragems

##Functionality
After configuring all APIs, a specified Twitter account will autonomously post tweets in the following format:

<tt> &lsaquo;Quora Question Text&rsaquo; &lsaquo;Hash Tag from Quora Categories&rsaquo; &lsaquo;Bitly URL to Quora Question&rsaquo; </tt>
The scripts parse a user's page daily and find new questions that have not yet been posted to Twitter. Using Bitly's API, the scripts also enable tracking click through rates of each tweet/link.

##Non-Standard Dependencies
* selenium
* beautifulsoup
* bitly_api
* twitter (note: this is not python-twitter) 

##Getting Started
1. Install all dependencies 
2. Register for a bitly account and get API key
3. Create Twitter handle and register an application with <b> read and write</b> permissions
4. Create (or find) a user profile on Quora
5. Update global variables in driver.py and run it





