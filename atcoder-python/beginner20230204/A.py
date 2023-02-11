'''
Created on 2023/02/04
'''

N = int(input())
add_list = []

for i in range(N):
    A, B = map(int, input().split())
    add_list.append(A + B)
    
for num in add_list:
    print(num)

