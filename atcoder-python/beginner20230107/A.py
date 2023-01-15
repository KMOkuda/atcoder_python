'''
Created on 2023/01/07
 
'''
 
N = int(input())
strs = []
 
for i in range (N):
    strs.append(input())
 
strs.reverse()
 
for i in range (N):
    print(strs[i])