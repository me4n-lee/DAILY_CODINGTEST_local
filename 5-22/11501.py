# https://www.acmicpc.net/problem/11501
# 주식
# 11501

import sys
input = sys.stdin.readline

t = int(input())

def fun():

    benefit = 0
    max_stock = n_list[0]


    for i in range(1, n):
        if max_stock < n_list[i]:
            max_stock = n_list[i]
        
        benefit += max_stock - n_list[i]

    return benefit

for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.reverse()
    
    result = fun()
    print(result)