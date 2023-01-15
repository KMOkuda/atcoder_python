'''
Created on 2023/01/15
回答できず、、、
'''

N = int(input())

s = set()
common_list1 = []
common_list2 = []

original_list1 = []
original_list2 = []

count = 0
s2 = set()


for i in range(N):
    S, T = map(str, input().split())
    original_list1.append(S)
    original_list2.append(T)
    s.add(S)
    s.add(T)

for i in s:
    if i in original_list1 and i in original_list2:
        count += 1
    
    if count > 1:
        break

if count > 1:
    print("Yes")
else:
    print("No")
 