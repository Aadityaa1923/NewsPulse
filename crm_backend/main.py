import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from textblob import TextBlob


def load_dotenv(path: str = ".env") -> None:
    env_path = Path(path)
    if not env_path.is_file():
        return

    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        key, sep, value = line.partition("=")
        if sep != "=":
            continue

        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and value and key not in os.environ:
            os.environ[key] = value


load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("NEWSAPI_KEY")
if not API_KEY:
    raise RuntimeError("NEWSAPI_KEY must be set in environment or .env file")


@app.get("/")
def home():
    return {"message":"News CRM Backend Running"}

@app.get("/news")
def get_news():
    url = f"https://newsapi.org/v2/everything?q=india&apiKey={API_KEY}"
    r = requests.get(url)
    data = r.json()

    for article in data["articles"][:10]:
        text = article["title"] or ""
        polarity = TextBlob(text).sentiment.polarity
        article["sentiment_score"] = polarity

    return data