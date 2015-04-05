from django.shortcuts import render_to_response
from django.template import RequestContext

def index_page(request):
    ctx = RequestContext(request, {})
    return render_to_response('index.html', ctx)