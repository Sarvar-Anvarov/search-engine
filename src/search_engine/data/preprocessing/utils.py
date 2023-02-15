import nltk

nltk.download("stopwords")
# --------#

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

# Create lemmatizer and stopwords list
mystem = Mystem()
russian_stopwords = stopwords.words("russian")

def tokenize_description(text, tokenizer):
    return tokenizer.tokenize(text)


def remove_stopwords(text, stop_words):
    filtered_text = []
    for word in text:
        if word not in stop_words:
            filtered_text.append(word)

    return filtered_text

# Preprocess function
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]

    text = " ".join(tokens)

    return text