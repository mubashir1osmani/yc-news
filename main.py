from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_news = response.text
soup = BeautifulSoup(yc_news, 'html.parser')



#traverses the tree and finds the span -> titleline
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
links = []

for article in articles:
    article_tag = soup.find(name="a", className_="titleline")
    text = article.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    links.append(link)
    print(article_texts)
    print(links)