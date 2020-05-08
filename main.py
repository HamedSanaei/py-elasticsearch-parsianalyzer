from src import elastic_query as eq


re_crawling = input(
    "Data has been provided before and exist in \"Data\" folder.\n Do you want to re-crawl and get data? [Y/n]")
if re_crawling == ('y' or "Y"):
    print("Starting to crawling data ...")
    from src import webscrapper
else:
    print("Starting to index and searching for queries ...")

re_index = input(
    "Do you want to index or re-index documents?[Y/n] \n (Hint: if you are trying app for first time type \'y\' otherwise \'n\')")

if re_index == ('y' or "Y"):
    print("Starting to indexing data ...")
    from src import elastic_index


print("Searching for queries ...")

query = "لَنتِرنُت"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "1")

query = "محدودیت‌هایی"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "2")

query = "حدود ۶٫۷ درصد"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "3")
query = "درمان سخت‌تر خواهد بود و در ادامه افراد بیشتری به بخش های مراقبت‌های"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "4")

query = "2018بیش از 118 میلیارد دلار (67 میلیارد پوند)"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "5")

query = "آمایت مهتانی"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "6")

query = "سریلانکا"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "7")

query = "۱۲"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Date_fa"], "8")

query = "13"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Date_en"], "9")

query = "بیل د بلا"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "10")

query = "تعطیلی مدارس نیویورک تا پایان"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "11")

query = "اسماعیل للــه گنی"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "12")

query = "کتاد"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "13")

query = "تنی چند از مدیران عامل بانک ها برگذار شد"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "14")

query = "استعفای وزیر هنر استرالیا پس از"
res = eq.Queries.customSearchByTermSugestion(
    query, "hamed-parsianalyzer", ["Body", "Title"], "15")

print("Searching for queries was completed!")
# res = eq.Queries.firstQuestion()
# res = eq.Queries.secondQuestion()
# res = eq.Queries.thirdQuestion()
# res = eq.Queries.fourthQuestion()
# res = eq.Queries.fifthQuestion()
# res = eq.Queries.sixthQuestion()
# res = eq.Queries.seventhQuestion()
# res = eq.Queries.eighthQuestion()
# res = eq.Queries.ninthQuestion()
# res = eq.Queries.tenthQuestion()
# res = eq.Queries.eleventhQuestion()
# res = eq.Queries.twelvthQuestion()
# res = eq.Queries.thirtheenthQuestion()
# res = eq.Queries.fourteenthQuestion()
# res = eq.Queries.fiftheenthQuestion()
