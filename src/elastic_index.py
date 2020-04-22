from elasticsearch import Elasticsearch
import utility
from pathlib import Path

es = Elasticsearch()
# jj = es.indices.analyze

es.indices.delete(index="hamed-parsianalyzer")

# We can specify Analyzer by Mapping or while creating index
es.indices.create(index="hamed-parsianalyzer", body={"mappings": {
    "properties": {
        "Body": {
            "type": "text",
            "analyzer": "parsi"
        },
        "Title": {
            "type": "text",
            "analyzer": "parsi"
        }
    }
}})


# We can specify Analyzer by Mapping or while creating index
# es.indices.create(index="hamed-parsianalyzer", body={"settings": {
#     "index": {
#         "number_of_shards": 1,
#         "analysis": {
#             "analyzer": {
#                 "trigram": {
#                   "type": "custom",
#                   "tokenizer": "standard",
#                   "filter": ["lowercase", "shingle"]
#                   },
#                 "reverse": {
#                     "type": "custom",
#                     "tokenizer": "standard",
#                     "filter": ["lowercase", "reverse"]
#                 }
#             },
#             "filter": {
#                 "shingle": {
#                     "type": "shingle",
#                     "min_shingle_size": 2,
#                     "max_shingle_size": 3
#                 }
#             }
#         }
#     }
# }, "mappings": {
#     "properties": {
#         "Body": {
#             "type": "text",
#             "analyzer": "parsi",
#             "fields": {
#                 "trigram": {
#                     "type": "text",
#                     "analyzer": "trigram"
#                 },
#                 "reverse": {
#                     "type": "text",
#                     "analyzer": "reverse"
#                 }
#             }
#         },
#         "Title": {
#             "type": "text",
#             "analyzer": "parsi",
#             "fields": {
#                 "trigram": {
#                     "type": "text",
#                     "analyzer": "trigram"
#                 },
#                 "reverse": {
#                     "type": "text",
#                     "analyzer": "reverse"
#                 }
#             }
#         }
#     }
# }})


docs = utility.convertToArrayDictionary(Path("Data/news_data.json"))

for i in range(0, len(docs)):
    es.index(index="hamed-parsianalyzer",
             id=i, body=docs[i])


# hamed bulk index kon file json ro
