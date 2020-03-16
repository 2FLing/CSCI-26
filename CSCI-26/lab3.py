def pascal_triangle(n):
    line = [1]

    # Put your code here...
    for row in range(0,n):
        if(row==0):
            print(line)
        else:
            for i in range(0,row):   
                if(i==row-1):
                    a1=line[0]
                    line.append(a1)
                    l2=[_ for _ in line]
                    print(line)
                else:
                    a1=l2[i]
                    a2=l2[i+1]
                    line[i+1]=a1+a2
    return line
        
pascal_triangle(6)
## The output should look like this
## [1]
## [1, 1]
## [1, 2, 1]
## [1, 3, 3, 1]
## [1, 4, 6, 4, 1]
## [1, 5, 10, 10, 5, 1]
def evalTokens(tokens):
    # Evaluate RPN expression in 'tokens'
    stack = []

    # Put your code here (note: you will get error "pop from emply list"
    # if you just run the template without putting something in stack) 

    return stack.pop()

rpn = "3 1 -"                      # Test this first; make sure your answer is 2 and not -2
rpn = "19 2.14 + 4.5 2 4.3 / - *"  # Infix: (19 + 2.14) * (4.5 - 2 / 4.3); answer = 85.29...

rpn_tokens = rpn.split(" ")

result = str(evalTokens(rpn_tokens))
print('The Reverse Polish Notation is "' + rpn + '"')
print('The result is ' + result)   # should be 85.29744186046511 for above test line