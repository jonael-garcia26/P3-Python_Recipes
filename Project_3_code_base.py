import sys

# units of ingredients
units = ['cups', 'tablespoons', '', 'cups', 'teaspoons', 'teaspoons', 'slices', '', '', '']

# names of ingredients 
ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']

# list of ingredients available
pantry = []

# recipes
banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2, 0, 0]
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 0, 0, 3]
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 0, 5, 0]
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0, 0, 0]
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 0, 0.5, 1]

# list of recipes
menu = [banana_pancake_recipe, peach_crepe_recipe, apple_pie_recipe, french_toast_recipe, scrambled_eggs]

# list with the name of the recipes
menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]

# ask for ingredients available
def pantry_ingredients(units, ingredients):
    for i in range(len(units)):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        item = input(f'How many {unit}{ingredient} do you have? ')
        pantry.append(float(item))


# show the ingredients of an exisiting pantry
def show_pantry():  
    for i in range(len(pantry)):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        print(f'{pantry[i]} {unit}{ingredient}')

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
      
      new_recipe = []
      for i in range(len(units)):
          unit = units[i]
          if unit:
              unit += ' of '
          ingredient = ingredients[i]
          item = input(f'How many {unit}{ingredient} are required? ')
          new_recipe.append(float(item))
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
    new_pantry = []
    for i in range(len(pantry)):
        leftover = pantry[i] - recipe[i]*servings
        if leftover < 0: 
            # if not enough ingredients
            return False
        new_pantry.append(leftover)
    pantry[:] = new_pantry
    # if enough ingredients
    return True


# ask user to input ingredients available
pantry_ingredients(units, ingredients)
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
    while not pantry_update():
      print('Not enough ingredients!')
      pantry = []
      print("Update the ingredients.")
      pantry_ingredients(units, ingredients)
      pantry_update()
    
    # enough ingredients.
    print('Great choice. That was delicious!')
    print("Here's what's left in the pantry: ")
    show_pantry()