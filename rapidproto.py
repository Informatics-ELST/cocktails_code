import requests
import json
import webbrowser
from controlled_vocab import *

UserInput = ""

def cocktailname():
    global UserInput
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
        print("- " + str(i["strIngredient1"]))
        x=1
        while((str(i["strIngredient"+str(x+1)]))!="None"):
            x+=1
            print("- " + str(i["strIngredient"+str(x)]))

        # Ingredients - need to fix if there are not 4 ingredients (maybe loop?)
        print("Ingredients:     " + str(i["strIngredient1"]) + ", " + str(i["strIngredient2"]) + ", " + str(i["strIngredient3"]) + ", " + str(i["strIngredient4"]) + "\n")

        # Instructions
        print("\nInstructions: " + str(i["strInstructions"])+"\n")

def ingredientname():
    global UserInput
    print("Please enter ingredient: \n")
    UserInput = input()

    #using controlled vocab (vodka only implemented)
    UserInput = vodka_cv(UserInput)

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
    UserInput = specificCocktail[int(choice)-1]
    cocktailname()

