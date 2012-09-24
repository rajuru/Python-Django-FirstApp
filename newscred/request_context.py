from django.template import RequestContext

def custom_context(request):
  return {
    'author': 'The HungryCoder',
    'author_url': 'http://thehungrycoder.com'
  }