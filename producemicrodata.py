#cocktail = name, author, date published, description, 
cocktail_name = "espresso martini"
cocktail_ingredients_list = ["3 vodka", "2 lemons", "1 coffee"]
cocktail_instructions = "do this"

ingredients_string = "\t"
x = 0
while x < len(cocktail_ingredients_list):
    new_string = '- <span property = "recipeIngredient">'+cocktail_ingredients_list[x]+'</span>\n\t'
    ingredients_string = ingredients_string+new_string
    x = x+1

print("this is ingredients string: ", ingredients_string)



#print("<span property = 'name' > %s < /span > " % (drinkname,))
print(
"""
    <div vocab="http://schema.org/" typeof="Recipe">\n
      <span property="name">"""+cocktail_name+"""</span>\n
      By <span property="author">John Smith</span>,
      <meta property="datePublished" content="2009-05-08">May 8, 2009
      <img property="image" src="bananabread.jpg"
        alt="Banana bread on a plate" />
      <span property="description">This classic banana bread recipe comes
      from my mom -- the walnuts add a nice texture and flavor to the banana
      bread.</span>
      Prep Time: <meta property="prepTime" content="PT15M">15 minutes
      Cook time: <meta property="cookTime" content="PT1H">1 hour
      Yield: <span property="recipeYield">1 loaf</span>
      Tags: <link property="suitableForDiet" href="http://schema.org/LowFatDiet" />Low Fat
      <div property="nutrition" typeof="NutritionInformation">
        Nutrition facts:
        <span property="calories">240 calories</span>,
        <span property="fatContent">9 grams fat</span>
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