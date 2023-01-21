'''
Created on 2023/01/21
'''

N, X = map(int,input().split())
dx = []
dx.append({0})

for i in range(N):
    A, B = map(int,input().split())
    
    for j in range(B):
        dx.append({0})
        for k in (dx[len(dx) - 2]):
            dx[len(dx) - 1].add(k)
            dx[len(dx) - 1].add(k + A)
        #print(*dx[len(dx) - 1])  
        
        
if X in dx[len(dx) - 1]:
    print("Yes")
else:
    print("No")
