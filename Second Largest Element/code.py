numbers = [25,128,56,13,6]
length = len(numbers)
max_element = numbers[0]
for i in range (0,length):
    if(numbers[i]>max_element):
        max_element=numbers[i]
second_element = -1
for j in range(length):
    if(numbers[j] > second_element and max_element!=numbers[j]):
        second_element = numbers[j]
print(second_element)