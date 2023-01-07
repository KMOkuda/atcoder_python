'''
Created on 2023/01/07
 
'''
 
N = int(input())
nums = []
 
for i in range (N):
    M = int(input())
    odd_count = 0
    l = list(map(int, input().split()))
    for j in range (len(l)):
        if l[j] % 2 == 1:
            odd_count = odd_count + 1
    nums.append(odd_count)
 
for i in range(N):
    print(nums[i])
 
'''
Created on 2023/01/07

'''

N = int(input())
nums = []

for i in range (N):
    M = int(input())
    odd_count = 0
    l = list(map(int, input().split()))
    for j in range (len(l)):
        if l[j] % 2 == 1:
            odd_count = odd_count + 1
    nums.append(odd_count)

for i in range(N):
    print(nums[i])
    