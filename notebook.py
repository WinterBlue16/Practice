# from itertools import product
# a, b, c = map(int, input().split())
# def m(x):
#     X=[]
#     for i in range(x):
#         X.append(i)
#     return X
# lisum=[m(a), m(b), m(c)]
# a=list(product(*lisum))
# for i in range(len(a)):
#     v=list(a[i])
#     for i in range(len(v)):
#         print(v[i], end=' ')
#     print(' ')
# print(len(a)) # 84번 문제

# M = [[0 for col in range(19)] for row in range(19)]
# n = int(input())
# for i in range(n): 
#     i, j = map(int, input().split())
#     M[i-1][j-1] = 1 # 인덱스 번호를 좌표 번호와 일치시킨다
    
# for i in M:
#     print(" ".join(map(str, i))) # 리스트의 대괄호와 ,를 동시에 없애준다

print(ord('┌'))

print(chr(9484))
