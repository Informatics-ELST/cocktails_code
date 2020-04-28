#cocktail = name, author, date published, description, 


def m_r_rdfa(cocktail_name, cocktail_ingredients_list, cocktail_instructions):
    #cocktail_name = "espresso martini"
    #cocktail_ingredients_list = ["3 vodka", "2 lemons", "1 coffee"]
    #cocktail_instructions = "do this"

    ingredients_string = ""
    x = 0
    while x < len(cocktail_ingredients_list):
        #if(x == 0):
        new_string = '- <span property = "recipeIngredient">'+cocktail_ingredients_list[x]+'</span>\n\t'
        ingredients_string = ingredients_string+new_string
        x = x+1

    #print("this is ingredients string: ", ingredients_string)
    #print("<span property = 'name' > %s < /span > " % (drinkname,))
    print(
    """
        <div vocab="http://schema.org/" typeof="Recipe">\n
          <span property="name">"""+cocktail_name+"""</span>\n
          </div>
          Ingredients:
        """+
          str(ingredients_string),
          #- <span property="recipeIngredient">3 or 4 ripe bananas, smashed</span>
          #- <span property="recipeIngredient">1 egg</span>
          #- <span property="recipeIngredient">3/4 cup of sugar</span>
          
    """Instructions:
          <span property="recipeInstructions">
          """+cocktail_instructions+"""
          </span>
        </div>
    """
    )

    #with open('cocktail_m_r_json_output.txt', 'w') as file:
    #    file.write('<script type="application/ld+json">')
    #    json.dump(data, file)
    #    file.write('</script>')

    #file.close()

    #print("\nWritten to JSON file!\n")
