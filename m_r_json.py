#machine readable json

import json

def m_r_json(cocktail_name, cocktail_ingredients, cocktail_instructions):
    #takes drink name in, recipe
    #ingredients comes as list of ingredients

    data = {}
    data['cocktail'] = []
    data['cocktail'].append({
        'name': str(cocktail_name),
        'ingredients': str(cocktail_ingredients),
        'instructions': str(cocktail_instructions)})

    with open('cocktail_m_r_json_output.txt', 'w') as outfile:
        json.dump(data, outfile)

    print("\nWritten to JSON file!\n")
