def test_get_users(api_client):
    response = api_client.get("/users", params={"page": 2})

    assert response.status_code == 200, f"Unexpected status {response.status_code}"
    data = response.json()

    assert "data" in data, "Response JSON missing 'data' key"
    assert isinstance(data["data"], list), "'data' is not a list"
    assert len(data["data"]) > 0, "User list is empty"

    assert response.elapsed.total_seconds() < 2, "API response too slow"
