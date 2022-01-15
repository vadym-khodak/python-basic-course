def test_index():
    from .web import app

    # GIVEN a Flask test client
    with app.test_client() as client:

        # WHEN send get request to "/" url
        response = client.get("/")

        # THEN response status equals 200 and content_type should be text/html
        assert response.status_code == 200
        assert response.content_type == "text/html; charset=utf-8"


def test_ping():
    from .web import app

    # GIVEN a Flask test client
    with app.test_client() as client:

        # WHEN send get request to "/ping" url
        response = client.get("/ping")

        # THEN response status equals 200 and content_type should be "text/html" decoded data is "pong"
        assert response.status_code == 200
        assert response.data.decode() == "pong"
        assert response.content_type == "text/html; charset=utf-8"


def test_api_ping():
    from .web import app

    # GIVEN a Flask test client
    with app.test_client() as client:

        # WHEN send get request to "/api/ping" url
        response = client.get("/api/ping")

        # THEN response status equals 200 and content_type should be "application/json" json.message is "pong"
        assert response.status_code == 200
        assert response.json["message"] == "pong"
        assert response.content_type == "application/json"


if __name__ == "__main__":
    pass
