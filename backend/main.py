from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from movies import MOVIES
from recommender import MovieRecommender

app = FastAPI(title="CineMatch ML API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173","http://127.0.0.1:5173"], allow_methods=["GET"], allow_headers=["*"])
model = MovieRecommender()

@app.get("/health")
def health():
    return {"status": "ok", "catalog_size": len(MOVIES), "model": "tfidf-cosine"}

@app.get("/movies")
def movies(q: str = Query(default="", max_length=100)):
    term = q.strip().casefold()
    return [m for m in MOVIES if not term or term in m["title"].casefold() or any(term in g.casefold() for g in m["genres"])]

@app.get("/recommend/{movie_id}")
def recommend(movie_id: int, limit: int = Query(default=5, ge=1, le=10)):
    try:
        return {"seed": next(m for m in MOVIES if m["id"] == movie_id), "recommendations": model.recommend(movie_id, limit)}
    except (KeyError, StopIteration):
        raise HTTPException(status_code=404, detail="Movie not found") from None
