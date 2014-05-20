<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader

from polls.models import Poll

# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 4da71ad7af025505fafd1edca6cdd2e71717b09e
