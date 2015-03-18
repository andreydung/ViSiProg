from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from interface.models import Trial, TrialLLNL2, TrialLLNL3, TrialCOLOR, TrialBuilding
from django.contrib.auth.models import User
from django.template import RequestContext
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.conf import settings

def validateGroup(value):
    groups = value.split(",end,")[:-1]
    for g in groups:
        numbers = g.split(",")
        if len(numbers) != 9:
            raise ValidationError("Wrong number of image per each group!!", code = 'invalid')
    
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
        groups_page(request)

    return render_to_response('interface/test.html',\
                    context_instance=RequestContext(request))

def groups_page(request, theusername = ""):
    if theusername:
        userid = User.objects.get(username=theusername).pk
    else:
        userid = request.user.id

    trials = Trial.objects.filter(subject_id = userid).order_by('-time')
    lastgroups = []
    for t in trials:
        tmp = t.group.split(',end,')[-2]
        lastgroup = [settings.LISTGOOGLE[int(c)] for c in tmp.split(",")]
        lastgroups.append(lastgroup)

    return render_to_response('interface/groups.html',\
                    {'groups': lastgroups, 'imagepath': settings.IMAGEPATH},\
                    context_instance=RequestContext(request))

# ============================= LLNL2 =========================================
@ensure_csrf_cookie
@login_required
def test_page_LLNL2(request):
    if request.method == "POST":
        newgroup = request.POST["group"]
        validateGroup(newgroup)

        t = TrialLLNL2(group = newgroup, time = timezone.now(), subject = request.user)
        t.save()
        groups_page_LLNL2(request)

    return render_to_response('interface/testLLNL2.html',\
                    context_instance=RequestContext(request))

def groups_page_LLNL2(request, theusername = ""):
    if theusername:
        userid = User.objects.get(username=theusername).pk
    else:
        userid = request.user.id

    trials = TrialLLNL2.objects.filter(subject_id = userid).order_by('-time')
    lastgroups = []
    for t in trials:
        tmp = t.group.split(',end,')[-2]
        lastgroup = [settings.LISTLLNL2[int(c)] for c in tmp.split(",")]
        lastgroups.append(lastgroup)

    return render_to_response('interface/groups.html',\
                    {'groups': lastgroups, 'imagepath': settings.LLNL2PATH},\
                    context_instance=RequestContext(request))


# ============================= LLNL3 =========================================
@ensure_csrf_cookie
@login_required
def test_page_LLNL3(request):
    if request.method == "POST":
        newgroup = request.POST["group"]
        validateGroup(newgroup)

        t = TrialLLNL3(group = newgroup, time = timezone.now(), subject = request.user)
        t.save()
        groups_page_LLNL3(request)

    return render_to_response('interface/testLLNL3.html',\
                    context_instance=RequestContext(request))

def groups_page_LLNL3(request, theusername = ""):
    if theusername:
        userid = User.objects.get(username=theusername).pk
    else:
        userid = request.user.id

    trials = TrialLLNL3.objects.filter(subject_id = userid).order_by('-time')
    lastgroups = []
    for t in trials:
        tmp = t.group.split(',end,')[-2]
        lastgroup = [settings.LISTLLNL3[int(c)] for c in tmp.split(",")]
        lastgroups.append(lastgroup)

    return render_to_response('interface/groups.html',\
                    {'groups': lastgroups, 'imagepath': settings.LLNL3PATH},\
                    context_instance=RequestContext(request))


# ============================= Color =========================================
@ensure_csrf_cookie
@login_required
def test_page_COLOR(request):
    if request.method == "POST":
        newgroup = request.POST["group"]
        validateGroup(newgroup)

        t = TrialCOLOR(group = newgroup, time = timezone.now(), subject = request.user)
        t.save()
        groups_page_COLOR(request)

    return render_to_response('interface/testCOLOR.html',\
                    context_instance=RequestContext(request))

def groups_page_COLOR(request, theusername = ""):
    if theusername:
        userid = User.objects.get(username=theusername).pk
    else:
        userid = request.user.id

    trials = TrialCOLOR.objects.filter(subject_id = userid).order_by('-time')
    lastgroups = []
    for t in trials:
        tmp = t.group.split(',end,')[-2]
        lastgroup = [settings.LISTCOLOR[int(c)] for c in tmp.split(",")]
        lastgroups.append(lastgroup)

    return render_to_response('interface/groups.html',\
                    {'groups': lastgroups, 'imagepath': settings.COLORPATH},\
                    context_instance=RequestContext(request))

# ============================= Buildings =========================================
@ensure_csrf_cookie
@login_required
def test_page_Building(request):
    if request.method == "POST":
        newgroup = request.POST["group"]
        validateGroup(newgroup)

        t = TrialBuilding(group = newgroup, time = timezone.now(), subject = request.user)
        t.save()
        groups_page_Building(request)

    return render_to_response('interface/testBuilding.html',\
                    context_instance=RequestContext(request))

def groups_page_Building(request, theusername = ""):
    if theusername:
        userid = User.objects.get(username=theusername).pk
    else:
        userid = request.user.id

    trials = TrialBuilding.objects.filter(subject_id = userid).order_by('-time')
    lastgroups = []
    for t in trials:
        tmp = t.group.split(',end,')[-2]
        lastgroup = [settings.LISTBUILDING[int(c)] for c in tmp.split(",")]
        lastgroups.append(lastgroup)

    return render_to_response('interface/groups.html',\
                    {'groups': lastgroups, 'imagepath': settings.BUILDINGPATH},\
                    context_instance=RequestContext(request))