'''
Created on 2023/01/28
'''

N = int(input())
forNum = 0


for i in range(N):
    op = input()
    if(op == "For"):
        forNum += 1

if(forNum * 2 >= N):
    print("Yes")
else:
    print("No")