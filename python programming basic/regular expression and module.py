

## 정규표현식
### r : raw string
a = 'hello world\nwelcome'
print(a)

a = r'hello world\nwelcome'   # \n을 문자열 그대로 반환
print(a)

### 정규표현식 정리
### . : 어떠한 한개의 character와 일치(newline 제외)
### \w : 문자 character와 일치
### \s : 공백문자와 일치
### \t, \n, \r : tab, newline, return
### \d : 숫자 character와 일치
### 등등

### search method
import re

m = re.search(r'abc','123abcdef')  # re.search(찾고자하는 정규식 패턴, 찾을 대상)
print(m)
type(m)                            # match라는 객체이며 start,end,group 등의 함수가 포함되어있음
print(m.start())
print(m.end())
print(m.group())

n = re.search(r'\d\d\d\w','111abcdef119')
print(n)
n

b = re.search(r'abc','123abdef')
print(b)                          # 패턴이 없으면 none

