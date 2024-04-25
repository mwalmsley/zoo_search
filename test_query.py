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

    retrieve_response = client.collections['comments'].retrieve()
    print(retrieve_response)

    # print(client.collections['comments'].documents[2130906].retrieve())

    # search_parameters = {
    #     'q': 'galaxy merger',
    #     'query_by': 'comment_body',
    #     }
    # response = client.collections['comments'].documents.search(search_parameters)
    # print(response)
    