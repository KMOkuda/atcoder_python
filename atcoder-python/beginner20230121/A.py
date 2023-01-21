'''
Created on 2023/01/21
'''

swap = input().split()

from1 = int(swap[1]) - 1
to1 = int(swap[2])
from2 = int(swap[3]) - 1
to2 = int(swap[4])



num = input().split()

num[from1:to1], num[from2:to2] = num[from2:to2], num[from1:to1]


print(*num)



