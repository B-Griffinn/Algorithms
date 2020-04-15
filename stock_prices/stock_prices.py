#!/usr/bin/python
import argparse


def find_max_profit(prices):

	# save min_indx and max index
	min_index = 0
	max_index = len(prices) - 1 # bc we can not sell Friday's stock


	# loop thru arr without last index bc thats friday 
	# and find the smallest
	for i in range(len(prices) - 1):

		if prices[min_index] > prices[i]:
			min_index = i
	
	# loop thru right side of arr from min_index in our arr
	for i in range(min_index + 1, len(prices) - 1):
		if prices[max_index] < prices[i]:
			max_index = i


	# return max difference btween max and min
	return prices[max_index] - prices[min_index]





if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))