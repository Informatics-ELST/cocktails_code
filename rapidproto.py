# Imports
import requests
import json
import webbrowser
from controlled_vocab import *


# Global Definitions
user_input = ""

# SEARCH for a cocktail by it's name
        


def cocktail_name(user_input):
    
    if user_input == "":
        user_input = input("Please enter the name of the cocktail: ")
    else:
        pass
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+user_input
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt[f])

    # Handling incorrect inputs
    if tt["drinks"] is None:
        print()
        print("Sorry, That cocktail doesn't exist in our database :-(. Please try searching for something else")
        print()
        
    else:
        for i in (tt["drinks"]):
            print("______________________________________")

            print("\nCocktail Name:   " + str(i["strDrink"]), "\n")
            
            # Printing the ingredients and their respective quantities.
            print("Ingredients:")
            print("- " + str(i["strMeasure1"]) +
                  " of " + str(i["strIngredient1"]))
            x=1
            while((str(i["strIngredient"+str(x+1)]))!="None"):
                x+=1
                print("- " + str(i["strMeasure"+str(x)]) + " of "+ str(i["strIngredient"+str(x)]))

            # Printing the instructions
            print("\nInstructions: ")
            instructions = str(i["strInstructions"])
            formatted = instructions.split(". ")
            j=1
            for x in formatted:
                print(str(j)+". "+(x))
                j+=1
            print("______________________________________")


# FILTER Cocktails by an ingredient's name.
# Note  : this will display all the outputs, however, to see more details of the outputs a SEARCH function will be called
def ingredient_name():
    global user_input
    #using controlled vocab (vodka only implemented)
    #user_input = vodka_cv(user_input)

    f = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+input()
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt["url"])
    if tt is None:
        print("sorry bro no can do")
    else:
        print("\nCocktail Name:")
        selector = 0
        specific_cocktail = []
        for i in (tt["drinks"]):
            selector= selector+1
            print(str(selector) + ". " + str(i["strDrink"]), "\n")
            specific_cocktail.append(str(i["strDrink"]))

        choice = input("Please choose the cocktail (by it's number): ")
        user_input = specific_cocktail[int(choice)-1]
        cocktail_name(user_input)

# Allows users to find a random cocktail (ID_RANGE: 1100 - )
def surprise_me():
    
    f = r"https://www.thecocktaildb.com/api/json/v1/1/random.php"
    data = requests.get(f)
    tt = json.loads(data.text)
    for i in (tt["drinks"]):
        print("______________________________________")

        print("\nWe have selected:   " + str(i["strDrink"]), "\n")
        print("Here's the ingredients:")
        print("- " + str(i["strMeasure1"]) +
              " of " + str(i["strIngredient1"]))
        x = 1
        while((str(i["strIngredient"+str(x+1)])) != "None"):
            x += 1
            print("- " + str(i["strMeasure"+str(x)]) +
                  " of " + str(i["strIngredient"+str(x)]))
        # Instructions
        print("\nThis is how you make it: ")
        instructions = str(i["strInstructions"])
        formatted = instructions.split(". ")
        j = 1
        for x in formatted:
            print(str(j)+". "+(x))
            j += 1
        print("______________________________________")
