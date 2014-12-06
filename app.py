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
        if contador < 6:
            html+="\t<article class=\"tweet\"> <span class=\"autor\">"+tweet.author.name+"</span>\n"
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
    contadorMuseoCiencias=generarMonumento("museo artes ciencias","museoartesciencias")
    contadorPuertaAlcala=generarMonumento("puerta alcala","puertaalcala")

    grafico="  $(function () {\
        $('#container').highcharts({\
            chart: {\
                type: 'bar'\
            },\
            title: {\
                text: 'Fruit Consumption'\
            },\
            xAxis: {\
                categories: ['Sitios turisticos']\
            },\
            yAxis: {\
                title: {\
                    text: 'Tweets por sitio'\
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
                name: 'Museo de las Artes y las Ciencias',\
                data: ["+str(contadorMuseoCiencias)+"]\
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
        recalcularTodo()
        return render.index(html=html,grafico=grafico)



if __name__ == "__main__":
    app.run()
