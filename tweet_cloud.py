#
# This program uses the wordcloud library
# Installation is through pip
# library is at https://github.com/amueller/word_cloud
# Dependies for wordcloud are two: (1) matplotlib (2) Pillow
# (matplotlib needs Pillow to work, since no PIL)
# Both matplotlib and Pillow can be pip installed
#

from wordcloud import WordCloud

# Read the tweet text
text = open('tweet_text.txt').read()

# Generate a wordcloud image
wordcloud = WordCloud().generate(text)

import matplotlib 
# added this code from http://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear
matplotlib.use('Agg') 
# added this code from http://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear
import matplotlib.pyplot as plt

plt.imshow(wordcloud)
plt.axis("off")
# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
# Save the image instead of displaying it
plt.savefig('tweet_cloud')
