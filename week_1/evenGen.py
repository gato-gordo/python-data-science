import random
def genEven():
  ''' Returns a random even number x, where 0 <= x < 100'''
  # Your code here
  return random.choice(range(0, 100, 2))
