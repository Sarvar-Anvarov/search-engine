import os
import sys
import nltk

# this is temporary solution
sys.path.append(os.path.join(sys.path[0], "../../src"))

# download stopwords
nltk.download("stopwords")


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    return f'<a target="_blank" href="{link}">{link}</a>'
