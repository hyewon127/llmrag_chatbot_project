from opensearch_client import client

index_name = "documents"

body = {

    "settings": {
        "index": {
            "knn": True 
        }
    },

    "mappings": {
        "properties": {

            "content": {
                "type": "text"
            },

            "embedding": {
                "type": "knn_vector",
                "dimension": 384
            }
        }
    }
}

client.indices.create(
    index=index_name,
    body=body
)
