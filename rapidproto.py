import requests
import json
import webbrowser
from controlled_vocab import *

user_input = ""

def surprise_me():
    print("We're selecting a random cocktail for you...")
    f = r"https: // www.thecocktaildb.com/api/json/v1/1/random.php"
    data = requests.get(f)
    tt = json.loads(data.text)
    for i in (tt["drinks"]):
        print("______________________________________")

        print("\nCocktail Name:   " + str(i["strDrink"]), "\n")
        print("Ingredients:")
        print("- " + str(i["strMeasure1"]) +
                " of " + str(i["strIngredient1"]))
        x = 1
        while((str(i["strIngredient"+str(x+1)])) != "None"):
             x += 1
             print("- " + str(i["strMeasure"+str(x)]) +
                  " of " + str(i["strIngredient"+str(x)]))
        # Instructions
        print("\nInstructions: ")
        instructions = str(i["strInstructions"])
        formatted = instructions.split(". ")
        j = 1
        for x in formatted:
            print(str(j)+". "+(x))
            j += 1
        print("______________________________________")
    
def cocktail_name(user_input):
    if user_input == "":
        print("Please enter the name of the cocktail: ")
    else:
        pass

    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+user_input
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt["url"])

    if tt["drinks"] is None:
        print()
        print("Sorry, That cocktail doesn't exist in our database :-(. Please try searching for something else")
        print()
        cocktail_name()
    else:
        for i in (tt["drinks"]):
            print("______________________________________")

            print("\nCocktail Name:   " + str(i["strDrink"]), "\n")
            print("Ingredients:")
            print("- " + str(i["strMeasure1"]) +
                  " of " + str(i["strIngredient1"]))
            x=1
            while((str(i["strIngredient"+str(x+1)]))!="None"):
                x+=1
                print("- " + str(i["strMeasure"+str(x)]) + " of "+ str(i["strIngredient"+str(x)]))
            # Instructions
            print("\nInstructions: ")
            instructions = str(i["strInstructions"])
            formatted = instructions.split(". ")
            j=1
            for x in formatted:
                print(str(j)+". "+(x))
                j+=1
            print("______________________________________")

def ingredient_name():
    #using controlled vocab (vodka only implemented)
    user_input = vodka_cv(user_input)

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
