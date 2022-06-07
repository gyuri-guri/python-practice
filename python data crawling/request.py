## reuqest 모듈을 이용한 크롤링 


### request 모듈 
#### http reuqest/response를 위한 모듈 
#### HTTP method를 메소드 명으로 사용하여 request 요청 ex. get, post 
import requests


### get 방식 요청하기 
#### http get 요청
#### query parameter 이용하여 데이터 전달하기
#### 대부분의 경우가 get 방식에 해당됨 
url = 'https://news.v.daum.net/v/20190728165812603'
resp = requests.get(url)

resp  # <RESPONSE[200]> : 응답코드. 2XX -> 성공
resp.text  # 웹 페이지 소스를 열었을때 나오는 데이터와 같음


### post 방식 요청하기
#### 민감한 데이터를 포함한 경우 사용됨. 일반 페이지에서는 자주 사용되지 않음
#### http post 요청
#### post data 이용하여 데이터 전달하기
url2 = 'https://www.kangcom.com/member/member_check.asp'
data = { 
    'id' : 'matching22',
    'pwd' : 'test12345'
}
requests.post(url2, data = data)
resp.text


### HTTP header 데이터 이용
#### header 데이터 구성하기 
#### header 데이터 전달하기 
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
resp = requests.get(url,headers = headers)

resp.text   


### HTTP response 처릭하기
#### response 객체 이해
#### status_code 확인
#### text 속성 확인 
if resp.status_code == 200 :
    resp.headers
else :
    print('error')


