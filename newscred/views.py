from newscred.models import Topic, Fetch
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.cache import cache_page

from django.contrib.auth.forms import PasswordChangeForm
from bootstrap.forms import BootstrapMixin, Fieldset
from django.http import HttpResponse
from django.template import RequestContext

def augment_topic(topic):
  """
    Merge the topic data that are present in database with the topic object
  """

  try:
    cached_topic = Topic.objects.get(guid=topic['guid'])
    topic['name'] = cached_topic.name
    topic['augmented'] = True
  finally:
    return topic


def index(request):
  topics = []
  query = request.GET.get('q', '')

  if query:
    fetcher = Fetch()
    topics = fetcher.get_topics(query)

    if topics:
      #check if the topic is present in db
      for index, topic in enumerate(topics):
        topics[index] = augment_topic(topic)


  return render_to_response('newscred/index.html', {'q': query, 'topics': topics})

#@cache_page(60 * 10)
def detail(request, topic_guid):
  fetcher = Fetch()
  topic = fetcher.get_topic(topic_guid)
  images = fetcher.get_images(topic_guid)
  related_topics = fetcher.get_related_topic(topic_guid)
  return render_to_response('newscred/detail.html', {'topic': topic, 'images': images, 'related_topics': related_topics}, context_instance=RequestContext(request))

def update(request, topic_guid):
  fetcher = Fetch()
  topic_info = fetcher.get_topic(topic_guid)

  #merge the edited on with the fetched one
  topic_info['name'] =  request.POST['topic_title']
  topic = Topic(name=topic_info['name'], topic_group=topic_info['topic_group'], description=topic_info['description'],guid=topic_guid)
  topic.save()

  return HttpResponse(True)






