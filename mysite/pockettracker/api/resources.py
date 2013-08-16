from tastypie.resources import ModelResource
from pockettracker.models import pocketdata

class MyModelResource(ModelResource):
  class Meta:
    queryset = pocketdata.objects.all()
    allowed_methods = ['get']


