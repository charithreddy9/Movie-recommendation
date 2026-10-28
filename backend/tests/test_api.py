from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    result = client.get("/health")
    assert result.status_code == 200
    assert result.json()["catalog_size"] == 12

def test_recommendation_ranking():
    result = client.get("/recommend/1?limit=4")
    assert result.status_code == 200
    items = result.json()["recommendations"]
    assert len(items) == 4
    assert all(item["id"] != 1 for item in items)
    assert [m["score"] for m in items] == sorted([m["score"] for m in items], reverse=True)

def test_invalid_id():
    assert client.get("/recommend/999").status_code == 404

def test_invalid_limit():
    assert client.get("/recommend/1?limit=0").status_code == 422

def test_genre_search():
    result = client.get("/movies?q=romance").json()
    assert result and all("Romance" in m["genres"] for m in result)
