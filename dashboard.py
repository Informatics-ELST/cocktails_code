import requests
import json
import webbrowser
from controlled_vocab import *
from rapidproto import *

def dashboard():
    print("Please specify how you would like search for a drink:")
    print("1 : Cocktail Name")
    print("2 : Ingredient Name")

    selected = input()
    if(selected == "1"):
        cocktailname()
    if(selected == "2"):
        ingredientname()
    else:
        dashboard()

dashboard()
