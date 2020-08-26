import requests as req
from bs4 import BeautifulSoup as bs
import urllib.parse as urllib
import webbrowser 
import random

URL = "https://www.assisi-ni.org/wp-admin/admin-ajax.php"
PAYLOAD = {
        "action" : "jet_engine_elementor", 
        "handler" : "listing_load_more", 
        "query[post_status][]":"publish",
        "query[post_type]":"animals", 
        "query[posts_per_page]":6,
        "query[paged]":1,
        "query[suppress_filters]":"false",
        "query[jet_smart_filters]":"jet-engine/default",
        "widget_settings[lisitng_id]":3474,
        "widget_settings[posts_num]":6, 
        "page":1}


ANIMAL_PARAMETRES = {
    "query[meta_query][0][key]" : "type",
    "query[meta_query][0][value]" : "Dog"
}


HEADERS = {
  'authority': 'www.assisi-ni.org',
  'Content-type': 'application/json',
  'x-requested-with': 'XMLHttpRequest',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://www.assisi-ni.org',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'referer': 'https://www.assisi-ni.org/',
}

def addSearchParametres(animal):
    if (animal != None):
        PAYLOAD.update(ANIMAL_PARAMETRES)
        PAYLOAD["query[meta_query][0][value]"] = animal
        

def getListOfAnimals(animal):
    addSearchParametres(animal)
    listOfAnimals = []
    pageNumber = 1
    resultsLength = 99
    while(resultsLength > 0):
        PAYLOAD['page']=pageNumber
        page = req.post(URL, headers=HEADERS, data = urllib.urlencode(PAYLOAD))
        response = page.json()
        soup = bs(response["data"]["html"], 'html.parser')
        results = soup.findAll('a')
        resultsLength = len(results)
        for i in range(1, resultsLength, 2):
            listOfAnimals.append(results[i]['href'])
        pageNumber+=1
    return listOfAnimals
   

def getMyBestFriend(animal = None):
    listOfAnimals = getListOfAnimals(animal)
    lent = len(listOfAnimals)
    randomInt = random.randint(0, lent-1)
    return listOfAnimals[randomInt]
