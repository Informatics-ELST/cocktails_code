import requests
import json
import webbrowser
from controlled_vocab import *

#UserInput = ""

def cocktailname(UserInput):
    #global UserInput
    if (UserInput==""):
        print("Please enter the name of the cocktail: ")
        UserInput = input()
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+UserInput
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt["url"])

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
        print()


def choose_ingredient():
    print("Please enter ingredient: \n")
    UserInput = input()

    UserInput = vodka_cv(UserInput)
    

    #this will have to be the last cv check to be run, I'll see if there's
    #a more efficient way to code this...
    #this is due to the ingredientname() being called within whisky_cv()
    UserInput = whisky_cv(UserInput)

    if type(UserInput) is list:
        for spirit in UserInput:
            ingredientname(spirit)
    else:
        ingredientname(UserInput)

    

def ingredientname(UserInput):
    #global UserInput
    """print("Please enter ingredient: \n")
    UserInput = input()

    #using controlled vocab (vodka only implemented)
    UserInput = vodka_cv(UserInput)"""

    f = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+UserInput
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt["url"])
    print("\nCocktail Name:")
    selector = 0
    specificCocktail = []
    for i in (tt["drinks"]):
        selector= selector+1
        print(str(selector) + ". " + str(i["strDrink"]), "\n")
        specificCocktail.append(str(i["strDrink"]))

    choice = input("Please choose the cocktail (by it's number): ")
    chosen_drink = specificCocktail[int(choice)-1]
    cocktailname(chosen_drink)

