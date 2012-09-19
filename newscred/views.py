from newscred.models import Topic, Fetch
from django.shortcuts import render_to_response, get_object_or_404
import urllib2
import json
from django.views.decorators.cache import  cache_page


def fetch_topics(query):
  if query:
    response = urllib2.urlopen(
      'http://api.newscred.com/topics?access_key=c4bcc3f7c9bf9ec159f51da0a86ca658&query=%s&format=json' % query)
    data = response.read()
    jsonData = json.loads(data)
    return jsonData['topic_set']


def index(request):
  topics = []
  query = request.GET.get('q', '')

  if query:
    fetcher = Fetch()
    topics = fetcher.get_topics(query)

  return render_to_response('newscred/index.html', {'q': query, 'topics': topics})

@cache_page(60 * 10)

def detail(request, topic_guid):
  fetcher = Fetch()
  topic = fetcher.get_topic(topic_guid)
  images = fetcher.get_images(topic_guid)
  related_topics = fetcher.get_related_topic(topic_guid)
  return render_to_response('newscred/detail.html', {'topic': topic, 'images': images, 'related_topics': related_topics})

