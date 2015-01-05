from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render
from mysite.models import Tweet
#from twittmap.models import convertstof
from django.http import HttpResponse
from django.core.context_processors import request
from datetime import datetime, timedelta, date
import simplejson as json
import tweepy
import django.db as jdb
from tweepy.utils import import_simplejson

def index(request):
     #return HttpResponse('Templates/index.html',locals(),context_instance = RequestContext(request))
      return render(request, 'static/index.html')

def search_twitter(data, kkwd):   

    #filter it all
#     print data
    tweets = []
    try:
            
            user = data.id
            tid = data.user.id
            geo = data.coordinates
            text = data.text
            ts = data.created_at 
            time = data.created_at#datetime.strptime(data.created_at,'%a %b %d %H:%M:%S +0000 %Y')

    except AttributeError:
        return
    
    if geo is not None and text is not None and tid is not None and time is not None and user is not None:
     
        try:
            p = Tweet(
                      user = data.id,
                      tid = data.user.id,
                      lat = data.coordinates['coordinates'][0],
                      lon = data.coordinates['coordinates'][1],
                      text = data.text,
                      time = data.created_at,#datetime.strptime(data.created_at,'%a %b %d %H:%M:%S +0000 %Y'),
                      kwd = kkwd,
                      )
            p.save()
        except jdb.OperationalError:
            return
 
def crawl(request):

    CONSUMER_KEY = 'wfg76HPo6k56ItgdRCepxAvch'
    CONSUMER_SECRET = 'xn6PZNNO7ieGQgHfcuuAUiCTZMJtnExgtWyXcJK1G1EbssloXx'
    ACCESS_TOKEN_KEY = '43335008-tl7cFjjCOgEEukxlMBt1izBjKjKxrFIEfinonvohm'
    ACCESS_TOKEN_SECRET = 'YF3IZM5Xr7o8PkMZai6lHCTeNwbsEkWY7WrUUpQY3Iaxi'
    
    kkwd = request.GET.get('kwd');
    
    auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth1.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    
   
    api = tweepy.API(auth1)
    data = api.search(q=kkwd, lang='en', count=1000000)
    print data
    for d in data:
        search_twitter(d, kkwd)
    
    return HttpResponse('Done!')
 