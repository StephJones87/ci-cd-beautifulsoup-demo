# CI/CD BeautifulSoup Demo 🧪

This is the simplest possible Python project that:

- Scrapes a real website using `BeautifulSoup`
- Includes one test using `pytest`
- Runs tests automatically using **GitHub Actions** (CI)

## 🔍 What It Does

`scraper.py` contains a function that fetches the `<title>` of a web page using `requests` and `BeautifulSoup`.

We scrape: [https://httpbin.org/html](https://httpbin.org/html), which returns a simple HTML page titled with **"Herman Melville - Moby-Dick"**.

## ✅ Test

`test_scraper.py` checks that the title includes "Herman Melville".

To run it locally:

```bash
pip install -r requirements.txt
pytest
```

## ⚙️ GitHub Actions CI

Inside `.github/workflows/ci.yml`, we define a workflow that:

- Installs Python
- Installs dependencies
- Runs `pytest`

This happens automatically on **every push or pull request**.

## 🗂️ Project Structure

```
ci-cd-beautifulsoup-demo/
├── scraper.py
├── test_scraper.py
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml
```

## 🧠 Why This Exists

To help beginners learn:

- Basic web scraping
- Writing and running Python tests
- Setting up CI/CD with GitHub Actions

Feel free to fork this and build on it!
