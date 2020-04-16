# This is the file which crawl Asr Iran
# https://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1399/01/01&to_date=1399/01/28&p=1
import requests
from bs4 import BeautifulSoup
from pathlib import Path

import utility

sit_url = "https://www.asriran.com"
search_url = "https://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1399/01/01&to_date=1399/01/28"
response = requests.get(search_url)

soup = BeautifulSoup(response.text, "html.parser")


# get page numbers
query_page_count = soup.select_one("#pager").get_text().split(' ')[3]
page_count = utility.persianCharacterResolver(query_page_count)

news_urls = []

# iterate over pages
# for i in range(1, page_count):
#     url = search_url+"&p="+str(i)
#     response = requests.get(url)
#     news = soup.select(".archive_content .linear_news a")
#     for n in news:
#         news_urls.append(n.get("href", "problem"))

# utility.saveToJsonFile(news_urls, Path("Data/news.json"))
urls = utility.loadFromJsonFile("Data/news_urls.json")


print(soup.select_one("#pager").get_text())
# print()
