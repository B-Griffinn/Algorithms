#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

	# var for batches arr
	batches = []

	# iterate over recipe
	for i in recipe.keys():

	# if key exist in ingredients and is less than or = to igredients then we have enoughfor 1 batch
		if i in ingredients and recipe[i] <= ingredients[i]:
		# save batch count to ingredient batch list
			batches.append(ingredients[i] // recipe[i])

		else:
			return 0

	# find smallest batch number
	return min(batches)



if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))




# 1st attempt:
	# # create arrs to store values to iterate through
	# recipe_arr = []
	# ingred_arr = []
	# batches = 0
	


	# # loop through recipe.items()
	# for i in recipe.items():
	# 	print("I am items: ", i[1])
	# 	recipe_arr.append(i[1])
	

	# for j in ingredients.items():
	# 	print("I am items: ", j[1])
	# 	ingred_arr.append(j[1])


	# print(recipe_arr)
	# print(ingred_arr)

	# for r, i in list(zip(recipe_arr, ingred_arr)):

	# 	if recipe_arr[r] <= ingred_arr[i]:
	# 		batches = r
	# 		print("r", r)
	# 		print("i", i)
	# 		print("batches: ", batches)
	# 	else:
	# 		print("we can not make a batch")

