import requests
import os
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()

def main():
    topic=input("Enter a topic: ")
    headlines=fetch_headlines(topic, 10)
    sentiments=analyse_sentiments(headlines)
    print_summary(headlines, sentiments)


def fetch_headlines(topic, limits):
    """Fetch headlines from NewsAPI"""
    api_key=os.getenv("NEWS_API_KEY")
    url=(f"https://newsapi.org/v2/everything?"
         f"q={topic}&"
         f"language=en&"
         f"sortBy=publishedAt&"
         f"pageSize={limits}&"
         f"apiKey={api_key}")
    response=requests.get(url)
    if response.status_code !=200:
        print("Error:", response.status_code)
        return []
    data=response.json()
    return [article["title"] for article in data['articles']]


def analyse_sentiments(headlines):
    """Analyse sentiment polarity of each headline using TextBlob
    Returns a list of float sentiment scores ranging from -1 (most negative) to 1 (most positive)"""
    scores=[]
    for h in headlines:
        scores.append(TextBlob(h).sentiment.polarity)
    return scores


def print_summary(headlines, sentiments):
    """Print each headline with its sentiment score and the average score"""
    for h,s in zip(headlines, sentiments):
        print(f"{s:.2f} -> {h}")
    if sentiments:
        avg=sum(sentiments)/len(sentiments)
    else:
        avg=0

    print(f"\nAverage sentiment score: {avg:.2f}")


if __name__ == "__main__":
    main()
