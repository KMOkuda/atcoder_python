'''
Created on 2023/01/15
'''

N = int(input())
S = input()

#len(S)=6の場合

for i in range(0, len(S) - 1):#0 <= i <= 4
    answer = len(S) - i - 1#6 - 0 - 1 = 5     6 - 4 - 1 = 1
    for j in range(0, len(S) - 1 - i):
        if(S[j] == S[j + i + 1]):
            answer = j
            break
    print(answer)