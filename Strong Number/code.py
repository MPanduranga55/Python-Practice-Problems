n = int(input())
temp = n
result = 0

while n>0:
    last_digit = n%10
    fact = 1
    for i in range(1,last_digit+1):
        fact*=i
    result+=fact
    n=n//10
if result == temp:
    print("Strong Number")
else:
    print("Not a Strong Number")