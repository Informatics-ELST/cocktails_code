#machine readable json

import json

def m_r_json(cocktail_name, cocktail_ingredients, cocktail_instructions):
    #takes drink name in, recipe
    #ingredients comes as list of ingredients

    ingredients = ""
    for ingredient in cocktail_ingredients:
        ingredients = ingredients + ingredient + ", " 
    ingredients = ingredients[:-2]

    instructions = ""
    for instruction in cocktail_instructions:
        instructions = instructions + instruction + ", "
    instructions = instructions[:-2]

    data = {}
    data['@context'] = 'https://schema.org'
    data['@type'] = 'Recipe'

    data['name'] = cocktail_name
    data['ingredients'] = ingredients
    data['instructions'] = instructions

    """data['cocktail'] = []
    data['cocktail'].append({
        'name': str(cocktail_name),
        'ingredients': str(ingredients),
        'instructions': str(instructions)
        })"""

    with open('cocktail_m_r_json_output.json', 'w') as file:
        file.write('<script type="application/ld+json">\n')
        json.dump(data, file)
        file.write('\n</script>')

    file.close()

    print("\nWritten to JSON file!\n\n")
