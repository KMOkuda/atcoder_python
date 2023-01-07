'''
Created on 2023/01/07
 
'''
 
N, M = map(int, input().split())
point_list = []
 
for i in range(N):
    point_list.append([i + 1])
    
for i in range(M):
    # print(point_list)
    
    point1, point2 = map(int, input().split())
    point1_flg = -1
    point2_flg = -1
    
    
    if len(point_list) == 0:
        point_list.append([point1, point2])
        continue
    
    for j in range(len(point_list)):
            
        if point1 in  point_list[j]:
            point1_flg = j
        if point2 in  point_list[j]:
            point2_flg = j
    
    if point1_flg == point2_flg:
        continue
    else:
        point_list[point1_flg] = point_list[point1_flg] + point_list[point2_flg]
        del point_list[point2_flg]
 
print(len(point_list))