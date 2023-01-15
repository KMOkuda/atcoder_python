'''
Created on 2023/01/15
'''

A, B = map(int, input().split())

if(A * 2 == B or A * 2 + 1 == B):
    print("Yes")
else:
    print("No")