
## 기본 데이터 타입 
### int (정수), float (실수), str (문자열), boolean (참거짓)

a = 'hello'
b = 5
c = 11.4
type(a)
type(b)

### NONE
#### 아무런 값을 갖지 않음. 타 언어의 NULL과 같음

d = None
print(d)

### 숫자형타입(정수,실수) 연산자

a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

c = 7
c -= 3   # or +=,*=,**=
print(c)


## 데이터 타입 1. STRING 문자열
a = 'hello world'
b = '"hello" world'
print(a)
print(b)

c = """hello
world"""
print(c)

### ESCAPE STRING 이스케이프 문자 
#### \n : new line (=enter).  \t : tab ...

print("hello world\n\n")
print('ha\thaha')

### INDEXING & SLICING STRIN 문자열 인덱스 및 추출
#### 인덱스란? 문자열 내 각 문자는 순서를 가지는데 이 순서를 인덱스라고 함 
#### 첫번째부터 0으로 시작

a = 'hello world'
print(a[1])
print(a[10])

#### 인덱스는 (-) 값도 사용 가능

print(a[0])
print(a[-1])
print(a[-11]) # = a[0]

### 문자열 SLICING
#### [start:end]를 명령하면 [start:end) 추출. 생략되어있다면 0부터 or 끝까지

a = 'hello world'
print(a[0:4])
print(a[0:11])
print(a[0:1])
print(a[:5])
print(a[3:])
print(a[:])

### 문자열 함수
#### 1. replace 문자열 치환
a = 'hello world'
a.upper()  # 대문자 변환
a.replace('h','j')

#### 2. format 문자열 내 특정 문자를 변수로부 초기화하여 동적 문자열 생성
a = '오늘 기온 {}이ㅣ고 비올 확률은 {}%d입니다'

temperature = 25.5
prob = 0.8
a = '오늘 기온은 {}이고, 비올 확률은 {}% 이다'.format(temperature, prob)
print(a)

### SPLIT
#### 특정한 문자 구분해서 리스트로 치환
a = 'Hello world what a nice weather'
a.split ()
a.split('w')   # 구분자 설정









