import requests
import json
import webbrowser
from controlled_vocab import *

UserInput = ""

def surpriseme():
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
    
def cocktailname():
    global UserInput
    print("Please enter the name of the cocktail: ")
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+input()
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt["url"])

    if tt["drinks"] is None:
        print()
        print("Sorry, That cocktail doesn't exist in our database :-(. Please try searching for something else")
        print()
        cocktailname()
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
            print()
            print("______________________________________")
            print()

def ingredientname():
    global UserInput
    #using controlled vocab (vodka only implemented)
    UserInput = vodka_cv(UserInput)

    f = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+input()
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt["url"])
    if tt is None:
        print("sorry bro no can do")
    else:
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
