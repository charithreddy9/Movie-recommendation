"""TF-IDF and cosine-similarity content recommender."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from movies import MOVIES

class MovieRecommender:
    def __init__(self, movies=None):
        self.movies = MOVIES if movies is None else movies
        corpus = [" ".join(movie["genres"] * 3) + " " + movie["description"] for movie in self.movies]
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(corpus)
        self.by_id = {movie["id"]: i for i, movie in enumerate(self.movies)}

    def recommend(self, movie_id: int, limit: int = 5):
        if movie_id not in self.by_id:
            raise KeyError(movie_id)
        index = self.by_id[movie_id]
        similarities = cosine_similarity(self.matrix[index], self.matrix).ravel()
        ranked = sorted((i for i in range(len(self.movies)) if i != index), key=lambda i: (-similarities[i], self.movies[i]["id"]))
        return [{**self.movies[i], "score": round(float(similarities[i]), 4)} for i in ranked[:limit]]
