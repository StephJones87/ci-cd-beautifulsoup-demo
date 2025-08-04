from scraper import get_title

def test_get_title():
    url = "https://httpbin.org/html"
    title = get_title(url)
    assert "Herman Melville" in title
