#machine readable json

import json

def m_r_json(cocktail_name, cocktail_ingredients, cocktail_instructions):

    #loops through list of ingredients to create one continuous string
    ingredients = ""
    for ingredient in cocktail_ingredients:
        ingredients = ingredients + ingredient + ", " 
    ingredients = ingredients[:-2]

    #loops through list of instructions to create one continuous string
    instructions = ""
    for instruction in cocktail_instructions:
        instructions = instructions + instruction + ", "
    instructions = instructions[:-2]

    data = {} #initalising a dictionary to contain elements for JSON

    #adding tags to the variable
    data['@context'] = 'https://schema.org'
    data['@type'] = 'Recipe'

    #adding data to the variable
    data['name'] = cocktail_name
    data['ingredients'] = ingredients
    data['instructions'] = instructions

    #writing to a file
    with open('cocktail_m_r_json_output.json', 'w') as file:
        file.write('<script type="application/ld+json">\n') #adding tags for data type
        json.dump(data, file) #converting dictionary to json format
        file.write('\n</script>')

    file.close()

    print("\nWritten to JSON file!\n\n")
