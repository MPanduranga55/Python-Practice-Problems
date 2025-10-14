list1 = ["happy","joy","cheer","enjoy"]
list2 = ["cheer","enlight","enjoy","embrace"]
list3 = []
for char in list1:
    for word in list2:
        if char==word:
            list3.append(char)
for words in list3:
    print(words)