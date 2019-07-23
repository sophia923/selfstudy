'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

num = int(input('Enter a number: '))

if (num % 2) == 0:
    print('{0} is Even'.format(num))
else:
    print('{0} is Odd'.format(num))