from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from interface.models import Trial
from django.template import RequestContext
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone
from django.http import HttpResponseRedirect

# def validateGroup(value):
#     try:
#         a = [int(s) for s in value.lsplit().split(" ")]
#         print a
#         if len(a) != 9:
#             raise ValidationError("Wrong number of entries in group")
#     except ValidationError, err:
#         raise err


# Create your views here.
@login_required
def interface_page(request):
    return render(request, 'interface/index.html')

@ensure_csrf_cookie
@login_required
def test_page(request):
    if request.method == "POST":
        newgroup = request.POST["group"]
        print "Received result"
        # assert validateGroup(newgroup)
        t = Trial(group = newgroup, time = timezone.now(), subject = request.user)
        t.save()
        return HttpResponseRedirect()

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

