# https://www.acmicpc.net/problem/16401
# 과자 나눠주기
# 16401

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
n_list = list(map(int,input().split()))

# start = 1
# end = max(n_list)
# mid = (start + end) // 2

def fun():

    result = 0
    start = 1
    end = max(n_list)
    # for i in range(n):
    #     cnt += n_list[i] // mid
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(n):
            cnt += n_list[i] // mid

        if cnt >= m:
            result = mid
            start = mid + 1

        else:
            end = mid -1

    return result

answer = fun()
print(answer)


# print(n_list)
# answer = 0

# if m-1 < n:
#     answer = n_list[m-1]

# print(answer)

# def fun():

#     result = 0

#     for i in range(n):

#         cnt = 0

#         for j in range(n):
            
#             if m <= n:
#                 if n_list[i] <= n_list[j]:
#                     cnt += 1

#             #만약 조카의 수가 과자 수보다 많으면,
#             else:


#         if cnt == m:
#             answer = n_list[i]

#     return answer