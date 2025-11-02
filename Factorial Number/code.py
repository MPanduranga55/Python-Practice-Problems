def factoiral_number(n):
    if(n==0 or n==1):
        return 1
    elif(n<0):
        return "Error"
    else:
        return n*factoiral_number(n-1)
n=int(input())
print(factoiral_number(n))










