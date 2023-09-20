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



file = open("recipe.txt", "w")
for i in range(len(menu)):
    file.write(menu_list[i] + "\n")
    for j in range(len(units)):
        unit = units[j]
        if unit:
            unit += ' of '
        ingredient = ingredients[j]
        file.write(f"{menu[i][j]} {unit}{ingredient}\n")
file.close()
