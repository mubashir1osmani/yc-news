from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_news = response.text
soup = BeautifulSoup(yc_news, 'html.parser')

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    for link in soup.find("a"):
        print(link.get("href"))

article_upvote = [score.getText() for score in soup.find_all(name= "span", class_="score")]

print(article_texts[0])
