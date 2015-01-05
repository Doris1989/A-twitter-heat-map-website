
from tastypie.resources import ModelResource
from mysite.models import Tweet
from tastypie.constants import ALL

class EntryResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Tweet.objects.all()
        filtering = {'kwd': ALL}
        resource_name = 'tweet'
    
