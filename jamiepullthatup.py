try:
        #print(ingredient_list)
        selector = 0
        specific_cocktail = []
        for ingredient in ingredient_list:
            #print(ingredient)

            f = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+ingredient
            data = requests.get(f)
            tt = json.loads(data.text)
            #webbrowser.open(tt["url"])
            if tt is None:
                print("No cocktails including that ingredient could be found")
            else:
                #print("\nCocktail Name:")
                #selector = 0
                #specific_cocktail = []
                for i in (tt["drinks"]):
                    selector = selector+1
                    print(str(selector) + ". " + str(i["strDrink"]), "\n")
                    specific_cocktail.append(str(i["strDrink"]))
        get_specific_ingredients(specific_cocktail, selector)
    except:
        print("\nNo cocktails with that ingredient could be found\n")
        #better error messagecould be implemented
