import requests
from bs4 import BeautifulSoup
from pathlib import Path
from src import utility
import time


start_time = time.time()


sit_url = "https://www.asriran.com"
search_url = "https://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1399/01/01&to_date=1399/01/28"


string_args = input("""for crawl default news from 1st to 28th Farvardin 1399 type
-default To specify start date type -sdate and for ending date select -edate and for 
subject news type -subject. there are several news subject such as:
-1 ==> all subject
1  ==> political
2  ==> foreign policy
3  ==> international
4  ==> economic
5  ==> social
6  ==> sport
7  ==> scientific
8  ==> cultural/art
9  ==> accidents
10 ==> health
11 ==> technology & IT
12 ==> hobby
13 ==> general
14 ==> users
15 ==> chat cafe
16 ==> travel
(Hint: -edate 1399/01/01 -sdate 1385/01/01 -subject -1 )
""")
args = string_args.split()


starting_date = None
ending_date = None
catt_idd = None


for index, arg in enumerate(args):
    if arg == "-sdate":
        starting_date = args[index+1]
    elif arg == "-edate":
        ending_date = args[index+1]
    elif arg == "-subject":
        catt_idd = args[index+1]
    elif arg == "-default":
        search_url = "https://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1399/01/01&to_date=1399/01/28"

if args.__contains__("-default"):
    search_url = "https://www.asriran.com/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=100&from_date=1399/01/01&to_date=1399/01/28"
elif (starting_date is not None) and (ending_date is not None) and (catt_idd is not None):
    search_url = f"https://www.asriran.com/fa/archive?service_id=1&sec_id=-1&cat_id={catt_idd}&rpp=100&from_date={starting_date}&to_date={ending_date}"

response = requests.get(search_url)

soup = BeautifulSoup(response.text, "html.parser")

# get page numbers
query_page_count = soup.select_one("#pager").get_text().split(' ')[3]
page_count = utility.persianCharacterResolver(query_page_count)


# # # iterate over pages
news_urls = []
for i in range(1, page_count):
    url = search_url+"&p="+str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    news = soup.select(".archive_content .linear_news a")
    for n in news:
        news_urls.append(n.get("href", "problem"))

utility.saveToJsonFile(news_urls, Path("Data/news_urls.json"))
# print(time.time() - start_time)

urls = utility.loadFromJsonFile("Data/news_urls.json")


# this for is too slow
news_data = []
for idx, news_url in enumerate(urls):
    response = requests.get(sit_url+news_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # # shortlink is complete
    short_link = soup.select_one(".link_en").get_text()
    short_link = utility.removeTabAndLineCharacterAndSpaces(short_link)

    # # id is complete
    news_id = soup.select_one(" .news_id_c").get_text()
    news_id = utility.persianCharacterResolver(news_id)

    # # title is complete
    title = soup.select_one(" .title").get_text()
    title = ' '.join(title.split())

    # # category is complete
    category_fa = soup.select_one(
        ".news_path > a:nth-child(2)").get_text()
    category_Id = soup.select_one(
        ".news_path > a:nth-child(2)").get("href").split('=')[2]

    # # tag is complete
    # tags = utility.checkForNone(soup.select(".tags_item"))
    # tag_array = [utility.checkForNone(tag).get_text() for tag in tags]
    tags = soup.select(".tags_container .tags_title > a")
    tag_array = [utility.checkForNone(tag).get_text() for tag in tags]

    # body is complete
    body = utility.removeHTMLTags(utility.checkForNone(
        soup.select_one(".body")).get_text())

    # date is complete

    date_en = utility.checkForNone(soup.select_one(
        ".news_pdate_c >span:nth-child(2)")).get_text()
    date_fa = ' '.join(utility.checkForNone(soup.select_one(
        ".news_pdate_c")).get_text().split()).replace(date_en, '').replace("تاریخ انتشار: ", '')

    news_record = {"Id": news_id,
                   "News_url": news_url,
                   "Short_Link": short_link,
                   "Title": title,
                   "Cat_fa": category_fa,
                   "Cat_Id": category_Id,
                   "Tags": tag_array,
                   "Body": body,
                   "Date_en": date_en,
                   "Date_fa": date_fa
                   }
    news_data.append(news_record)
    fff = float(idx)/float(4102)
    print(str(idx)+"  " + str(float(idx)/float(4102)*100) + "  "+str(news_id))

utility.saveToJsonFile(news_data, "Data/news_data.json")
print(time.time() - start_time)
# print()
