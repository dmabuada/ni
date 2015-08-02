"""
Base model used for user shops.
"""

import logging
import datetime

from django.contrib.sites.models import Site
from django.core import urlresolvers
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from satchmo_utils.unique_id import slugify

log = logging.getLogger('ni.shops')


class Shop(models.Model):
    """
    Root class for all Shops
    """
    site = models.ForeignKey(Site, verbose_name=_('Site'))
    owner = models.ForeignKey(User, verbose_name=_('Owner'))
    name = models.CharField(_("Name of shop"), max_length=255, blank=False,
                            help_text=_(
                                "This is what the shop will be called in the default site language. To add non-default translations, use the Product Translation section below."))
    slug = models.SlugField(_("Shop slug"), blank=True,
                            help_text=_(
                                "Used for URLs, auto-generated from name if blank"),
                            max_length=255)
    short_description = models.TextField(_("Short description of shop"),
                                         help_text=_(
                                             "This should be a 1 or 2 line description in the default site language for use in product listing screens"),
                                         max_length=200, default='', blank=True)
    description = models.TextField(_("Description of shop"), help_text=_(
        "This field can contain HTML and should be a few paragraphs in the default site language explaining the background of the shop."),
                                   default='', blank=True)
    meta = models.TextField(_("Meta Description"), max_length=200, blank=True,
                            null=True,
                            help_text=_("Meta description for this shop"))
    date_added = models.DateField(_("Date added"), null=True, blank=True)
    active = models.BooleanField(_("Active"), default=True, help_text=_(
        "This will determine whether or not this shop will appear on the homepage"))
    featured = models.BooleanField(_("Featured"), default=False, help_text=_(
        "Featured items will show on the front page"))
    ordering = models.IntegerField(_("Ordering"), default=0, help_text=_(
        "Override alphabetical order in category display"))

    # objects = ProductManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return urlresolvers.reverse('ni_shops',
                                    kwargs={'product_slug': self.slug})

    class Meta:
        ordering = ('site', 'ordering', 'name')
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")
        unique_together = (('site', 'name'), ('site', 'slug'))

    def save(self, **kwargs):
        if not self.pk:
            self.date_added = datetime.date.today()

        if self.name and not self.slug:
            self.slug = slugify(self.name, instance=self)

        super(Shop, self).save(**kwargs)
