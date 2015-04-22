import json

from django.http import HttpResponse


def ping(request):
    response_data = {}
    response_data['result'] = 'in the pushup position'
    response_data['message'] = 'dogs are always'
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
