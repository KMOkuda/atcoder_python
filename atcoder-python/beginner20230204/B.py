'''
Created on 2023/02/04
'''

N, K = map(int, input().split())

dict_list = []

for i in range(N):
    name = input()
    if(i < K):
        dict_list.append(name)
    

dict_list.sort()

for i in range(K):
    print(dict_list[i])
