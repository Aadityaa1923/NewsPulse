from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from textblob import TextBlob
from pydantic import BaseModel

app = FastAPI()

class LoginData(BaseModel):
    username: str
    password: str

class SignupData(BaseModel):
    name: str
    email: str
    password: str
    interests: list[str]

users_db = []

@app.post("/login")
def login(user: LoginData):
    if user.username == "admin" and user.password == "1234":
        return {
            "status": "success",
            "message": "Login successful",
            "user": "Admin"
        }

    for u in users_db:
        if u["email"] == user.username and u["password"] == user.password:
            return {
                "status": "success",
                "message": "Login successful"
            }

    return {
        "status": "error",
        "message": "Invalid credentials"
    }

@app.post("/signup")
def signup(user: SignupData):
    for u in users_db:
        if u["email"] == user.email:
            return {
                "status": "error",
                "message": "Email already registered"
            }

    users_db.append({
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "interests": user.interests
    })

    return {
        "status": "success",
        "message": "Account created successfully"
    }
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "d9d860e0008e4e16a0932e57d4697c74"

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