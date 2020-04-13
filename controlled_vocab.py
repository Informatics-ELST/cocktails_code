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
        return "vodka"
    else:
        return user_ingredient

def whisky_cv(user_ingredient):
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
        return user_ingredient
        




