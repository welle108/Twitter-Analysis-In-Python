# sentiment.py
# Collects 2 search terms and compares their sentiment scores
# Author: Scott Weller
# Email: welle108@mail.chapman.edu
# Course: CPSC 353
# Assignment: PA01 Sentiment Analysis
# Date: October 9, 2018


print ""
print("------------------------------------------------------")
print("Ye Olde Twitter Analysis Script")
print("------------------------------------------------------")
print ""
import twitter
import json

# Authorize API and create API object
CONSUMER_KEY = 'oyxCsTsNvNUA3DQwY4Mpenaby'
CONSUMER_SECRET = 'bx2QC7jW83XTTwdIntilELb2KJzmXKWottNxT7XBSlzmvTdGWR'
OAUTH_TOKEN = '1047526902682906624-C5zZ8eGcGn5yd5jdZTs0nXsGyFqqRA'
OAUTH_TOKEN_SECRET = 'oX9kDoQ5xzm1cyuovqawC4whuV52C0ouh8Ojc7cd9uMcG'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Assign variables for each term
term1 = raw_input('Enter a search term: ')
term2 = raw_input('Enter second search term: ')
count = 1000

# Define collections of statuses
search_results1 = twitter_api.search.tweets(q=term1, count=count)
search_results2 = twitter_api.search.tweets(q=term2, count=count)

statuses1 = search_results1['statuses']
statuses2 = search_results2['statuses']

status_texts1 = [status['text'] for status in statuses1]
status_texts2 = [status['text'] for status in statuses2]

# Collections of words in each tweet

words1 = [w for t in status_texts1 for w in t.split()]
words2 = [w for t in status_texts2 for w in t.split()]

print "---------------------------------------------------------------------"
print 'Sentiment Analysis'
print "---------------------------------------------------------------------"
sent_file = open('AFINN-111.txt')

scores1 = {}  # initialize an empty dictionary
scores2 = {}
for line in sent_file:
    term, score = line.split("\t")
    # The file is tab-delimited.
    # "\t" means "tab character"
    scores1[term] = int(score)  # Convert the score to an integer.
    scores2[term] = int(score)

score1 = 0
score2 = 0
for word in words1:
    uword = word.encode('utf-8')
    if uword in scores1.keys():
        score1 = score1 + scores1[word]

for word in words2:
    uword = word.encode('utf-8')
    if uword in scores2.keys():
        score2 = score2 + scores2[word]

# Compare scores and print
print "First term score"
print float(score1)
print "Second term score"
print float(score2)
if score1>score2:
   print("'"+term1+"'"+" is currently more highly favored than "+"'"+term2+"'")
elif score1<score2:
   print("'"+term2+"'"+" is currently more highly favored than "+"'"+term1+"'")
elif score1 == score2:
   print("Both terms have the same sentiment score")

