import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def fetch_article(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_article(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ' '.join([para.get_text() for para in paragraphs])
    return article_text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\W', ' ', text)  # Remove non-word characters
    text = text.lower()  # Convert to lowercase
    return text

def collect_data(urls):
    articles = []
    for url in urls:
        html_content = fetch_article(url)
        if html_content:
            article_text = parse_article(html_content)
            cleaned_text = clean_text(article_text)
            articles.append(cleaned_text)
    return articles

def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=['text'])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    urls = [
        'https://example.com/news1',
        'https://example.com/news2',
        'https://example.com/news3'
    ]
    articles = collect_data(urls)
    save_to_csv(articles, 'collected_news.csv')
