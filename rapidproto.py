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
<<<<<<< Updated upstream
    #webbrowser.open(tt["url"])
=======
    # webbrowser.open(tt[f])
    #print("this is tt drinks: " + str(tt["drinks"]))
    #print("this is tt drinks length: " + str(len(tt["drinks"])))

    # Handling incorrect inputs
    selector = 10
    specific_cocktail = []


    if tt["drinks"] is None:
        print()
        print(
            "Sorry, That cocktail doesn't exist in our database :-(. Please try searching for something else")
        print()

    elif(len(tt["drinks"]) == 1):
        #for i in (tt["drinks"]):
        print("______________________________________")
        #i = 0
        print("Specific Cocktail", specific_cocktail)
        cocktail_name_var = specific_cocktail[selector]

        print("\nCocktail Name:   " + str(selector[specific_cocktail]), "\n")

        # Printing the ingredients and their respective quantities.
        print("Ingredients:")

        new_ingredient = ""
        ingredients_output_list = []


        x = 1
        while(str(["strIngredient"+str(x)]) != "None"):
            new_ingredient = str(specific_cocktail["strMeasure"+str(x)]) + \
                " of " + str(specific_cocktail["strIngredient"+str(x)])
            ingredients_output_list.append(new_ingredient)
            #print(new_ingredient)
            x += 1

            # code for instructions (copied from surprise me
        print("\nThis is how you make it: ")
        instructions = str(specific_cocktail["strInstructions"])
        formatted = instructions.split(". ")
        j = 1
        instructions_list = []
        for x in formatted:
            instructions_list.append(str(j)+". "+(x))
            print(str(j)+". "+(x))
            j += 1
>>>>>>> Stashed changes

    for i in (tt["drinks"]):
        print("______________________________________")
<<<<<<< Updated upstream

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
    mr = input("Would you like to produce a machine readable output? If so, what type?")
    print("0 : No, I would not like a machine readable output")
=======
    else:
        for i in (tt["drinks"]):
            selector = selector+1
            print("______________________________________")

            cocktail_name_var = str(i["strDrink"])

            print(str(selector) + ". " + "\nCocktail Name:   " + str(i["strDrink"]), "\n")
            specific_cocktail.append(str(i["strDrink"]))
            # Printing the ingredients and their respective quantities.
            print("Ingredients:")
            # """x=1
            # while((str(i["strIngredient"+str(x+1)]))!="None"):
            #    x+=1
            #    print("- " + str(i["strMeasure"+str(x)]) + " of "+ str(i["strIngredient"+str(x)]))
            # """
            new_ingredient = ""
            ingredients_output_list = []
            x = 1
            while((str(i["strIngredient"+str(x)])) != "None"):
                new_ingredient = str(i["strMeasure"+str(x)]) + \
                    " of " + str(i["strIngredient"+str(x)])
                ingredients_output_list.append(new_ingredient)
                print(new_ingredient)
                x += 1
            print("Specific Cocktail",specific_cocktail)

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

            #for i in (tt["drinks"]):

                #print(str(selector) + ". " + str(i["strDrink"]), "\n")
            #selector = selector+1
        choice = input("Please choose the cocktail (by it's number): ")
        chosen_drink = specific_cocktail[int(choice)]
        print("chosen drink:", chosen_drink)
        machine_readable_outputs(chosen_drink)
        #get_specific_ingredients(specific_cocktail, selector)


    machine_readable_outputs(cocktail_name_var, ingredients_output_list, instructions_list, instructions)


def machine_readable_outputs(cocktail_name, cocktail_ingredients_list, cocktail_instructions, instructions_string):
    print("\nWould you like to produce a machine readable output?\nIf so, what type of output do you require?")

    print("\n0 : No, I would not like a machine readable output")
>>>>>>> Stashed changes
    print("1 : RDFa")
    print("2 : HTML Microdata")
    

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

