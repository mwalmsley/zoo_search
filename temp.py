import json

if __name__ == '__main__':
    f_in = open('/Users/user/repos/zoo_search/data/gz_talk_export_imgurls.jsonl', 'r')
    f_out = open('/Users/user/repos/zoo_search/data/gz_talk_export_imgurls_bool.json', 'w')
    for line in f_in:
        d = json.loads(line)
        url = d.get('img_url')
        if url is None or url == "":
            d['has_img_url'] = False
        else:
            d['has_img_url'] = True
            if isinstance(url, list):
                url = url[0]
            assert isinstance(url, str)
            if not len(url) > 10:
                raise ValueError(url)
        f_out.write(json.dumps(d) + '\n')