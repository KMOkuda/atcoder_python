'''
Created on 2023/01/15
'''

S = input()
answer = 0

for i in range(len(S)):
    answer += (ord(S[len(S) - 1 - i]) - 64)  * (26 ** i)

print(answer)
