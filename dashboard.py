import requests
import json
import webbrowser
#from controlled_vocab import *
from rapidproto import *

selected = -1
while selected != int(0):
    print("Please specify how you would like search for a drink:")
    print("1 : Cocktail Name")
    print("2 : Ingredient Name")
    print("3 : Glass Name")
    print("0 : Exit program")

    selected = input()

        # Function selector (there's probably a better way of doing this)
    if(selected == "1"):
        cocktailname()
    elif(selected == "2"):
        #ingredientname()
        choose_ingredient()
    elif selected == "3":
        print("Add glasses code")
    elif selected == "0":
        pass
    else:
        (print("Incorrect submission"))
