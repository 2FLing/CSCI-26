from functools import reduce
### Lambda function
### write an equivalent lambda function and assigned it to the 'adder'
### variable. Then run the same print statement again and make sure
### you get the same output
# # def adder(x,y):
#   return x+y
adder=lambda x,y:x+y
print('The total is', adder(2,3))

### map() function
### rewrite this logic using an equivalent map() function. Rerun the
### print statement and check for same output
# vals = [1,2,3,4,5]
# dbls = []
# for x in vals:
#   dbls.append(x*x)
dbls=[n for n in map(lambda x:x*x,[1,2,3,4,5])]
print('The list elements been doubled', dbls)

### reduce() function
### rewrite this logic using an equivalent reduce() function. Rerun the
### print statement and check for same output. Remember functools
# vals = [1,2,3,4,5]

# sumofsquares = 0
# for x in vals:
#   sumofsquares += x*x
sumofsquares=reduce(lambda x,y:x+y,map(lambda x:x*x,[1,2,3,4,5]))
print('The sum of the square is', sumofsquares)

### closure technique
### combine the hi() and hello() functions into a common closure function
### that captures the greeting text as a bound variable. The closure function
### returns a specialized function that prints the saved 'Hi' or 'Hello'.
### Assign these return functions to the hi and hello variables. Call these
### hi and hello and check theat the results are identical
# def hi(name):
#   print ('Hi', name)
# def hello(name):
#   print ('Hello', name);
def say_hello():
    def hi(name):
        print ('Hi', name)
    def hello(name):
        print ('Hello', name)
    return (hi,hello)
hi,hello=say_hello()
hi('Sam')
hello('Alice')