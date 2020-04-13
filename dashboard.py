import requests
import json
import webbrowser
from controlled_vocab import *
from rapidproto import *


print("Please specify how you would like search for a drink:")
print("1 : Cocktail Name")
print("2 : Ingredient Name")
print("3 : Glass Name")

selected = input()

    # Function selector (there's probably a better way of doing this)
if(selected == "1"):
    cocktailname()
if(selected == "2"):
    ingredientname()
else:
    (print("Incorrect submission"))
