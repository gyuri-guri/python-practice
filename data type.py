
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


## Dictionary
### '키'와 '값'의 구조. '키'는 내부적으로 hash값으로 저장(동일 키 존재 불가)
### 인덱스가 없으므로 순서를 따지지않음

a = {'apple':'red','banana':'yellow','watermelon':'green','strawberry':'red','lemon':'yellow'}
print(a)
print(a[1])  # error. dictionary는 인덱스를 갖고있지 않음
print(a['apple'])

### dictionary타입의 항목 추가 및 변경

a['tomato'] = 'red'
a['orange'] = 'orange'
a['watermelon'] = 'black&green'
print(a)

### update() : 두 dictionary를 병합. 겹치는 키가 있다면 parameter로 전달되는 키 값으로 덮어짐

a = {'a':1, 'b':2,'c':3}
b = {'a':2, 'b':4, 'e':5}
a.update(b)
print(a)

### del(), pop() : key삭제

a.pop('b')
print(a)
del a['c']
print(a)

### clear() : Dictionary 모든 값 초기화

print(a)
a.clear()
print(a)

### IN() : key값 존재 확인. true or false

a = {'a':1,'b':2,'c':3}
print(a)
b = [1,2,3,4,5,6,7,8,9,10]
print(100 in b) # 리스트 내 원소 개수가 많으면 비효율
print('b' in a)
print(2 in a)

### 값 출력 : dictionary명[key명] 또는 get()

a['b']
print(a.get('b'))
print(a.get('d'))  # 값이 없으면 None
print(a['d'])      # error

### 모든 key,values

print(a)
print(a.keys())
print(a.values())
print(list(a.keys()))
print(list(a.values()))
list(a.items())          # 튜플형식으로 출력


## SET
### KEY만 활용하는 구조. 수학에서의 집합과 같은 개념. 중복불가하며 순서가 없음

a = {1,1,2,3,4,1,5}
print(a)
print(a[1])    # error. 인덱스 없음

### set() : 집합으로 변환

a = [1,1,2,3,3,4,1,5]
print(a)
b = set(a)
print(b)

### 집합의 연산

a = {1,2,3}
b = {2,3,4}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.issubset(b))      # 부분집합 판단(T/F)
