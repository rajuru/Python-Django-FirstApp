from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll
from django.http import HttpResponse
from django.http import Http404

def index(request):
  latest_polls_list = Poll.objects.all().order_by('-pub_date')[:5]

  return render_to_response('polls/index.html', {'latest_poll_list': latest_polls_list})



def detail(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)

  return HttpResponse("You are looking for Poll %s" % poll_id)