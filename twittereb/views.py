from django.shortcuts import render,redirect
from .models import tw_tweet
from datetime import datetime
from django.urls import reverse
# Create your views here.

def home(request):
    all_tweets = tw_tweet.objects.filter(parent_tweet_id = None)
    for tweet in all_tweets:
        tweet.count = tw_tweet.objects.filter(parent_tweet_id = tweet.id).count()
    return render(request, 'home.html', {'tweets':all_tweets})

def post(request):
    if request.POST:
        name = request.POST['name']
        text = request.POST['text']
        fileitem = request.FILES.get('img', None)
        if fileitem:     
            with open('twittereb/static/userimage/' + str(fileitem), 'wb+') as destination:
                for chunk in fileitem.chunks():
                    destination.write(chunk)
            imageurl = 'userimage/' + str(fileitem)

        else:
            imageurl=None
        new_tweet = tw_tweet(name=name, text= text,created_at=datetime.now(), image_path=imageurl )
        new_tweet.save()
        return redirect(reverse('home'))

    return render(request, 'post-tweet.html',{})


def detail(request,id):
    tweet = tw_tweet.objects.get(id=id)
    replies = tw_tweet.objects.filter(parent_tweet_id = id)

    return render(request, 'tweet-detail.html', {'tweet':tweet,'replies':replies})

def reply(request,id):
    tweet = tw_tweet.objects.get(id=id)
    if request.POST:
        name = request.POST['name']
        text = request.POST['text']
        fileitem = request.FILES.get('img', None)
        if fileitem:     
            with open('twittereb/static/userimage/' + str(fileitem), 'wb+') as destination:
                for chunk in fileitem.chunks():
                    destination.write(chunk)
            imageurl = 'userimage/' + str(fileitem)

        else:
            imageurl=None

        new_reply = tw_tweet(name=name, text=text,created_at=datetime.now(), parent_tweet_id =id,image_path = imageurl)
        new_reply.save()
        return redirect(reverse('home'))
    return render(request, 'reply.html', {'tweet':tweet})
