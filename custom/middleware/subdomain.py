import tldextract
from django.http import HttpResponseRedirect
import urllib


class SubDomain:
  def process_request(self, request):
    url_parts = tldextract.extract(request.META.get('HTTP_HOST'))
    keyword = url_parts.subdomain.lstrip('www.').replace('-',' ')
    if keyword:
      return HttpResponseRedirect('http://127.0.0.1:8000/topics/?q=%s' %  keyword)
