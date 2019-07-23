print('Hello World')


print('Mary\'s cosmetics')

print('신씨가 소리질렀다. \"도둑이야\".')

print('\"C:\\Windows\"')

print ("오늘은", "일요일")


print('naver;kakao;sk;samsung')

print('naver/kakao/sk/samsung')

print('first', end=' ');print('second', end=' ')


string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(string))

s = "hello"
t = "python"
print(s + '!' +' '+ t)

print('Hi ' * 3)

t1 = 'python'
t2 = 'java'

print((t1 + ' ' + t2 + ' ') * 4)

# LG전자 주식을 10주 보유하고 있습니다. 금일 종가 20,000원일 경우 총 평가 금액을 화면에 출력하라.
print(20000 * 10)

print(2 + 2 * 3)

a = 128
print(type(a))

a = '128'
print(type(a))

# 데이터 타입을 문자열로 변경하는 함수
num = 100
num_str = str(num)

lang = 'python'
print(lang[0],lang[2])

license_plate = '24가 2210'
print(license_plate[4:8])

string = '홀짝홀짝홀짝'
print(string[::2])

string_1 = 'PYTHON'
print(string_1[::-1])

phone_number = '010-1111-2222'
phone_numbers = phone_number.replace('-', ' ')
print(phone_numbers)

url = 'http://sharebook.kr'
print(url[-2:])

string_2 = 'abcdfe2a354a32a'
strings_2 = string_2.replace('a', 'A')
print(strings_2)

# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 
# 영화 제목을 movie_rank 이름의 리스트에 저장하라. (순위 정보는 저장하지 않는다.)

movie_rank = ['닥터스트레인지', '스플릿', '럭키']
movie_rank.append('배트맨')
print(movie_rank)

movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

movie_rank.remove('럭키')
print(movie_rank)

movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
print(movie_rank)


lang1 = ['C', 'C++', 'JAVA']
lang2 = ['Python', 'Go', 'C#']

langs = lang1 + lang2
print(langs)


nums = [1, 2, 3, 4, 5, 6, 7]
print('max:', max(nums))
print('min:', min(nums))


nums = [1, 2, 3, 4, 5]
print(sum(nums))

# len() 함수는 문자열의 길이 뿐만 아니라 자료구조에 저장된 데이터의 개수 또한 계산할 수 있습니다.
cook = ['피자', '김밥', '만두', '양념치킨', '족발', '피자', '김치만두', '쫄면', '쏘세지', '라면', '팥빙수', '김치전']
print(len(cook))

nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

nums = [1, 2, 3, 4, 5]
print(nums[::-1])


# join() 메서드를 사용하면 모든 데이터를 이어붙여 하나의 문자열로 만들어 줍니다. 
# join 앞의 ' ' 비어있는 문자열을 눈여겨 보세요. 
# interset에 들어 있는 데이터를 문자열로 이어 붙일 때 데이터와 데이터 사이에 ' ' 공백을 삽입합니다.
interest = ['삼성전자', 'LG전자', 'Naver']
print(''.join(interest))

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))
print('/'.join(interest))
print('\n'.join(interest))

string = '삼성전자/LG전자/Naver'
interest = [string[0:4], string[5:9], string[10:15]]
print(interest)


# split() 메서드는 매개변수를 기준으로 문자열을 자르고, 남은 문자열을 리스트에 저장합니다. 
# 이 때 파라미터로 전달된 구분 문자 ('/')는 삭제돼서 리스트에 저장되지 않습니다.
interest = string.split('/')
print(interest)

interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)

interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
print(interest_0)

my_variable = ()

t = 1, 2, 3, 4
print(type(t))

t = ('a', 'b', 'c')
# uppder() 메서드를 사용해서 소문자를 대문자로 변경하고, 이를 새로운 튜플에 저장합니다.
t = (t[0].upper(), t[1], t[2])
print(t)


interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data)

interest = ['삼성전자', 'LG전자', 'SK Hynix']
change = tuple(interest)
print(change)

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a + b + c)


scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(scores)

*valid_score, _, _= scores
print(scores)

_, _, *valid_score = scores
print(scores)

icecream_price = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
print('메로나 가격:', icecream_price['메로나'])
del icecream_price['메로나']
print(icecream_price)

inventory = {'메로나': [300, 20], '비비빅': [400,3], '죠스바': [250,100]}
print(inventory['메로나'][0])
print(inventory['메로나'])
item = inventory['메로나']
print(item[0], '원')
print(item[1], '개')

# 84번 할 차례


def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")

