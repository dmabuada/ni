"""
Allow Satchmo to use an email address instead of the user id as the
primary id
Taken from a posting on the Django mailing list.
Thanks to Vasily Sulatskov for sending this to the list.
"""

import re

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

EMAIL_RE = re.compile(
    # dot-atom
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"

    # quoted-string
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"'

    # domain
    r')@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$', re.IGNORECASE)


class EmailBackend(ModelBackend):
    """Authenticate using email only"""

    def authenticate(self, username=None, password=None, **kwargs):
        # If username is an email address, then try to pull it up
        if EMAIL_RE.search(username):
            # pylint: disable=no-member
            user = User.objects.filter(email__iexact=username)
            if user.count() > 0:
                user = user[0]
                if user.check_password(password):
                    return user
        return None
