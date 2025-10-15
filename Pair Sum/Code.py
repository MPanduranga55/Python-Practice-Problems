# Problem statement
# You are given an integer array 'ARR' of size 'N' and an integer 'S'. Your task is to return the list of all pairs of elements such that each sum of elements of each pair equals 'S'.

# Note:

# Each pair should be sorted i.e the first value should be less than or equals to the second value. 

# Return the list of pairs sorted in non-decreasing order of their first value. In case if two pairs have the same first value, the pair with a smaller second value should come first.


# Sample Input 1:
# 5 5
# 1 2 3 4 5
# Sample Output 1:
# 1 4
# 2 3
# Explaination For Sample Output 1:
# Here, 1 + 4 = 5
#       2 + 3 = 5
# Hence the output will be, (1,4) , (2,3).
# Sample Input 2:
# 5 0
# 2 -3 3 3 -2
# Sample Output 2:
# -3 3
# -3 3
# -2 2

from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # Write your code here.
    ans = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]+arr[j]==s):
                pair = [min(arr[i],arr[j]) , max(arr[i],arr[j])]
                ans.append(pair)
    ans.sort()
    return ans
n = int(input())
arr = list(map(int,input().split()))
s = int(input())
ans = pairSum(arr,s)
for pair in ans:
    print(pair[0],pair[1])
