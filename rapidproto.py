import requests
import json
import webbrowser

def userinput():
    print("Please specify how you would like search for a drink:")
    print("1 : Cocktail Name")
    print("2 : Ingredient Name")
    print("3 : Glass Name")

    selected = input()

    if(selected == "1"):
        cocktailname()
    if(selected == "2"):
        ingredientname()
    else: (print("Incorrect submission"))
        

def cocktailname():
    print("Please enter the name of the cocktail: \n")
    UserInput = input()
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+UserInput
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt["url"])
    
    for i in (tt["drinks"]):
        print(i, "\n")
    print(len(tt["drinks"])) 


def ingredientname():
    print("Please enter ingredient: \n")
    UserInput = input()
    f = r" https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+UserInput
    data = requests.get(f)
    tt = json.loads(data.text)
    #webbrowser.open(tt["url"])

    for i in (tt["drinks"]):
        print(i, "\n")
    print(len(tt["drinks"]))



userinput()
