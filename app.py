from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "26fdba1da5a9502fc6427b443d858197"  # Replace with your GNews API Key
NEWS_URL = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=us&max=10&apikey={API_KEY}"

@app.route("/")
def home():
    response = requests.get(NEWS_URL)
    news_data = response.json().get("articles", [])  # Extract articles list
    return render_template("index.html", news=news_data)

if __name__ == "__main__":
    app.run(debug=True)
