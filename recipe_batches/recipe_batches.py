#!/usr/bin/python

import math

# recipe & ingredients arguments needs to be a dict
# dicts need to be in the same form

# what I understand:
# - values in ingredients must be >= values in the recipe before we check how many batches we can make
	# - or if keys do not match

# - use a dict method .items() in order to iterate through recipe/ingredients
# - use our_recipe items in order to compare recipe to ingredients needed
# - batch variable to track number of possible batches

# - min loop == 1 in order to see if our first item in recipe is <= first item in ingredient

def recipe_batches(recipe, ingredients):

	batches = {}
	num_of_possible_batches = 0

	# loop through recipe
	for key in recipe.keys():
		# print("I am the keys: ", key)
		# print("I am the values: ", recipe[key])

		# compare keys in recipe to keys in ingredients
		if key in ingredients and recipe[key] < ingredients[key]:
			
			# find possible num of baches and udpated batches var


			print("Key: ", recipe[key])
		else:
			# no possible batches if we get here
			return 0
		

		

	# loop trhough batches and do math
	return "Return statement"
	
	
print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1500, 'flour': 40, 'sugar': 100, 'butter': 50} ))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
