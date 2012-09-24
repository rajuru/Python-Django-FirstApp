from django.template import RequestContext

def custom_context(request):
  return {
    'AUTHOR': 'The HungryCoder',
    'AUTHOR_URL': 'http://thehungrycoder.com'
  }