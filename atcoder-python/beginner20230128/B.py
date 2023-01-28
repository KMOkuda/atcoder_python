'''
Created on 2023/01/28
'''

N, M = map(int, input().split())
nlist = []
count = 0
mset = set()

for i in range(N):
    nlist.append(int(input()) % 1000);

for i in range(M):
    num = int(input())
    mset.add(num)
    
for i in range(N):
    if(nlist[i] in mset):
        count += 1


print(count)
