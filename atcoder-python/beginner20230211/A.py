'''
Created on 2023/02/11
'''

s = input()

answer = ""

for i in range(len(s)):
    if(s[i] == "1"):
        answer += "0"
    else:
        answer += "1"

print(s)
