import requests
import datetime 
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_URL = 'https://v3-api.newscatcherapi.com/api/search'
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def fetch_news(query, start_date, end_date):
    print("Inside the news fetcher API")
    print(query)
    headers = {
        'x-api-token': NEWS_API_KEY,
        'Content-Type': 'application/json'
    }

    params = {  
        'q': query,
        'from_': 1,
        'countries': 'CA',  
        'page_size': 10
    }
    req = requests.Request('GET', NEWS_API_URL, headers=headers, params=params)
    prepared_req = req.prepare()

    print(f"Full URL: {prepared_req.url}")
    try:
        response = requests.get(NEWS_API_URL, headers=headers, params=params)
        print(f"Response status code: {response.status_code}")
        print(f"Response content type: {response.headers['Content-Type']}")
        response.raise_for_status()
        print(response.json())
        return response.json().get('articles')
    
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

