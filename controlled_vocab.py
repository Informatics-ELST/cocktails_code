import json
#from vodka_spider import *
import tutorial
#from spiders import *

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
