# a = 9 
# print(a + 11*a + 111*a + 1111*a)

# inch = 2.54 
# centimeters = int(input('inch'))
# print('{.2f}cm')


# name = "철수"
# print(f"""
# "안녕, 철수야"
# """)

# from sympy import Symbol, solve

# x=Symbol('x')

# equation = 1*x**2 + 4*x - 21
# solve = equation

# import math
# a = 0.1*3
# b = 0.3
# math.isclose(a, b)
# print(math.isclose(a, b))

# print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다." \n 나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')


a = 1
b = 4
c = -21
print((-b + (b**2 - 4*a*c)**(1/2)) / 2*a)
print((-b + (b**2 + 4*a*c)**(1/2)) / 2*a)



# my_str = "Life is too short, you need python"
# a = ['a', 'e', 'i', 'o', 'u']
# for i in a:
#     my_str = my_str.replace(i, '')
# print(my_str)

# name = "철수"
# print(f'\"안녕, {name}야\"')




# daum = 89000
# naver = 751000
# total = (daum * 100) + (naver * 20)
# print(total)


# lost_total = (daum * 0.05 * 100) + (naver * 0.1 * 20)
# print(lost_total)

# F = 50
# C = (F-32) / 1.8
# print(C)



# print('pizza\n' * 10)


# monday_naver_price = 1000000

# blood_types = {'A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB'}
# for key in blood_types:
#     print(key)


blood_types = {'A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB'}

blood_dict = {}
for blood in blood_types:
	if blood_dict.get(blood):
		bblood_dict[blood] += 1
	else:
		blood_dict[blood] = 1
print(blood_dict)


blood_dict = {}
for blood in blood_types:
	blood_dict[blood] = blood_types.count(blood)
print(blood_dict)