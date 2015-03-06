from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def interface_page(request):
    return render(request, 'interface/index.html')

@login_required
def test_page(request):
    return render_to_response('interface/test.html')

@login_required
def groups_page(request):
    return render_to_response('interface/group.html')