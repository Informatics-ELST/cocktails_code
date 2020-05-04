import requests
import json
import webbrowser
from rapidproto import *


def dashboard():

    selected = -1
    while selected != int(0):
        print("Please specify how you would like search for a drink:")
        print("1 : Cocktail Name")
        print("2 : Ingredient Name")
        print("3 : Surprise Me!")
        print("0 : Exit program")


        selected = input("\nEnter your choice: ")
        if(selected == "1"):
            print("\nPlease enter the name of the cocktail: ")
            user_input = input()
            cocktail_name(user_input)

        elif(selected == "2"):
            #print("Please enter ingredient: ")
            choose_ingredient()

        elif(selected == "3"):
            print("\nWe're selecting a random cocktail for you...")        
            surprise_me()

        elif selected == "0":
            return

        else:
            (print("\nIncorrect submission"))


dashboard()
