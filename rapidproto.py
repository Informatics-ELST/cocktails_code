import requests
import json
import webbrowser
from controlled_vocab import *

UserInput = ""

def dashboard():

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
    else: (print("Incorrect submission"))
        

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

        # Ingredients - need to fix if there are not 4 ingredients (maybe loop?)
        print("Ingredients:     " + str(i["strIngredient1"]) + ", " + str(i["strIngredient2"]) + ", " + str(i["strIngredient3"]) + ", " + str(i["strIngredient4"]) + "\n")
 
        # Instructions
        print("Instructions:    " + str(i["strInstructions"]), "\n")


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

# Call dashboard / Main
dashboard()
