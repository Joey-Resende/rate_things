from fastapi.testclient import TestClient

from rate_things.api import api

client = TestClient(api)
 
 
def test_create_things_via_api():
    response = client.post(
        '/things', 
        json={
            "things": "Serie", 
            "name": "Cavaleiro da Lua", 
            "gender": "Heroi", 
            "score": 7, 
            "image": 7, 
            "cost": 7,
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["things"] == "Serie"
    assert result["id"] == 1
