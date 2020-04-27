import requests
import json
import webbrowser
from controlled_vocab import *


"""# Global Definitions
user_input = ""

# SEARCH for a cocktail by it's name"""
#use of global variables seen as bad coding practice
#pass variables to functions instead
        

def cocktail_name(user_input):
    
    """if user_input == "":
        user_input = input("Please enter the name of the cocktail: ")
    else:
        pass"""
    #above code unnecessary if cocktail_name() is called on apropriate variables

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

            new_ingredient = ""
            ingredients_output_list = []
            x=1
            while((str(i["strIngredient"+str(x+1)]))!="None"):
                
                new_ingredient = str(i["strMeasure"+str(x)]) + " of " + str(i["strIngredient"+str(x)])
                ingredients_output_list.append(new_ingredient)
                #print("1")
                x += 1
                
            
            print(ingredients_output_list)


    #mr = input("Would you like to produce a machine readable output? If so, what type?")
    #print("0 : No, I would not like a machine readable output")

    #print("1 : RDFa")

    #print("2 : HTML Microdata")
    #recipe name, author, date published, description, preptime, cooktime, ingredients, instructions
    

def choose_ingredient():
    user_input = []
    #print("Please enter ingredient: \n")
    user_input.append(input("Please enter ingredient: \n"))

    user_input = vodka_cv(user_input[0])
    
    user_input = whisky_cv(user_input[0])

    """if type(user_input) is list:
        for spirit in user_input:
            ingredient_name(spirit)
    else:
        ingredient_name(user_input)"""

    #print(user_input)
    ingredient_name(user_input)


# FILTER Cocktails by an ingredient's name.
# Note  : this will display all the outputs, however, to see more details of the outputs a SEARCH function will be called
def ingredient_name(ingredient_list):

    try:
        #print("try triggered")
        selector = 0
        specific_cocktail = []
        for ingredient in ingredient_list:
            #print(ingredient)
            
            f = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+ingredient
            data = requests.get(f)
            tt = json.loads(data.text)
            #webbrowser.open(tt["url"])
            if tt is None:
                print("sorry bro no can do") #sort out language used here for submission
            else:
                #print("\nCocktail Name:")
                #selector = 0
                #specific_cocktail = []
                for i in (tt["drinks"]):
                    selector= selector+1
                    print(str(selector) + ". " + str(i["strDrink"]), "\n")
                    specific_cocktail.append(str(i["strDrink"]))
        get_specific_ingredients(specific_cocktail, selector)
    except:
        print("\nNo cocktails with that ingredient could be found\n")
        #better error messagecould be implemented


def get_specific_ingredients(specific_cocktail, selector):
    #put below in separate function that only runs after all names output
    choice = input("Please choose the cocktail (by it's number): ")
    chosen_drink = specific_cocktail[int(choice)-1]
    cocktail_name(chosen_drink)



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
