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


# iterate over pages
# news_urls = []
# for i in range(1, page_count):
#     url = search_url+"&p="+str(i)
#     response = requests.get(url)
#     news = soup.select(".archive_content .linear_news a")
#     for n in news:
#         news_urls.append(n.get("href", "problem"))

# utility.saveToJsonFile(news_urls, Path("Data/news_urls.json"))


urls = utility.loadFromJsonFile("Data/news_urls.json")


# this for is to slow
for news_url in urls:
    response = requests.get(sit_url+news_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # # shortlink is complete
    # short_link = soup.select_one(".link_en").get_text()
    # short_link = utility.removeTabAndLineCharacterAndSpaces(short_link)

    # # id is complete
    # news_id = soup.select_one(" .news_id_c").get_text()
    # news_id = utility.persianCharacterResolver(news_id)

    # # title is complete
    # title = soup.select_one(" .title").get_text()
    # title = ' '.join(title.split())

    # # category is complete
    # category_fa = soup.select_one(
    #     "#news > div.container.common-main.news-main > div > div.row > div.col1-news > div:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div > a:nth-child(2)").get_text()
    # category_Id = soup.select_one(
    #     "#news > div.container.common-main.news-main > div > div.row > div.col1-news > div:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div > a:nth-child(2)").get("href").split('=')[2]

    # # tag is complete
    # tags = soup.select(".tags_item")
    # tag_array = [tag.get_text() for tag in tags]

    ## body is complete
   ######## body = utility.removeHTMLTags(soup.select(".body").get_text())

    ## date is complete

    date_en = soup.select_one(
        "#news > div.container.common-main.news-main > div > div.row > div.col1-news > div:nth-child(10) > div.row.b_mrg > div.col-sm-6.col-ms-12 > div > span:nth-child(2)").get_text()
    date_fa = ' '.join(soup.select_one(
        ".news_pdate_c").get_text().split()).replace(date_en, '').replace("تاریخ انتشار: ", '')

    print(date_fa)


# print()
