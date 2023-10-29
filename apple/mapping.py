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
        "id": {"type": "long"},
        "url": {"type": "text"},
        "maxUpvotes": {"type": "integer"},
        "text_vector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "dot_product"
        },
        "text_summary_vector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "dot_product"
        },
        "text_summary_modified_vector": {
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
                "id": {"type": "long"},
                "replyCount": {"type": "integer"},
                "upvoteCount": {"type": "integer"},
                "dateCreated": {"type": "date", "format": "yyyy-MM-dd'T'HH:mm:ss"},
                "author": {"type": "text"},
                "community": {"type": "text"},
                "subcommunity": {"type": "text"},
                "product": {"type": "text"},
                "OS": {"type": "text"},
                "additionalInfo": {"type": "text"},
                "name": {"type": "text"},
                "text": {"type": "text"},
                "textSummary": {"type": "text"},
                "textSummaryModified": {"type": "text"}
            }
        },
        "answers": {
            "type": "nested",
            "properties": {
                "id": {"type": "long"},
                "responseId": {"type": "long"},
                "upvoteCount": {"type": "integer"},
                "dateCreated": {"type": "date", "format": "yyyy-MM-dd'T'HH:mm:ss"},
                "author": {"type": "text"},
                "text": {"type": "text"}
            }
        }
    }
}

client.indices.create(index='apple', mappings=mappings)