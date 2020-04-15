import requests
import json
import webbrowser
from controlled_vocab import *
from rapidproto import *

def dashboard():
    print("Please specify how you would like search for a drink:")
    print("1 : Cocktail Name")
    print("2 : Ingredient Name")
    print("3 : Surprise Me!")


    selected = input()
    if(selected == "1"):
        cocktailname()
    if(selected == "2"):
        print("Please enter ingredient: ")
        ingredientname()
    if(selected == "3"):
        print("A surprise is on it's way!")
        surpriseme()
    else:
        dashboard()

dashboard()
