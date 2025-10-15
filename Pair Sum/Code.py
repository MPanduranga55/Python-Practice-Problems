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
