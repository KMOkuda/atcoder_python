'''
Created on 2023/02/04
'''

N, M = map(int, input().split())

connect_list = []
point_set = set()
connect_count = 0
circle_count = 0


for i in range(M):
    
    Abelongs = True
    Bbelongs = True
    
    A, B = map(int, input().split())
    
    if len(connect_list) == 0 or (A not in point_set and B not in point_set):
        connect_list.append(set([A , B]))
        point_set.add(A)
        point_set.add(B)
        continue
    
    if A not in point_set:
        Abelongs = False
    if B not in point_set:
        Bbelongs = False
    
    tmp = -1
    
    for i in range(len(connect_list)):
        if A in connect_list[i] and B in connect_list[i]:
            circle_count += 1
            break
        elif A in connect_list[i]:
            if Bbelongs == False:
                connect_list[i].add(B)
            elif tmp == -1:
                tmp = i
            else:
                connect_list[i].add(connect_list[tmp])
                del connect_list[tmp]
            break
        
    point_set.add(A)
    point_set.add(B)

print(circle_count)

