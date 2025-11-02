numbers = list(map(int,input().split()))
length = len(numbers)
for i in range(0,length):
    if numbers[i]<0:
        numbers[length-1] , numbers[i] = numbers[i] , numbers[length-1]
print(numbers)