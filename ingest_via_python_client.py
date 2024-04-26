import typesense

SCHEMA = {
      'name' : 'comments',

      'fields' : [

          {
            'name'  : 'comment_body',
            'type'  : 'string',
            'index': True
          },

          {'name'  : 'board_title',
          'type'  : 'string',
          'facet': True
          },

          {'name'  : 'board_description',
          'type'  : 'string',
          'facet' : True},


          {'name'  : 'discussion_title',
          'type'  : 'string',
          'facet': False
          },


          {'name'  : 'comment_id',
          'type'  : 'int64',
          'index' : True,
          'facet' : False},

          {'name'  : 'comment_user_id',
          'type'  : 'int64',
          'index' : True,
          'facet' : False},

          {'name'  : 'comment_focus_type',
          'type'  : 'string',
          'index' : False,
          'facet' : False},

          {'name'  : 'comment_created_at_unix',
          'type'  : 'int64',
          'index' : False,
          'facet' : False},

          {'name'  : 'img_url',
          'type'  : 'string',
          'index' : False,
          'optional' : True
          },

          {'name'  : 'has_img_url',
          'type'  : 'bool',
          'index' : True
          }

          # {'name' : 'embedding',
          # 'type' : 'float[]',
          # 'embed': {
          #     'from': ['comment_body'],
          #     'model_config': {
          #       # https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2
          #         # 'model_name': 'ts/all-MiniLM-L12-v2'
          #         'model_name': 'ts/e5-small-v2',
          #         # this one requires...
          #         "indexing_prefix": "passage:",
          #         "query_prefix": "query:"
          #         }
          #     }
          # }
      ],

      # 'default_sorting_field' : 'comment_created_at_unix',
      'default_sorting_field' : 'comment_id',
  }


if __name__ == '__main__':

  client = typesense.Client({
    'nodes': [{
      'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
      'port': '8108',      # For Typesense Cloud use 443
      'protocol': 'http'   # For Typesense Cloud use https
    }],
    'api_key': 'xyz',
    'connection_timeout_seconds': 20
  })

  collections = client.collections.retrieve()
  if 'comments' in [collection['name'] for collection in collections]:
    client.collections['comments'].delete()
  client.collections.create(SCHEMA)

  # json_loc = '/Users/user/repos/zoo_search/data/gz_talk_export_1000comments.jsonl'
  # json_loc = '/Users/user/repos/zoo_search/data/gz_talk_export.jsonl'
  # json_loc = '/Users/user/repos/zoo_search/data/gz_talk_export_imgurls.jsonl'
  json_loc = '/Users/user/repos/zoo_search/data/gz_talk_export_imgurls_bool.json'
  with open(json_loc) as jsonl_file:
    client.collections['comments'].documents.import_(jsonl_file.read().encode('utf-8'), {'action': 'upsert'})
