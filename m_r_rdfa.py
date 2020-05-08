def m_r_rdfa(cocktail_name, cocktail_ingredients_list, cocktail_instructions):
    
    # Creates a string of all of the ingredients to be able to print it all off
    ingredients_string = ""
    x = 0
    while x < len(cocktail_ingredients_list):
        #if(x == 0):
        new_string = '- <span property = "recipeIngredient">'+cocktail_ingredients_list[x]+'</span>\n\t'
        ingredients_string = ingredients_string+new_string
        x = x+1

    # Writes the entirety of the RDFa output into a HTML file - we have checked schema.org for formatting
    with open('cocktail_m_r_rdfa_output.html', 'w') as file:
        file.write('<div vocab="http://schema.org/" typeof="Recipe">\n')
        file.write('  <span property="name">'+cocktail_name+'</span>\n')
        file.write('  Ingredients:\n')
        file.write(ingredients_string)
        file.write('\n')
        file.write('Instructions:\n')
        file.write('   <span property="recipeInstructions">\n')
        file.write(cocktail_instructions)
        file.write('\n')
        file.write('   </span>\n')
        file.write('</div>')

    file.close()
    # Tells the user that a file has been made.
    print("\nWritten to HTML file as RDFa!\n\n")
