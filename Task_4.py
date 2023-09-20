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

# Hace una copia de recipe.txt
file = open("recipe.txt")
file2 = open("recipe2update.txt", "w")
for line in file:
    file2.write(line)
file.close()
file2.close()

# pide los servings
def servingsn():
    global servings
    servings = int(input("How many servings? "))

# Revisa si los ingredientes del pantry son suficientes y devuelve las recetas que se puedan hacer
def menu_update():

    new_menu_list = []
    new_menu = []
    for i in range(len(menu)):
        newdict = dict()
        for j in pantry:
            if pantry[j] >= menu[i][j] * servings:
                newdict[j] = menu[i][j]
            else:
                break
        if len(newdict) == 10:
            new_menu.append(newdict)
            new_menu_list.append(menu_list[i])
    return new_menu,new_menu_list

# ask for ingredients available
def pantry_ingredients(dicRes):
    for i in dicRes:
        item = input(f'How many {i} do you have? ')
        pantry[i] = (float(item))
    # global servings
    # servings = int(input("How many servings? "))



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
    
    if menu_list == []:
        i = -1
    # add new recipe
    print(i+2, ". Add new recipe.", sep="")

    # exit program 
    print(i+3, ". Nevermind, I don't want to cook anything (Exit).", sep="")
    
    option = int(input("Select an option by typing its number here:"))
    
    # if new recipe selected
    # Añade las nuevas recetas a recipe2udate.txt
    if option == i+2:
        file2 = open("recipe2update.txt", "a")
        new_recipe_name = input("Name of the new recipe: ")
        file2.write(new_recipe_name + "\n")
        menu_list.append(new_recipe_name)
      
        new_recipe = {}
        for i in dicRes:
            item = input(f'How many {i} are required? ')
            new_recipe[i] = (float(item))
            file2.write(f"{item} {i}\n")
        menu.append(new_recipe)
        file2.close()
    
    #return option selected
    return option

# check valid option
def valid_option(option):
    while True:
      # valid option
      if option in range(1,len(menu_list)+1):
          recipe = menu[option - 1]
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
        leftover = pantry[i] - recipe[i] * servings
        if leftover < 0: 
            # if not enough ingredients
            return False
        else:
            pantry[i] = leftover
    # if enough ingredients
    return True

# ask user to input ingredients available
pantry_ingredients(dicRes)
servingsn()
cook = True
menu,menu_list = menu_update()
# initialize servings
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
    servingsn()
    menu,menu_list = menu_update()