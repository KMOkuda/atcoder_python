'''
Created on 2023/02/11
'''

N, M = map(int, input().split())

answer = []

reten = list(map(int, input().split()))



if(M == 0):
    for i in range(N):
        answer.append(i + 1)
    
    print(*answer)
    exit(0)

if reten[0] > 1:
    for i in range(1, reten[0]):
        answer.append(i);


firstFlg = True   
from_index = last_index = reten[0]

for i in reten:
    if(last_index + 1 < i or reten[len(reten) - 1] == i):
        if reten[len(reten) - 1] == i:
            last_index = i
        for j in range(last_index + 1, from_index - 1, -1):
            answer.append(j)
        for j in range(last_index + 2, i):
            answer.append(j)
        from_index = i
        last_index = i
        
    else:
        last_index = i
        continue

if(reten[len(reten) - 1] != N - 1):
    for i in range(reten[len(reten) - 1] + 1, N):
        answer.append(i + 1)

print(*answer)

    