# from random import randint
# dice1 = list()  # history of dice1 as entries in a list
# dice2 = list()  # history of dice2 as entries in a list 
# win = False     # weither last throw was a boxcar

# def roll(d):
#   d.append(randint(1,6))  # simulate rolling a dice, by pushing a 1-to-6 into list
#   return

# while not win:
#   roll(dice1)
#   roll(dice2)

#   if  dice1[-1] == 6 and dice2[-1] == 6:
#     win = True

# print(dice1)   # print history
# print(dice2)   # print history
# print('Boxcars in', len(dice1), 'throws')

## (delete above and uncomment & fix up below)
from random import randint
from copy import deepcopy
def printhistory(state):
  print(state['dice1'])
  print(state['dice2'])
  print('Boxcars in', len(state['dice1']), 'throws')

def nextthrow(state):
  # **** Your code goes here ****
  fake_state=copy.deepcopy(state)
  fake_state['dice1'].append(randint(1,6))
  fake_state['dice2'].append(randint(1,6))
  if(fake_state['dice1'][-1]==6 and fake_state['dice2'][-1]==6):
    return fake_state
  else:
    return nextthrow(state)
printhistory(nextthrow({'dice1':list(), 'dice2':list()}))