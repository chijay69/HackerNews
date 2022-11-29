# testing hacker news api
import json
import urllib.request as urllib2

response = urllib2.urlopen('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
html = response.read()
print(html)

base_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'

top_story_ids = json.loads(html)
for story in top_story_ids:
    response = urllib2.urlopen(base_url.format(story))
    print(response.read())
