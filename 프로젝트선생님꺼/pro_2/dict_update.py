#.update()
a = {}

# 1
a.update(key='value')

# 2
a.update({key: value})


# .env 환경변수 세팅(python-decouple)

NAVER_CLIENT_ID=''
NAVER_CLIENT_SECRET=''



#네이버 요청하는법
#1-1
import requests
from decouple import config

CLIENT_ID = config(NAVER_CLIENT_ID)
CLIENT_SECRET = config(NAVER_CLIENT_SECRET)
HEADERS = {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}


# 1- 2요청 보내기
url = 'https://openapi.naver.com/v1/search/movie.json'
address = f'{url}?query={movieNm}'
response = requests.get(address, headers=HEADERS).json()


# 3 이미지 파일 저장하기
# 3-1 movie_naver.csv 여기서 영화코드랑 썸네일 url

# 3-2 요청보내서 응답을 작성하기 

url = 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1731/173123_P06_135928.jpg'

for in 
with open(f'images/test.jpg', 'wb') as f:
    response = requests.get(url).content
    f.write(image)
