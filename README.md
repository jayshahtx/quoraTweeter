#QuoraTweeter 

quoraTweeter is a collection of Python scripts which help you scrape, parse, and tweet a user's Quora activity to Twitter.

##Functionality

After configuring all APIs, a specified Twitter account will autonomously post tweets in the following format:

<tt> &lsaquo;Quora Question Text&rsaquo; &lsaquo;Hash Tag from Quora Categories&rsaquo; &lsaquo;Bitly URL to Quora Question&rsaquo; </tt>

The scripts parse a user's page daily and find new questions that have not yet been posted to Twitter. Using Bitly's API, the scripts also enable tracking click through rates of each tweet/link.

##Dependencies


