# print("""\    /\\
#  )  ( ')
# (  /  )
#  \(__)|""")
#
# 
# A, B = map(int, input().split())
# 
# result_1 = A - B
# result_2 = A * B
# result_3 = A // B
# result_4 = A % B
# print( A + B)
# print(result_1)
# print(result_2)
# print(result_3)
# print(result_4)
# print('{} \n{}'.format(A+B, A-B))
# a = '강한친구'
# b = '대한육군'
# print('{} {}'.format(a, b))
# print('{} {}'.format(a, b))
#
# print('강한친구 대한육군')
# print('강한친구 대한육군')

# A, B, C = map(int, input().split())
# print((A+B)%C)
# print((A%C + B%C)%C)
# print((A*B)%C)
# print((A%C * B%C)%C)
#
# A= int(input())
# D, E, F = map(int, input())
# print(A * F)
# print(A * E)
# print(A * D)
# print(A * (D*100 + E*10 + F))

# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# a = int(input())
# if a >= 90:
#     print('A')
# elif a >= 80:
#     print('B')
# elif a >= 70:
#     print('C')
# elif a >= 60:
#     print('D')
# else:
#     print('F')


# a = int(input())
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print('1')
# else:
#     print('0')

#
# H, M = map(int, input().split())
#
# M -= 45
# if M < 0:
#     H -= 1
#     if H < 0:
#         H = 23
#     M = 60+M
# print(H, M)
#
# print("""|\\_/|
# |q p|   /}
# ( 0 )\"""\\\
# \n|"^"`    |
# ||_/=\\\\__|""")
#
# A, B, C = map(int, input().split())
# print((A+B)%C)
# print((A%C + B%C)%C)
# print((A*B)%C)

# print((A%C * B%C)%C)

# A = int(input())
# B, C, D = map(int, input())
# print(A * D)
# print(A * C)
# print(A * B)
# print(A*(D + (10*C) + (100*B)))
#
# A, B = map(int, input().split())
# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# else:
#     print('==')

# N = int(input())
# if N >= 90:
#     print('A')
# elif N >= 80:
#     print('B')
# elif N >= 70:
#     print('C')
# elif N >= 60:
#     print('D')
# else:
#     print('F')
#
# N = int(input())
# if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
#     print('1')
# else:
#     print('0')
#
# H, M = map(int, input().split())
# M -= 45
# if H >= 0:
#     H -= 1
#     M = 60 + M
#     if H < 0:
#         H = 23
# print(H, M)

# a, b, c = map(int, input().split())
# if a <= b <= c:
#     print(b)
# elif a <= c <= b:
#     print(c)
# elif b <= a <= c:
#     print(a)
# elif b <= c <= a:
#     print(c)
# elif c <= a <= b:
#     print(a)
# elif c <= b <= a:
#     print(b)


# N = int(input())
# for i in range(1, 10):
#     Ni = N * i
#     print('{0} * {1} = {2}'.format(N, i, Ni))

# H, M = map(int, input().split()) # 현재 시간 입력 받기
# Hour = 0
# Minute = 0
# total_minute = H*60 + M # 현재 시간을 분으로 환산하기 ex) 3시 40분 = 3*60+40=220분
# adjust_time = total_minute - 45 # 45분 전 시간을 분으로 계산하기 ex) 220-45=175분
# if adjust_time < 0: # 하루의 시작이 0:0이므로 조정한 시간이 0보다 작으면 0시 0분으로 출력
#     print('0 0')
# else:
#     Hour, Minute = divmod(adjust_time, 60) # 아닌 경우 계산한 총 분을 60으로 나누어
#     print('{} {}'.format(Hour, Minute)) # 몫을 시간, 나머지를 분으로 계산한다.


# T = int(input())
# # print(A, B)
# for i in range(T):
#     A, B = map(int, input().split())
#     print(A+B)

# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, input().split())
#     print('Case #{}: {}'.format(i, a+b))

# T = int(input())
# for i in range(1, T+1):
#     print(' '*(T-i) + '*'*i)

N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
for i in range(N):
    if A[i] < X:
        print(A[i], end=' ')
    # if A < X:
    #     result.append(A)
    # print(result)

