import json
#from vodka_spider import *
import tutorial
#from spiders import *
from rapidproto import *


def vodka_cv(user_ingredient):
    with open('tutorial/vodka.json', 'r') as myfile:
        data=myfile.read()

    myfile.close()

    obj = json.loads(data)

    #vodka_list = [str(obj['vodka brand'])]
    #print (vodka_list)
    #print(obj)

    vodka_list = []
    for pair in obj:
        #print(pair["vodka_brand"])
        vodka_list.append((pair["vodka_brand"]).lower())

    #print(vodka_list)

    if user_ingredient.lower() in vodka_list:
        return ["vodka"]
    else:
        return [user_ingredient]

def whisky_cv(user_ingredient):

    #############################
    #NEED TO ADD BRANDS!!!!!!!!!#
    #############################
    
    #user_ingredient = user_ingredient.lower()
    whisky_list = ["scotch", "whisky", "blended whisky", "single malt",
                   "whiskey", "blended whiskey", "irish whiskey"] #any more to add?

    if user_ingredient.lower() in whisky_list:
        """ingredientname("Scotch")
        ingredientname("Blended Whiskey")
        ingredientname("Whiskey")"""
        #add all other whisky types from db to this list bellow
        return ["Scotch", "Blended whiskey", "Whiskey", "Irish whiskey"]

    else:
        return [user_ingredient]

def gin_cv(user_ingredient):
    with open('tutorial/gin.json', 'r') as myfile:
        data=myfile.read()

    myfile.close()

    obj = json.loads(data)

    #gin_list = [str(obj['gin brand'])]
    #print (gin_list)
    #print(obj)

    gin_list = []
    for pair in obj:
        #print(pair["gin_brand"])
        gin_list.append((pair["gin_brand"]).lower())

    #print(gin_list)

    if user_ingredient.lower() in gin_list:
        return ["gin"]
    else:
        return [user_ingredient]

def rum_cv(user_ingredient):
    with open('tutorial/rum.json', 'r') as myfile:
        data=myfile.read()

    myfile.close()

    obj = json.loads(data)

    #rum_list = [str(obj['rum brand'])]
    #print (rum_list)
    #print(obj)

    rum_list = []
    for pair in obj:
        #print(pair["rum_brand"])
        rum_list.append((pair["rum_brand"]).lower())

    #print(rum_list)

    if user_ingredient.lower() in rum_list:
        return ["rum"]
    else:
        return [user_ingredient]
        




