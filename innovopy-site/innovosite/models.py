from __future__ import unicode_literals

from django.db import models
from core.models import DocumentFile


class Innovosite(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    documents = models.ManyToManyField(DocumentFile, related_name='site_documents', blank=True)

    def get_absolute_url(self):
        return reverse('innovosite', args=[self.id])

    def __unicode__(self):
        return self.name


class SubOrganization(models.Model):
    name = models.CharField(max_length=256)
    org_type = models.CharField(max_length=48)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    org_site = models.ForeignKey(Innovosite, related_name = 'suborganizations')
    org_parent = models.ForeignKey('SubOrganization', null=True, blank=True)

    documents = models.ManyToManyField(DocumentFile, related_name='organization_documents')
    
    def get_absolute_url(self):
        return reverse('unit', args=[self.id])

    def __unicode__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=48, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    building_site = models.ForeignKey(Innovosite)

    documents = models.ManyToManyField(DocumentFile, related_name='building_documents')
    
    def get_absolute_url(self):
        return reverse('building', args=[self.id])

    def __unicode__(self):
        return self.name






















