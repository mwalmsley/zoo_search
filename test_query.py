import typesense

if __name__ == '__main__':

    client = typesense.Client({
        'nodes': [{
        'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
        'port': '8108',      # For Typesense Cloud use 443
        'protocol': 'http'   # For Typesense Cloud use https
        }],
        'api_key': 'xyz',
        'connection_timeout_seconds': 10
    })

    # retrieve_response = client.collections['comments'].retrieve()
    # print(retrieve_response)

    # print(client.collections['comments'].documents[2130906].retrieve())

    search_parameters = {
        'q': 'The zoom scale of this image is incorrect',
        'query_by': 'comment_body',
        # "query_by": "embedding",
        }
    response = client.collections['comments'].documents.search(search_parameters)
    # print(response.keys())
    print(response['hits'][0]['document']['comment_body'])
    print(response['hits'][0]['document']['img_url'])
    