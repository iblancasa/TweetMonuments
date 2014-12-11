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



html=""
grafico=""
ultimavez=datetime.datetime.now()

def generarMonumento(busqueda,etiqueta):
    global html
    tweets = api.search(q=busqueda, until=str(datetime.date.fromordinal(datetime.date.today().toordinal()-1)),count=1)
    tweetAyer = tweets[0].id
    tweets = api.search(q=busqueda,since_id=tweetAyer)

    primero=tweets[0].created_at
    ultimo=penultimo=primero

    html+="<section class=\"monumento\" id=\""+etiqueta+"\">\n"

    contador =0

    for tweet in tweets:
        penultimo=ultimo
        ultimo=tweet.created_at
        url="https://twitter.com/"+ tweet.author.screen_name+"/status/"+str(tweet.id)
        html+="\t<article class=\"tweet\"> <span class=\"autor\"><a href=\""+url+"\">"+tweet.author.name+"</a></span>\n"
        html+="\t\t<p class=\"texto\">"+tweet.text+"</p>\n\t</article>\n"
        contador+=1

    html+="</section>\n"

    diferencia=primero-penultimo
    diferencia=diferencia.days * 86400+diferencia.seconds *60
    if diferencia>0:
        dato=float(float(600)/(float(diferencia)/float(contador)))
        print dato
        return dato
    else:
        return 0


def recalcularTodo():
    global html
    global grafico
    html=""

    contadorAlhambra=generarMonumento("alhambra","alhambra")
    contadorGiralda=generarMonumento("giralda","giralda")
    contadorSagrada=generarMonumento("sagrada familia","sagradafamilia")
    contadorMezquita=generarMonumento("mezquita cordoba","mezquitacordoba")
    contadorPuertaAlcala=generarMonumento("puerta alcala","puertaalcala")

    grafico="  $(function () {\
        $('#container').highcharts({\
            chart: {\
                type: 'bar',\
                height: 250, \
                backgroundColor:'#EBECFF'\
            },\
            title: {\
                text: 'En Twitter se habla de...'\
            },\
            xAxis: {\
                categories: ['Lugares turisticos']\
            },\
            yAxis: {\
                title: {\
                    text: 'Estimacion de la media de tweets en 10 min'\
                }\
            },\
            series: [{\
                name: 'Alhambra',\
                data: ["+str(contadorAlhambra)+"]\
            },{\
                name: 'Giralda',\
                data: ["+str(contadorGiralda)+"]\
            },{\
                name: 'Sagrada Familia',\
                data: ["+str(contadorSagrada)+"]\
            },{\
                name: 'Mezquita de Cordoba',\
                data: ["+str(contadorMezquita)+"]\
            },{\
                name: 'Puerta de Alcala',\
                data: ["+str(contadorPuertaAlcala)+"]\
            }\
            ]\
        });\
        });"




class index:
    def GET(self, name):
        global html
        global grafico
        global ultimavez

        if datetime.datetime.now()-ultimavez>datetime.timedelta(minutes=10):
            recalcularTodo()
            print "He recalculado"
            ultimavez=datetime.datetime.now()
        else:
            print "Nada, todo esta calculado"
        return render.index(html=html,grafico=grafico)



if __name__ == "__main__":
    recalcularTodo()
    app.run()
