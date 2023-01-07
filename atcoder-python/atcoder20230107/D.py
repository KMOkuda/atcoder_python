'''
Created on 2023/01/07

'''
import math

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            if cnt != 1:
                arr.append([i, cnt])
                arr.append([temp, 1])
            else:
                arr.append([math.sqrt(temp), 2])
                arr.append([i, cnt])
            
            break
            
    return arr


num = int(input())

for i in range(num):

    N = int(input())
    
    fact_list = factorization(N) 
    
    # print(fact_list)
    
   
    print(str(int(fact_list[0][0])) + " " + str(int(fact_list[1][0])))
