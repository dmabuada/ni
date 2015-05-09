from time import time
from logging import getLogger


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
        }

        self.logger.info(
            '[%s] %s (%.1fs)',
            response.status_code,
            request.get_full_path(),
            time() - request.timer,
            extra=extra)
        return response
