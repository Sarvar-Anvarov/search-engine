from nltk.corpus import stopwords
from search_engine.config import settings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TfidfSearchEngine:
    def __init__(self, model=None):
        self.name = "tf-idf"
        self.model = model

    def fit(self, X):
        vectorizer = TfidfVectorizer(stop_words=stopwords.words("russian"))
        self.model = vectorizer.fit(X)
        return vectorizer.transform(X)

    def predict(self, request, X_transformed, top_n):
        if not self.model:
            raise Exception("Model is not fitted yet. Fit model before predicting.")

        pred = self.model.transform([request]).toarray()
        return cosine_similarity(X_transformed, pred).squeeze().argsort()[-top_n:][::-1]
