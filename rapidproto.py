import requests                 # Requests are made to retrieve data from the API
import json                     # API feeds JSON files
import webbrowser               # Allows the code to interface with the API
from controlled_vocab import *  # Imports all of the controlled vocabulary functions
from m_r_json import *          # Machine Readable output - JSON
from m_r_rdfa import *          # Machine Readable ouptut - RDFa


# SEARCH for a cocktail by it's name
# use of global variables seen as bad coding practice
# pass variables to functions instead

def cocktail_name(user_input):
    """if user_input == "":
        user_input = input("Please enter the name of the cocktail: ")
    else:
        pass"""
    # above code unnecessary if cocktail_name() is called on appropriate variables

    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+user_input

    data = requests.get(f)
    tt = json.loads(data.text)

    cocktail_found = 1

    # Handling incorrect inputs
    if tt["drinks"] is None:
        print()
        print(
            "Sorry, That cocktail doesn't exist in our database :-(. Please try searching for something else")
        print()
        cocktail_found = 0

    # If there is only one result, the full details of the cocktail is printed
    elif(len(tt["drinks"]) == 1):
        for i in (tt["drinks"]):
            print("______________________________________")

            cocktail_name_var = str(i["strDrink"])

            print("\nCocktail Name:   " + str(i["strDrink"]), "\n")

            # Printing the ingredients and their respective quantities.
            print("Ingredients:")

            new_ingredient = ""
            ingredients_output_list = []


            x = 1

            while(str(i["strIngredient"+str(x)]) != "None"):
                new_ingredient = str(i["strMeasure"+str(x)]) + \
                    " of " + str(i["strIngredient"+str(x)])
                ingredients_output_list.append(new_ingredient)
                print(new_ingredient)
                x += 1

                # code for instructions (copied from surprise me
            print("\nThis is how you make it: ")
            instructions = str(i["strInstructions"])
            formatted = instructions.split(". ")
            j = 1
            instructions_list = []
            for x in formatted:
                instructions_list.append(str(j)+". "+(x))
                print(str(j)+". "+(x))
                j += 1

        print("______________________________________")

    # If there are multiple outputs, a list of the results is printed instead.
    # This makes it easier for the user to see the output if there are lots of results.
    # We then index each result so that the user can select which they would like to get more information about.
    else:
        selector = -1
        specific_cocktail = []
        for i in (tt["drinks"]):
            selector = selector+1
            #print("specific cocktails:", str(specific_cocktail))
            print("______________________________________\n")

            cocktail_name_var = str(i["strDrink"])
            specific_cocktail.append(str(i["strDrink"]))

            # Selector assigns an index to each result
            print(str(selector) + ". " +
                  str(i["strDrink"]))

            new_ingredient = ""
            ingredients_output_list = []
            

            print("______________________________________")

        # Prompts the user to select one of the results
        choice = input("\nPlease choose the cocktail (by it's number): ")
        cocktail_name_var = specific_cocktail[int(choice)]

        print("______________________________________")
        print("\nCocktail Name: ", cocktail_name_var)
        print("\nIngredients:")
        x = 1
        while((str(i["strIngredient"+str(x)])) != "None"):
            new_ingredient = str(i["strMeasure"+str(x)]) + " of " + str(i["strIngredient"+str(x)])
            ingredients_output_list.append(new_ingredient)
            print(new_ingredient)
            x += 1

        # Code for instructions (similar from surprise me)
        print("\nThis is how you make it: ")
        instructions = str(i["strInstructions"])
        formatted = instructions.split(". ")
        j = 1
        instructions_list = []
        for x in formatted:
            instructions_list.append(str(j)+". "+(x))
            print(str(j)+". "+(x))
            j += 1
        print("______________________________________")

    if (cocktail_found == 1):
        machine_readable_outputs(cocktail_name_var, ingredients_output_list, instructions_list, instructions)


