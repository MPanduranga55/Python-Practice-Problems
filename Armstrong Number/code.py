n = int(input())
duplicate_n = n
length = len(str(n))
result = 0
while n>0:
    last_digit = n%10
    result += last_digit**length
    n = n//10
if result == duplicate_n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")