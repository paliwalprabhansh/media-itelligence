from flask import Flask, request, jsonify
import logging
from utils.news_fetcher import fetch_news
from utils.ml_utils import analyze_sentiment, extract_keywords
import datetime
import json

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    print('Searching')
    
    if not start_date or not end_date:
        return jsonify({'error': 'Missing "start_date" or "end_date" parameter'}), 400
    
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400
    
    try:
        print("Trying to search in the news")
        news_articles = fetch_news(query, start_date, end_date)
        if news_articles is not None:
            with open('news_articles.json', 'w') as f:
                json.dump(news_articles, f)
        results = []
        for article in news_articles:
            print("Sendtiments and news articles")
            sentiment = analyze_sentiment(article.get('title', ''))
            keywords = extract_keywords(article.get('title', ''))
            article['sentiment'] = sentiment
            article['keywords'] = keywords
            
            results.append(article)
            print(results)
        logging.info(f"Search successful for query: {query}")
        return jsonify(results), 200
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8081)