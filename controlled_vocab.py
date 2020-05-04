import json
import tutorial

#fucntion to implement vodka orientated controlled vocabulary
def vodka_cv(user_ingredient):
    with open('tutorial/vodka.json', 'r') as myfile: #JSON file opened
        data=myfile.read() #whole file read into variable

    myfile.close() #closing file to reduce unecessary use of memory (and avoid errors by ahving file remaining open)

    obj = json.loads(data) #uses loads() function to interpret JSON saved in variable

    vodka_list = [] #initalising list used to store controlled vocabulary terms
    for pair in obj: #looping through each item in the JSON variable
        vodka_list.append((pair["vodka_brand"]).lower()) #adds each brand saved in the JSON to the list

    if user_ingredient.lower() in vodka_list: #checks to see if user input is part of the controlled vocabulary
        return ["vodka"]
    else:
        return [user_ingredient]

#fucntion to implement vodka orientated controlled vocabulary
#works in same way as vodka function, with added items
def whisky_cv(user_ingredient):

    #initalising the vocabulary with various names used within the API
    whisky_list = ["scotch", "whisky", "blended whisky", "single malt",
                   "whiskey", "blended whiskey", "irish whiskey"]

    with open('tutorial/whisky.json', 'r') as myfile:
        data=myfile.read()

    myfile.close()

    obj = json.loads(data)

    for pair in obj:
        whisky_list.append((pair["whisky_brand"]).lower())

    if user_ingredient.lower() in whisky_list:
        return ["Scotch", "Blended whiskey", "Whiskey", "Irish whiskey", "Whisky"]

    else:
        return [user_ingredient]

def gin_cv(user_ingredient):
    with open('tutorial/gin.json', 'r') as myfile:
        data=myfile.read()

    myfile.close()

    obj = json.loads(data)

    gin_list = []
    for pair in obj:
        gin_list.append((pair["Gin_brand"]).lower())

    if user_ingredient.lower() in gin_list:
        return ["gin"]
    else:
        return [user_ingredient]

def rum_cv(user_ingredient):
    with open('tutorial/rum.json', 'r') as myfile:
        data=myfile.read()

    myfile.close()

    obj = json.loads(data)

    rum_list = []
    for pair in obj:
        rum_list.append((pair["rum_brand"]).lower())

    if user_ingredient.lower() in rum_list:
        return ["rum"]
    else:
        return [user_ingredient]
        




