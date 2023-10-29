from elasticsearch import Elasticsearch

import os
from dotenv import load_dotenv
load_dotenv()
client = Elasticsearch(os.getenv("ELASTIC_URL"),
                       ca_certs="./http_ca.crt",
                       basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
                       verify_certs=False)

# can also add date format
mappings = {
    "properties": {
        "url": {"type": "text"},
        "maxUpvotes": {"type": "integer"},
        "text_vector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "dot_product"
        },
        "name_vector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "dot_product"
        },
        "question": {
            "type": "nested",
            "properties": {
                "type": {"type": "text"},
                "upvoteCount": {"type": "integer"},
                "viewCount": {"type": "integer"},
                "replyCount": {"type": "integer"},
                "dateCreated": {"type": "date", "format": "yyyy-MM-dd'T'HH:mm:ss"},
                "authorName": {"type": "text"},
                "authorId": {"type": "text"},
                "category0": {"type": "text"},
                "category1": {"type": "text"},
                "category2": {"type": "text"},
                "name": {"type": "text"},
                "text": {"type": "text"}
            }
        },
        "answers": {
            "type": "nested",
            "properties": {
                "id": {"type": "text"},
                "parentId": {"type": "text"},
                "upvoteCount": {"type": "integer"},
                "dateCreated": {"type": "date", "format": "yyyy-MM-dd'T'HH:mm:ss"},
                "authorName": {"type": "text"},
                "authorId": {"type": "text"},
                "text": {"type": "text"}
            }
        }
    }
}

client.indices.create(index='microsoft', mappings=mappings)