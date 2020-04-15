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


    selected = input("Enter your choice: ")
    if(selected == "1"):
        print("Please enter the name of the cocktail: ")
        user_input = input()
        cocktail_name(user_input)
    if(selected == "2"):
        print("Please enter ingredient: ")
        ingredient_name()
    if(selected == "3"):
        print("We're selecting a random cocktail for you...")        
        surprise_me()
    else:
        dashboard()

dashboard()
