'''
Created on 2023/01/14

'''

H, W = map(int, input().split())
str_list = []

for i in range(H):
    str_list.append(input())

N = int(input())

for i in range(N):
    A, B = map(int, input().split())