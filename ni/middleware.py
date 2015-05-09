from time import time
from logging import getLogger


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class LoggingMiddleware(object):
    def __init__(self):
        self.logger = getLogger('ni')

    def process_request(self, request):
        request.timer = time()
        return None

    def process_response(self, request, response):
        # TODO: more data here
        extra = {
            'execution_time': time() - request.timer,
            'method': request.method,
            'path': request.get_full_path(),
            'user_agent': request.META['HTTP_USER_AGENT'],
            'resolver_match': request.resolver_match._func_path,
            'url_name': request.resolver_match.url_name,
            'user': str(request.user),
            'remote_address': request.META.get('REMOTE_ADDR'),
            'x-forwarded-for': request.META.get('HTTP_X_FORWARDED_FOR'),
            'session_id': request.session._session_key
        }

        self.logger.info(
            '[%s] %s (%.1fs)',
            response.status_code,
            request.get_full_path(),
            time() - request.timer,
            extra=extra)
        return response
