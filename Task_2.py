import sys

# list of ingredients available
pantry = {}

# list of recipes
menu = []
# list with the name of the recipes
menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]

file = open("recipe.txt")
p = False
for i in range(len(menu_list)):
    dicRes = dict()
    for j in file:
        j = j.strip("\n")
        if j.startswith(menu_list[i]):
            p = True
        elif j.endswith("peaches"):
            p = False
            j = j.split(" ",1)
            dicRes[j[1]] = float(j[0])
            break
        elif p:
            j = j.split(" ",1)
            dicRes[j[1]] = float(j[0])
    menu.append(dicRes)
file.close()

# ask for ingredients available
def pantry_ingredients(dicRes):
    for i in dicRes:
        item = input(f'How many {i} do you have? ')
        pantry[i] = (float(item))


# show the ingredients of an exisiting pantry
def show_pantry():  
    for i in pantry:
       print(f'{pantry[i]} {i}')

# show the menu options
def recipe_menu():
    print("What would you like to cook? Here's the recipe book:")
    
    # options already in the menu
    for i in range(len(menu_list)):
      print(i+1, ". ", menu_list[i], sep="")
    
    # add new recipe
    print(i+2, ". Add new recipe.", sep="")

    # exit program 
    print(i+3, ". Nevermind, I don't want to cook anything (Exit).", sep="")
    
    option = int(input("Select an option by typing its number here:"))
    
    # if new recipe selected
    if option == i+2:
      new_recipe_name = input("Name of the new recipe: ")
      menu_list.append(new_recipe_name)
      
      new_recipe = {}
      for i in dicRes:
        item = input(f'How many {i} do you have? ')
        new_recipe[i] = (float(item))
      menu.append(new_recipe)
    
    #return option selected
    return option

# check valid option
def valid_option(option):
    while True:
      # valid option
      if option in range(1,len(menu_list)+1):
          recipe = menu[option - 1]
          global servings
          servings = int(input("How many servings? "))
          break

      # exit program
      elif option == len(menu_list)+2:
          print('See you later!')
          sys.exit(0)

      # invalid option
      else:
          print('Please select a valid option')
          option = recipe_menu()
    return recipe

# update pantry
def pantry_update():
    # list of updated ingredients available
    for i in pantry:
        leftover = pantry[i] - recipe[i]*servings
        if leftover < 0: 
            # if not enough ingredients
            return False
        else:
            pantry[i] = leftover
    # if enough ingredients


# ask user to input ingredients available
pantry_ingredients(dicRes)
cook = True

# initialize servings to 1
servings = 1
while cook:
    # ask user what they'd like to make (from options)
    option = recipe_menu()
    print(f'You selected option {option}')
    
    # verify the selected option is valid
    recipe = valid_option(option)
    
    # if the option is valid and want to cook
    
    # while not enough ingredients
    while pantry_update() == False:
      print('Not enough ingredients!')
      pantry = {}
      print("Update the ingredients.")
      pantry_ingredients(dicRes)
    
    # enough ingredients.
    print('Great choice. That was delicious!')
    print("Here's what's left in the pantry: ")
    show_pantry()