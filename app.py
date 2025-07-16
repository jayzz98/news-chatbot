from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

NEWS_API_KEY = "89534d0c42a2e05fa7ddf778cdd29f5c"

@app.route('/search-news', methods=['POST'])
def search_news():
    data = request.get_json()
    query = data.get("query", "")
    
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news = response.json()

    articles = []
    for article in news.get("articles", []):
        articles.append({
            "title": article["title"],
            "url": article["url"],
            "source": article["source"]["name"],
            "publishedAt": article["publishedAt"]
        })

    return jsonify({"results": articles})
    
if __name__ == '__main__':
    app.run(debug=True)
