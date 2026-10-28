# CineMatch — Full-Stack ML Movie Recommendation System

**Status: working portfolio starter (local development); not yet deployed.**

A content-based movie recommendation app using **scikit-learn TF-IDF + cosine similarity**, served by **FastAPI**, with a responsive **React/Vite frontend**. No paid AI service or API key required.

## What this demonstrates

- **Machine learning:** tokenize movie descriptions and genres; weight genre features; vectorize with TF-IDF; rank by cosine similarity.
- **Backend engineering:** REST endpoints, validation, CORS, error handling, automatic OpenAPI documentation.
- **Frontend engineering:** searchable movie catalog, selectable seed, dynamic ranked recommendations, similarity score bars, responsive layout.
- **Software quality:** automated API tests and a GitHub Actions workflow for tests and frontend build.

## Architecture

```text
React / Vite ──HTTP──► FastAPI ──► scikit-learn TF-IDF model
                                            │
                                            ▼
                                   12 synthetic movie records
```

## Run the app

Requires Python 3.10+ and Node.js 20+.

**Terminal 1 — API:**

```bash
cd backend
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn main:app --reload
```

Open **http://localhost:8000/docs** for interactive API docs.

**Terminal 2 — UI:**

```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:5173**.

To use a nonlocal API, set `VITE_API_BASE_URL` in `frontend/.env`.

## API reference

| Endpoint | Description |
| --- | --- |
| `GET /health` | Model and API health |
| `GET /movies?q=romance` | Search by genre or title |
| `GET /recommend/1?limit=5` | Rank movies similar to item 1 |

## Tests

```bash
cd backend
python -m pytest -q
```

The first five backend API tests passed locally. Frontend build verification depends on installing npm dependencies and is configured in GitHub Actions.

## Dataset, transparency, limitations

`backend/movies.py` contains **12 fictional, hand-written movie entries**. This is a small synthetic catalog, not a representative real-world movie dataset. The recommendation engine is a **real content-based ML baseline**, but it has **no user-behavior data, predictive-rating model, model quality benchmark, or personalized learning**. Similarity scores are not probabilities or predictions of enjoyment.

### Roadmap

- Import a properly licensed movie dataset and document provenance.
- Compare TF-IDF with embedding-based retrieval and evaluate against labeled relevance judgments.
- Add feedback persistence, model versioning, Docker, deployment, observability, and screenshots.
- Track improvement through reproducible experiments and CI.

**Tech:** Python, FastAPI, scikit-learn, React, Vite, pytest, GitHub Actions.

**Repository owner:** [charithreddy9](https://github.com/charithreddy9)
