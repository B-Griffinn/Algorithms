#!/usr/bin/python

import sys

possible_plays = [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

def rock_paper_scissors(n, cache = possible_plays):
  if n <= 0:
    return [[]]
  elif n == 1:
    return [['rock'], ['paper'], ['scissors']]
  elif n == 2:
    return possible_plays
  print('Hello')
  return cache 

  # rock_paper_scissors(n * cache)
    # our list of lists needs to grow by `n` and show all possibilities need to grow by `n` as well

print(rock_paper_scissors(2))
print(rock_paper_scissors(3))



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')