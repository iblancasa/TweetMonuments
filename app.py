#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form
from web.contrib.template import render_mako
import tweepy
import datetime
import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)


urls = (
        '/(.*)','index'
        )

app = web.application(urls, globals(), autoreload=False)

render = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )


contadorAlhambra=0


def recalcular():
    global contadorAlhambra
    tweets = api.search(q='Alhambra', until=str(datetime.date.fromordinal(datetime.date.today().toordinal()-1)),count=1)
    tweetAyer = tweets[0].id
    tweets = api.search(q='Alhambra',since_id=tweetAyer)
    contadorAlhambra=0
    for tweet in tweets:
        contadorAlhambra+=1



class index:
    def GET(self, name):
        global contadorAlhambra
        recalcular()
        return render.index(tweets=contadorAlhambra)



if __name__ == "__main__":
    app.run()
