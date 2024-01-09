from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup

import os
from dotenv import load_dotenv
load_dotenv()
client = Elasticsearch(os.getenv("ELASTIC_URL"),
                       ca_certs="./http_ca.crt",
                       basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
                       verify_certs=False)

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

hits = resp["hits"]["hits"]
questions = [thread["_source"]["question"]["name"] for thread in hits]

for i, question in enumerate(questions):
    print(f"{i}. {question}")

print("\n")
index = int(input("Which is your problem? "))

solutions = [solution["text"] for solution in hits[index]["_source"]["answers"]]
for solution in solutions:
    print("\n")
    print(BeautifulSoup(solution, features="lxml").get_text())
