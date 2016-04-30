import json
#
# This JSON file contains the text of tweets of several tweeples
#
tweets_file = open('./data/tweets.json', 'r')
#
# The tweets were pulled through a separate script, like this:
#
#import json
#from twitter import TwitterStream, OAuth, Twitter
#
#CONSUMER_KEY = 'your_key_here'
#CONSUMER_SECRET = 'your_key_secret_here'
#ACCESS_TOKEN = 'your_token_here'
#ACCESS_SECRET = 'your_token_secret_here'
#
#oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
#
# scenario 1
#t = Twitter(auth=oauth) # if I am looking at timelines
#iterator = t.statuses.user_timeline(screen_name="GoogleTrends") # any handle's tweets
#iterator = t.statuses.home_timeline() # my own tweets
#
# scenario 2
#twitter_stream = TwitterStream(auth=oauth) # if I am looking at streams
#iterator = twitter_stream.statuses.sample() # live tweets at any given point of time
#
#i = 50 # just so that a small number of tweets is presented
#
#tweetsfull = open("./static/tweets.json", "w")
#
#for tweet in iterator:
#    tweet_raw = json.dumps(tweet)
#    print >> tweetsfull, tweet_raw # the entire tweet is written to a file, for use later
#    tweet_text = json.loads(tweet_raw.strip())
#    if 'text' in tweet_text:
#        print tweet['text'].encode('utf-8')  # only the text of the tweet is displayed on the console
#    i -= 1
#    if i == 0:
#        break
#
#tweetsfull.close()
#
#######################
#
# Now to clean up the text of words such as "RT",
# phrases such as "https://", and
# punctuation marks
#
end_strip = [".", ",", "?", "/", "!", "*", ":", ")", "'", '"']
start_strip = [":", "*", "(", "'", '"']

words = [] # a list to contain all the words in all the tweets

for line in tweets_file:
    tweet = json.loads(line)
    print tweet
    if 'text' in tweet: # because if tweets from stream, even stuff such as deletions are returned
        tweet_text = tweet['text'] # I am looking only at "real" tweets, i.e. those with text
        #print tweet
        for word in tweet_text.split():
            word = word.lower()
            if word == "rt": # do not add to list if word is "rt"
                break
            for item in end_strip:
                if word.endswith(item):
                    word = word[:-1]
            for item in start_strip:
                if word.startswith(item):
                    word = word[1:]
            words.append(word)

tweets_file.close()

prefix_list = ("http", "@", "t.co", "bit.ly")
# don't reckon words that start with any of the strings in the prefix list
for word in words[:]:
    if word.startswith(prefix_list):
        words.remove(word)

text = ""
for word in words:
    print word
    text = text + " " + word
print text
text = text.encode('utf-8') # for non-English characters

#######################
# This part of the script uses the wordcloud library
# Installation is through pip
# library is at https://github.com/amueller/word_cloud
# Dependies for wordcloud are two: (1) matplotlib (2) Pillow
# (matplotlib needs Pillow to work, since no PIL)
# Both matplotlib and Pillow can be pip installed
#######################

from wordcloud import WordCloud
wordcloud = WordCloud().generate(text)

# added this code from http://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear
# so that the generated figure can be saved as well
import matplotlib
matplotlib.use('Agg')
#
import matplotlib.pyplot as plt

plt.imshow(wordcloud)
plt.axis("off")
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
#plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
# save the figure
plt.savefig('./examples/tweet_cloud')
