from elasticsearch import Elasticsearch


es = Elasticsearch()


class Queries():

    @classmethod
    def firstQuestion(cls):
        match_query = "لَنتِرنُت"
        cls.initialMethod("First", "One", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":   match_query,
                "fields": ["Body", "Title"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def secondQuestion(cls):
        match_query = "محدودیت‌هایی"
        cls.initialMethod("Second", "One", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":   match_query,
                "fields": ["Body", "Title"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def thirdQuestion(cls):
        match_query = "حدود ۶٫۷ درصد"
        cls.initialMethod("Third", "One", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query": match_query,
                "fields": ["Body", "Title"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def fourthQuestion(cls):
        match_query = "درمان سخت‌تر خواهد بود و در ادامه افراد بیشتری به بخش های مراقبت‌های"
        cls.initialMethod("Fourth", "One", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":  match_query,
                "fields": ["Body", "Title"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def fifthQuestion(cls):
        match_query = "2018بیش از 118 میلیارد دلار (67 میلیارد پوند)"
        cls.initialMethod("Fifth", "One", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query": match_query,
                "fields": ["Body", "Title"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def sixthQuestion(cls):
        match_query = "آمایت مهتانی"
        cls.initialMethod("Sixth", "One", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":  match_query,
                "fields": ["Body", "Title"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def seventhQuestion(cls):
        match_query = "سریلانکا"
        cls.initialMethod("Seventh", "One", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query": match_query,
                "fields": ["Body", "Title"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def eighthQuestion(cls):
        match_query = "۱۲"
        cls.initialMethod("Eighth", "Two", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":  match_query,
                "fields": ["Date_en", "Date_fa"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def ninthQuestion(cls):
        match_query = "13"
        cls.initialMethod("Ninth", "Two", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":  match_query,
                "fields": ["Date_en", "Date_fa"]
            }
        }})
        Queries.printResult(res)

    @classmethod
    def tenthQuestion(cls):
        match_query = "بیل د بلا"
        #match_query = "بلاسی"
        cls.initialMethod("Tenth", "Three", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":  match_query,
                "fields": ["Body", "Title"]
            }
        }, "suggest": {
            "text": match_query,
            "my-suggest-1": {
                "term": {
                    "field": "Body"
                }
            },
            "my-suggest-2": {
                "term": {
                    "field": "Title"
                }
            }
        }})
        Queries.printResult(res)
        return res

    @classmethod
    def eleventhQuestion(cls):
        match_query = "تعطیلی مدارس نیویورک تا پایان"
        cls.initialMethod("Eleventh", "Three", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query": match_query,
                "fields": ["Body", "Title"]
            }
        }, "suggest": {
            "text": match_query,
            "my-suggest-1": {
                "term": {
                    "field": "Body"
                }
            },
            "my-suggest-2": {
                "term": {
                    "field": "Title"
                }
            }
        }})
        Queries.printResult(res)
        return res

    @classmethod
    def twelvthQuestion(cls):
        match_query = "اسماعیل للــه گنی"
        cls.initialMethod("Twelveth", "Three", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":  match_query,
                "fields": ["Body", "Title"]
            }
        }, "suggest": {
            "text": match_query,
            "my-suggest-1": {
                "term": {
                    "field": "Body"
                }
            },
            "my-suggest-2": {
                "term": {
                    "field": "Title"
                }
            }
        }})
        Queries.printResult(res)
        return res

    @classmethod
    def thirtheenthQuestion(cls):
        match_query = "کتاد"
        cls.initialMethod("Thirtheenth", "Three", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":   match_query,
                "fields": ["Body", "Title"]
            }
        }, "suggest": {
            "text": match_query,
            "my-suggest-1": {
                "term": {
                    "field": "Body"
                }
            },
            "my-suggest-2": {
                "term": {
                    "field": "Title"
                }
            }
        }})
        Queries.printResult(res)
        return res

    # @classmethod
    # def fourteenthQuestion(cls):
    #     cls.initialMethod("Twelve", "Three")
    #     res = es.search(index="hamed-parsianalyzer", body={"query": {
    #         "multi_match": {
    #             "query":   "تنی چند از مدیران عامل بانک ها برگذار شد",
    #             "fields": ["Body", "Title"]
    #         }
    #     }, "suggest": {
    #         "text": "تنی چند از مدیران عامل بانک ها برگذار شد",
    #         "simple_phrase": {
    #             "phrase": {
    #                 "field": "Body.trigram",
    #                 "size": 1,
    #                 "gram_size": 3,
    #                 "direct_generator": [{
    #                     "field": "Body.trigram",
    #                     "suggest_mode": "always"
    #                 }],
    #                 "highlight": {
    #                     "pre_tag": "<em>",
    #                     "post_tag": "</em>"
    #                 }
    #             }
    #         }
    #     }})
    #     Queries.printResult(res)
    #     return res
    @classmethod
    def fourteenthQuestion(cls):
        match_query = "تنی چند از مدیران عامل بانک ها برگذار شد"
        cls.initialMethod("Fourteenth", "Three", match_query)

        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query": match_query,
                "fields": ["Body", "Title"]
            }
        }, "suggest": {
            "text": match_query,
            "my-suggest-1": {
                "term": {
                    "field": "Body"
                }
            },
            "my-suggest-2": {
                "term": {
                    "field": "Title"
                }
            }
        }})
        Queries.printResult(res)
        return res

    @classmethod
    def fiftheenthQuestion(cls):
        match_query = "استعفای وزیر هنر استرالیا پس از"
        cls.initialMethod("Fiftheenth", "Three", match_query)
        res = es.search(index="hamed-parsianalyzer", body={"query": {
            "multi_match": {
                "query":  match_query,
                "fields": ["Body", "Title"]
            }
        }, "suggest": {
            "text": match_query,
            "my-suggest-1": {
                "term": {
                    "field": "Body"
                }
            },
            "my-suggest-2": {
                "term": {
                    "field": "Title"
                }
            }
        }})
        Queries.printResult(res)
        return res

    @classmethod
    def initialMethod(self, question_number, section_number, match_query):
        print("============================================")
        print(
            f"This is answer to {question_number} question in section {section_number}")
        print(f"Search for: {match_query}")

    @classmethod
    def printResult(cls, res):
        print("Got %d Hits:" % res['hits']['total']['value'])
        for hit in res['hits']['hits']:
            tmp = str(hit["_score"])
            print(
                "Title: %(Title)s: News_url: %(Short_Link)s Score: " % hit["_source"]+tmp)
