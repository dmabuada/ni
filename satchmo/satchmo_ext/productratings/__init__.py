from django_comments.models import Comment
from django_comments.signals import comment_will_be_posted
from django_comments.signals import comment_was_posted

from listeners import *

comment_was_posted.connect(save_rating, sender=Comment)
comment_was_posted.connect(one_rating_per_product, sender=Comment)
comment_was_posted.connect(check_with_akismet, sender=Comment)

