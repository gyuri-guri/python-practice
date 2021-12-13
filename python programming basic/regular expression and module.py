

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
print(b)                      # 패턴이 없으면 none

m = re.search(r'\d\d', '112abcde119')
print(m.start())
print(m.end())

mm =re.search(r'\d\d\d\w','111abcdef119')
mm

### [] : 문자들의 범위를 나타내는 용도
#### [abck] : a or b or c or k
#### [abc.^] :a or b or c or . or ^
#### [a-d] : 해당 문자 사이의 범위에 속하는 문자 중 하나 
#### [0-9] : 모든 숫자
#### [a-z] : 모든 소문자
#### [A-Z] : 모든 대문자
#### [a-zA-Z0-9] : 모든 알파벳 문자 및 숫자
#### [^0-9] : ^가 맨 앞에 오면 해당 문자 패턴이 아닌 것과 매칭(=NOT)

print(re.search(r'[cbm]at','cat'))  # c or b or m이고 at인 패턴
print(re.search(r'[cbm]at','mat'))
print(re.search(r'[cbm]at','aat'))  # none

print(re.search(r'[0-9]haha','1hahaha'))
print(re.search(r'[0-9]haha','1ahahaha')) # none

print(re.search(r'[abc.^]aron','caron'))
print(re.search(r'[abc.^]aron','^aron'))
print(re.search(r'[abc.^]aron','daron'))  # none

print(re.search(r'[^abc]aron','aaron'))   # none
print(re.search(r'[^abc]aron','#aron'))
print(re.search(r'[^abc]aron','8aron'))

### 다른 문자와 함께 사용되어 특수한 의미를 지님 
#### \d : 숫자. (=[0-9])
#### \D : 숫자가 아닌 문자 (=[^0-9])
#### \s : 공백 문자
#### \S : 공백이 아닌 문자
#### \w : 알파벳 대소문자 (=[^0-9a-zA-Z])
#### \W : 알파벳과 문자 제외 (=[^0-9a-zA-Z])

print(re.search(r'\sand','.apple and banana'))
print(re.search(r'\Sand','apple and banana'))  # none
print(re.search(r'\Sand','apple .and banana'))  

### . : 모든 문자
print(re.search(r'.and','.and'))
print(re.search(r'.and','pand'))

### .을 자체로 인식시키기
print(re.search(r'\.and','.and'))
print(re.search(r'\.and','pand'))  # none

### 반복패턴 : 가능한 많은 부분이 매칭됨
#### '+' : 1번 이상 패턴 발생
#### '*' : 0번 이상 패턴 발생
#### '?' : 0 혹은 1번의 패턴 발생
re.search(r'a[bcd]*b','abcbdccb')
re.search(r'b\w+a','banana')
re.search(r'\i+','pilgii')


### ^ : 문자열 맨 앞부터 일치하는 경우 검색
### $ : 문자열 맨 뒤부터 일치하는 경우 검색
print(re.search(r'b\w+a','cabana'))
print(re.search(r'^b\w+a','cabana'))  # none
print(re.search(r'^b\w+a','babana'))
print(re.search(r'b\w+a$','cabana'))

### grouping
#### ()을 사용하여 그루핑
#### 매칭 결과를 각 그룹별로 분리 가능
#### 패턴 명시 할때 각 그룹을 괄호() 안에 넣어 분리하여 사용 
m = re.search(r'\w+@.+','test@gmail.com')
print(m.group())

m = re.search(r'(\w+)@(.+)','test@gmail.com')
print(m.group(0))
print(m.group(1))
print(m.group(2))

### {} : *,+,?를 사용하여 반복적인 패턴을 찾는 것은 가능하나, 반복 횟수 제한은 불가
###     {}에 숫자를 명시하면 숫자 만큼의 반복인 경우에만 매칭
print(re.search('pi{3}g','piiig'))
print(re.search('pi{3}g','piiiig'))    # none
print(re.search('pi{3,5}g','piiiig'))  # 최소 3개 최대 5개 

### 미니멈 매칭(non-greedy way) : *?, +? 를 이용하여 미니멈 매칭
print(re.search(r'<.+>','<html>haha</html>'))
print(re.search(r'<.+?>','<html>haha</html>'))

### {}? : {m,n} => m번에서 n번 반복하나 가능한 많이 매칭됨
###       {m,n}? => 최소 m번만 매칭하면 만족
print(re.search(r'a{3,5}','aaaa'))
print(re.search(r'a{3,5}?','aaaa'))

### match : search와 유사하나, 주어진 문자열의 시작부터 비교하여 패턴이 있는 지 확인
###         시작부터 패턴이 존재하면 none 반환
re.match(r'\d\d\d','my number is 123')  # 앞에서부터 비교
re.match(r'\d\d\d','123 is my number')
re.match(r'^\d\d\d','123 is my number')

### findall : 매칭되는 전체 패턴 반환. 모든 결과를 리스트 형태로 반환
re.findall(r'[\w-]+@[\w.]+','test@gamil.com haha test222@gmail.com nice to meet you')
re.findall(r'\w+@[\w.]+',' test@gmail.com haha test22@gmail.com nice to meet you')

### sub : 주어진 문자열에서 일치하는 모든 패턴을 replace
###       결과를 다시 문자열로 반환. 두번째 인자는 문자열 or 함수
###       count가 0인 경우 전체, 1이상 해당 숫자만큼 치환
re.sub(r'\w+@[\w.]+','great','test@gmail.com haha test2@gmail.com nice test')             # 모두대치
re.sub(r'\w+@[\w.]+','great','test@gamil.com haha test2@gmail.com nice test', count = 1)  # 첫번째 문자만 대치

### compile : 동일한 정규표현식을 써야할때 유용함.(한번만들어서 저장 후 사용 가능)
###           해당 표현식을 re.RegexObject객체로 저장하여 사용가능
email_reg = re.compile(r'\w+@[\w.]+')
print(email_reg.search('test@gmail.com ahah good'))
print(email_reg.findall('test@gmail.com ahah good'))