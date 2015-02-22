import satchmo_json

from django.http import HttpResponse


def ping(request):
    response_data = {}
    response_data['result'] = 'test'
    response_data['message'] = 'test'
    return HttpResponse(satchmo_json.dumps(response_data), content_type="application/json")