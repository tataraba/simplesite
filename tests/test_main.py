
def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>Hello World!</h1>" in response.text
