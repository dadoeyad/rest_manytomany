from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Property(models.Model):
    friendly_name = models.CharField(_('Friendly name'), max_length=200)
    date_added = models.DateTimeField(default=timezone.now())
    images = models.ManyToManyField('PropertyImage')

    class Meta:
        ordering = ['-date_added', 'friendly_name']
        verbose_name_plural = 'Properties'

    def __unicode__(self):
        return self.friendly_name


class PropertyImage(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    image_file = models.ImageField(_('Name'))

    def __unicode__(self):
        return self.name
