import json

from django.http import HttpResponse

def ping(request):
    response_data = {}
    response_data['result'] = 'dogs are always'
    response_data['message'] = 'in the pushup position'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
