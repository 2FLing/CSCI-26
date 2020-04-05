# This programs simulate table or database processing. The 'toons' data
# structure (a list of dictionaries) is updated so:
#   1) it creates a new field called 'greeting' with his/her salutation
#   2) it updates the 'gender' field with the full value
#   3) it adds a new field called 'address' and fills it with 'Toontown'

# toons = [{'fname':'Mickey', 'lname':'Mouse', 'gender':'m'},
#          {'fname':'Minnie', 'lname':'Mouse', 'gender':'f'},
#          {'fname':'Yosemite', 'lname':'Sam', 'gender':'m'}]
         
# def update_toons(toons):
#     for toon in toons:
#         toon['greeting'] = ' '.join(['Mr' if toon['gender'] == 'm' else 'Ms',
#                                      toon['fname'],
#                                      toon['lname']])
#         toon['gender']   = 'male' if toon['gender'] == 'm' else 'female'
#         toon['address']  = 'ToonTown'

# update_toons(toons)

# print(toons)
# ==> [{'fname':'Mickey', 'lname':'Mouse', 'gender':'male', 'greeting':'Mr Mickey Mouse', 'address':'ToonTown'},
#      {'fname':'Minnie', 'lname':'Mouse', 'gender':'female', 'greeting':'Ms Minnie Mouse', 'address':'ToonTown'},
#      {'fname':'Yosemite', 'lname':'Sam', 'gender':'male',  'greeting':'Mr Yosemite Sam', 'address':'ToonTown'}]
# After you have tested the program, delete the lines of code above and
# "uncomment" your template below. When you finish adding your FP code,
# it should print identically as before
from functools import reduce
from copy import deepcopy

# Your code goes here: It should have these new functions: pipeline,
# create_greeting, update_gender, create_address. It should have
# another function that creates a new 'toons' structure using deepcopy
toons = [{'fname':'Mickey', 'lname':'Mouse', 'gender':'m'},
        {'fname':'Minnie', 'lname':'Mouse', 'gender':'f'},
        {'fname':'Yosemite', 'lname':'Sam', 'gender':'m'}]
def pipeline(toons,)
print (pipeline(toons, [create_greeting,
                       update_gender,
                       create_address]))