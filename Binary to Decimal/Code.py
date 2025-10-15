n = int(input())
decimal_number = 0
power = 0
while(n>0):
    last_digit=n%10
    decimal_number+=(2**power)*last_digit
    n=n//10
    power +=1
print(decimal_number)