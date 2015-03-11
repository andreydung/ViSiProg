from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from interface.models import Trial
from django.template import RequestContext
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone
from django.http import HttpResponseRedirect

def validateGroup(value):
    groups = value.split(",end,")[:-1]
    for g in groups:
        numbers = g.split(",")
        if len(numbers) != 9:
            raise Exception("Wrong number of image per each group!!")
    
# Create your views here.
@login_required
def interface_page(request):
    return render(request, 'interface/index.html')

@ensure_csrf_cookie
@login_required
def test_page(request):
    if request.method == "POST":
        newgroup = request.POST["group"]
        validateGroup(newgroup)

        t = Trial(group = newgroup, time = timezone.now(), subject = request.user)
        t.save()
        return HttpResponseRedirect('/interface/groups/')

    return render_to_response('interface/test.html',\
                    context_instance=RequestContext(request))

@login_required
def groups_page(request):
    trials = Trial.objects.filter(subject_id = request.user.id).order_by('-time')
    lastgroups = []
    for t in trials:
        tmp = t.group.split(',end,')[-2]
        lastgroup = [settings.LISTIMAGE[int(c)] for c in tmp.split(",")]
        lastgroups.append(lastgroup)

    return render_to_response('interface/groups.html',\
                    {'groups': lastgroups, 'imagepath': settings.IMAGEPATH},\
                    context_instance=RequestContext(request))

