from time import time
from logging import getLogger


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', None)
    return ip


class LoggingMiddleware(object):
    def __init__(self):
        self.logger = getLogger('ni')

    def process_request(self, request):
        request.timer = time()
        return None

    def process_response(self, request, response):
        # return response
        # TODO: more data here
        extra = {
            'execution_time': time() - request.timer,
            'method': request.method,
            'path': request.get_full_path(),
            'user_agent': request.META.get('HTTP_USER_AGENT'),
            'remote_address': request.META.get('REMOTE_ADDR'),
            'x-forwarded-for': request.META.get('HTTP_X_FORWARDED_FOR'),
        }

        if hasattr(request.resolver_match, '_func_path'):
            extra['resolver_match'] = request.resolver_match._func_path,

        if hasattr(request.resolver_match, 'url_name'):
            extra['resolver_match'] = request.resolver_match.url_name,

        if hasattr(request, 'user'):
            extra['user'] = str(request.user)

        if hasattr(request, 'session'):
            extra['session_id'] = request.session._session_key

        self.logger.info(
            '[%s] %s (%.1fs)',
            response.status_code,
            request.get_full_path(),
            time() - request.timer,
            extra=extra)
        return response