# This function directs the program to the relevant functions, depending on which machine readable output they would like.
def machine_readable_outputs(cocktail_name, cocktail_ingredients_list, cocktail_instructions, instructions_string):
    print("\nWould you like to produce a machine readable output?\nIf so, what type of output do you require?")

    print("\n0 : No, I would not like a machine readable output")
    print("1 : RDFa")
    print("2 : JSON LD")

    m_r_input = input()

    if m_r_input == "0":
        print("______________________________________\n")
        return
    elif m_r_input == "1":
        # RDFa function called:
        m_r_rdfa(cocktail_name, cocktail_ingredients_list, instructions_string)
    elif m_r_input == "2":
        # JSON function called:
        m_r_json(cocktail_name, cocktail_ingredients_list,
                 cocktail_instructions)
    print("______________________________________")
    

# Prompts the user for the ingredient they would like to select.
# This allows us to run a controlled vocabulary before the ingredient function.
def choose_ingredient():
    user_input = []
    #print("Please enter ingredient: \n")
    user_input.append(input("\nPlease enter ingredient: \n"))
    print()

    # Controlled Vocabulary: Vodka
    user_input = vodka_cv(user_input[0])

    # Controlled Vocabulary: Gin
    user_input = gin_cv(user_input[0])

    # Controlled Vocabulary: Rum
    user_input = rum_cv(user_input[0])

    # Controlled Vocabulary: Whisky
    user_input = whisky_cv(user_input[0])

    """if type(user_input) is list:
        for spirit in user_input:
            ingredient_name(spirit)
    else:
        ingredient_name(user_input)"""

    # print(user_input)
    ingredient_name(user_input)


# FILTER Cocktails by an ingredient's name.
# Note  : this will display all the outputs, however, to see more details of the outputs a SEARCH function will be called
def ingredient_name(ingredient_list):

    try:
        #print(ingredient_list)
        selector = -1
        specific_cocktail = []
        for ingredient in ingredient_list:
            # print(ingredient)

            f = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+ingredient
            data = requests.get(f)
            tt = json.loads(data.text)
            # webbrowser.open(tt["url"])
            if tt is None:
                print("No cocktails including that ingredient could be found")
            else:
                #print("\nCocktail Name:")
                #specific_cocktail = []
                for i in (tt["drinks"]):
                    selector = selector+1
                    print(str(selector) + ". " + str(i["strDrink"]), "\n")
                    specific_cocktail.append(str(i["strDrink"]))
        get_specific_ingredients(specific_cocktail, selector)
    except:
        print("\nNo cocktails with that ingredient could be found\n\n")
        # better error messagecould be implemented


# When there are multiple outputs, this allows the user to select the result by its index
def get_specific_ingredients(specific_cocktail, selector):
    # put below in separate function that only runs after all names output

    choice = input("Please choose the cocktail (by it's number): ")
    chosen_drink = specific_cocktail[int(choice)]
    cocktail_name(chosen_drink)


# This allows users to find a random cocktail if they have no preference
def surprise_me():
    # API Call
    f = r"https://www.thecocktaildb.com/api/json/v1/1/random.php"
    data = requests.get(f)
    tt = json.loads(data.text)
    # Prints all of the result details
    for i in (tt["drinks"]):
        print("______________________________________")
        cocktail_name_var = str(i["strDrink"])
        print("\nWe have selected:   " + cocktail_name_var, "\n")
        # Ingredients & Quantities
        print("Here's the ingredients:")
        new_ingredient = ""
        ingredients_output_list = []
        x = 1
        while((str(i["strIngredient"+str(x)]))!="None"):
            x+=1
            new_ingredient = "- " + str(i["strMeasure"+str(x)]) + " of " + str(i["strIngredient"+str(x)])
            ingredients_output_list.append(new_ingredient)
            print(new_ingredient)
        # Instructions
        print("\nThis is how you make it: \n")
        instructions = str(i["strInstructions"])
        formatted = instructions.split(". ")
        j = 1
        instructions_list = []
        for x in formatted:
            instructions_list.append(str(j)+". "+(x))
            print(str(j)+". "+(x))
            j += 1
        print("______________________________________")
    
    # Calls the Machine Readable output function
    machine_readable_outputs(cocktail_name_var, ingredients_output_list, instructions_list, instructions)
    
