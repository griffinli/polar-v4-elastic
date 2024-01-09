from elasticsearch import Elasticsearch
import json

import os
from dotenv import load_dotenv
load_dotenv()
client = Elasticsearch(os.getenv("ELASTIC_URL"),
                       ca_certs="./http_ca.crt",
                       basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
                       verify_certs=False)

# resp = client.search(query={
#     "nested": {
#         "path": "question",
#         "query": {
#             "bool": {
#                 "must": [
#                     {"match": {"question.name": "start"}}
#                 ]
#             }
#         }
#     }
# }, index="apple")

resp = client.search(query={
    "nested": {
        "path": "question",
        "query": {
            "bool": {
                "must": [
                    {"match": {"question.name": "iphone frozen"}}
                ]
            }
        }
    }
}, index="apple")

# resp = client.search(query={
#     "match": {
#         "url": {
#             "query": "122300"
#         }
#     }
# }, index="apple")


print(json.dumps(dict(resp)))