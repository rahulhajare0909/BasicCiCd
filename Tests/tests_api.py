import requests

def test_google_status():
    r = requests.get("https://www.google.com")
    assert r.status_code == 200