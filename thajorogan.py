selector = 0
specific_cocktail = []
for i in (tt["drinks"]):
    selector = selector+1
    print("______________________________________")

    cocktail_name_var = str(i["strDrink"])

     print(str(selector) + ". " + "\nCocktail Name:   " +
            str(i["strDrink"]), "\n")
      specific_cocktail.append(str(i["strDrink"]))
       # Printing the ingredients and their respective quantities.
       print("Ingredients:")
        #"""x=1
        #while((str(i["strIngredient"+str(x+1)]))!="None"):
        #    x+=1
        #    print("- " + str(i["strMeasure"+str(x)]) + " of "+ str(i["strIngredient"+str(x)]))
        #"""
        new_ingredient = ""
         ingredients_output_list = []
          x = 1
           while((str(i["strIngredient"+str(x)])) != "None"):
                new_ingredient = str(i["strMeasure"+str(x)]) + \
                    " of " + str(i["strIngredient"+str(x)])
                ingredients_output_list.append(new_ingredient)
                print(new_ingredient)
                x += 1


            #code for instructions (copied from surprise me
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
            get_specific_ingredients(specific_cocktail, selector)
