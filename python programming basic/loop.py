
## 반복문의 이해 및 활용
### 특정 조건을 만족하는 경우 반복수행. 
### while 문을 써서  반복문 가능. 단, 반복을 멈추게 하는 장치가 필요



### while문
#### while뒤의 조건이 True일 경우 while 코드블럭 계속 수행
#### 조건이 False가 되면 반복 중지, 다음 코드 실행
from typing import Collection


a = [1, 10, 9, 24]
i = 0
while i < len(a):
    print('value: ', a[i], ', index: ', i)
    i += 1   # i를 하나씩 증가시키는 걸로 중지 장치 설정



### while 키워드를 이용하여 리스트의 아이템 출력하기 
#### case 1. 20 미만인 원소만 출력
a = [1, 10, 9, 24, 25, 26]
i = 0
while i < len(a):
    if a[i] < 20:
        print(a[i])
    i += 1          # 조건문에 들어가면 안됨. 

#### case 2. 홀수인 원소만 출력
i = 0
while i < len(a):
    if a[i]%2 != 0:
        print(a[i])
    i += 1



### break
#### loop를 중단할 때 사용
#### 조건문 안에서 사용이 되며 조건을 만족하면 loop를 탈출하는 구문임 
#### loop를 중단 하는 경우, while 이후의 코드를 실행함.
#### crawling을 할때 또는 반복될 범위를 모를 때 사용됨
a = [1, 10, 9, 24, 25, 26]
i = 0
while i < len(a):
    if a[i] > 20:
        break     # 조건이 만족되면 break 실행

    print(a[i])

    i += 1



### continue
#### continue가 사용되는 경우 while 조건으로 점프함
#### 특정 경우는 코드를 수행하지 않고 다음으로 건너뛰기 위해 사용

#### break절은 바로 중단됨.
a = 7
while a > 0:
    a =- 1
    if a == 5:
        break
    print(a)

#### continue는 while 조건 계속 실행
a = 7
while a > 0:
    a -= 1  
    if a == 5:
        continue
    print(a)


### 1~100 더하기
number = 1
number_sum = 0

while number <= 100:
    number_sum += number
    number += 1

print(number_sum)



### for 반복문 
#### 리스트나 문자열 등 순회 가능한 객체를 순회하며 값을 처리 
#### for문 안에서 변수사용은 주의해야함. 
a = [1,2,3,5,4]
for i in a:
    print(i,i*2)



#### 문자열 적용
a = 'hello world'
for character in a:
    print(character)



#### 리스트 적용
a = [1,4,2,5,6,3]
for num in a:
    print(num)



#### 조건문과 같이 사용
for num in a:
    if num%2 == 0:
        print(num/2)
    else:
        print(num+1)



#### dict(dictionary) 적용
##### dictionary의 경우 key값을 참조하며 순회.
##### key() : key값만 순회가능
##### values() : value만 순회가능
##### items() : tuple형태로 key,value 순회 가능
a = {'korea':'seoul','japan':'tokyo','canada':'ottawa'}
for k in a:
    print(k)      # key값 순회

for k in a:
    print(k, a[k])  # key,value 모두 순회

for v in a.values():
    print(v)        # value만 순회



#### for에서 index사용
a = [1,2,4,3,6]
for num in a:
    print(num)

for index, num in enumerate(a):
    print(index, num)             # 인덱스와 값 모두 출력

for index, num in enumerate(a):
    if index > 3 :
        print(index,num) 



##### break
###### 특정 조건일때 loop종료
a = [100, 90, 42,5,3,7]
for num in a:
    if num < 40:
        break
    print(num)



##### continue
for num in a:
    if num == 5:
        continue
    print(num)



#### loop 중첩
a = [4,5,3]
for i in a:
    for j in a:
        print(i+j)



#### 구구단 만들기
x = [2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]
for i in y:
    for j in x:
        print(i,'x',j,'=',i*j)



#### collection의 길이
##### len()함수로 길이 계산이 가능
a = [1,2,3,4,5]
print(len(a))
print(len('hello world'))        



#### range()
##### 리스트만들때 쉽게 만들 수 있음
print(range(100))
print(list(range(100)))    # 0 <= x < 100 
print(list(range(1,101)))  # 1 <= x <= 100

a = list(range(1,101))
print(a)

##### 1~100 사이의 5배수만 갖는 리스트 생성
print(list(range(5,101,5)))

##### 구구단 (while 버전)
x = 1
while x <= 9:
    y = 1
    while y <= 9:
        print(x,'x',y,'=',x*y) 
        y +=1
    x +=1

##### 최소값, 최대값 찾기
a = [33,4,56,3,65,2,47,86,3,13,4,15,65]
_min = a[0]
_max = a[0]

for x in a :
    if x < _min:
        _min = x
    if x > _max:
        _max = x
print(_min,_max)


##### 평균 구하기
i = 0
_sum = 0

while i < len(a):
    _sum += a[i]
    i += 1
print(_sum/len(a))

_sum = 0
for x in a:
    _sum += x
print( _sum / len(a))
