import gzip
import json

england_text = ''

with gzip.open('./jawiki-country.json.gz', 'rt') as file:
  for line in file:
    article_json = json.loads(line)
    if article_json['title'] == 'イギリス':
      england_text = article_json['text']
      break

with open('./england_text.txt', mode='w') as file:
  file.write(england_text)