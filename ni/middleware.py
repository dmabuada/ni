"""
Gather some data on the request for kibana.
TODO: make this async
"""

from time import time
from logging import getLogger


def get_client_ip(request):
    """
    :param request: request object
    :return: the remote address, either x-forwarded-for or the remote_address
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR', None)
    return ip_address


class LoggingMiddleware(object):
    """
    On each request, gather some basic information and ship to logstash
    """
    def __init__(self):
        self.logger = getLogger('ni')

    # pylint: disable=no-self-use
    def process_request(self, request):
        """
        begin a timer
        :param request:
        :return:
        """
        request.timer = time()
        return None

    # pylint: disable=no-self-use
    def process_response(self, request, response):
       """
        :param request:
        :param response:
        :return: Logs some basic data on the request and returns the response
        """
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

