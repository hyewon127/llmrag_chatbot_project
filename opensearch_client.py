from opensearchpy import OpenSearch

client = OpenSearch(

    hosts=[{
        "host":"opensearch",
        "port":9200
    }],

    use_ssl=False,
    verify_certs=False
)
