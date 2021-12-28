
## 반복문의 이해 및 활용
### 특정 조건을 만족하는 경우 반복수행. 
### while 문을 써서  반복문 가능. 단, 반복을 멈추게 하는 장치가 필요



### while문
#### while뒤의 조건이 True일 경우 while 코드블럭 계속 수행
#### 조건이 False가 되면 반복 중지, 다음 코드 실행
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