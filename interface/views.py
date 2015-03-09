from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from interface.models import Trial
from django.template import RequestContext
from django.conf import settings

# Create your views here.
@login_required
def interface_page(request):
    return render(request, 'interface/index.html')

@login_required
def test_page(request):
    return render_to_response('interface/test.html',\
                    context_instance=RequestContext(request))

@login_required
def groups_page(request):
    trials = Trial.objects.filter(subject_id = request.user.id)
    lastresult = []
    for t in trials:
        tmp = [settings.LISTIMAGE[int(c)] for c in t.group.split(" ")][-9:]
        lastresult.append(tmp)

    return render_to_response('interface/groups.html',\
                    {'groups': lastresult, 'imagepath': settings.IMAGEPATH},\
                    context_instance=RequestContext(request))