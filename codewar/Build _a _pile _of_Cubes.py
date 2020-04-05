def find_nb(m):
    n=1
    sum=0
    while(sum!=m):
        if(n>m):
            n=0
            break
        sum+=pow(n,3)
        n+=1
    return n-1

print(find_nb(40539911473216))