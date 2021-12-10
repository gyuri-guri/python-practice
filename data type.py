
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


## LIST 와 TUPLE
### LIST와 TUEPLE 모두 여러개의 값을 데이터 구조
### LIST와 TUEPLE의 차이점 : LIST는 생성 후 변경가능(MUTABLE)
### LIST와 TUEPLE의 차이점 : TUPLE은 생성 후 변경불가능(IMMUTABLE)

a = [] # 빈 리스트 생성
a = [1,2,3,4,5,10]
a = ['apple','banana',1,23,[33,55]]  # 원소로 리스트도 가능

### 문자열을 리스트로 바꾸면?
a = 'hello world'
b = list(a)
print(a)
print(b)

### 튜플을 리스트로 바꾸면?
c = ('a','b','c')
d = list(c)
print(c)
print(d)

### split() : 구분자로 구분하여 리스트로 반환
a = 'hello world nice weather'
b = a.split()  # split('구분자')
c = a.split('o')
print(a)
print(b)
print(c)

## LIST INDEXING
a = [1,2,3,4,5,6]
print(a[0])
print(a[2])
print(a[-1])

## LIST UPDATE
### 일반 문자열은 불변이기에 추가하거나 대체만 가능. 
a = 'hello world'
b = 'b' + a[1:]   # 추가
c = a.replace('h', 'd')  # 대체
print(a)
print(b)
print(c)

### 리스트는 불변 가능이기에 인덱스를 이용한 수정 가능
a = [1,2,3,4,5,6,7]
a[0] = 200
a[5] = 555
print(a)

## LIST SLICING
a = [1,2,3,4,5,6,7,8,9,10]
print(a[4:7])
print(a[1:5:1])   # index:index:interval
print(a[1:6:2])

## LIST관련 함수
### append() : 리스트 끝에 항목 추가
a = [1,2,3,4,5]
a.append(8)
print(a)

### extend() : 리스트 연장. +,-로 가능함
a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
print(a)

c = [11,12,13,14,15]
c += b 
print(c)

### insert() : 항목추가
a = [1,2,3,4,5]
a.insert(1, 40)  # index, value
print(a)

### remove() : 항목삭제
a = [1,2,3,4,5]
a.remove(2)     #value
print(a)

a = [1,2,5,3,5]
a.remove(5)     # 지우려는 값이 여러개있으면 가장 앞 값 삭제
print(a)

### pop() : 지우고 싶은 아이템  반환 후 삭제
a = [1,2,3,4,5]
a.pop()      # index. default 값은 맨 마지막 값
print(a)

a.pop(1)
print(a)

b = a.pop(2)
print(b)        # 지운값을 다시 변수에 지정 가능

### index() : 찾고자하는 값의 인덱스 반환
a = [1,2,3,4,5]
a.index(2)

### in : 리스트 내 해당값 존재여부. value in [list] 
a = [1,2,3,4,5]
b = 7

c = b in a
print(c)

### list 정렬 
a = [10,7,3,5,15,13,17,15,14,19]
a.sort()       # 리스트 자체를 내부적으로 정렬
print(a)

a.sort(reverse = True)
print(a)
s
b = sorted(a)  # 정렬된 리스트의 복사본 반환
print(b)

## Tuple
c = (1,2,3)
c[0] = 100 
print(c)    # 튜플은 불변

d = (100,200)
print(type(d))

d = 100, 200
print(type(d))

a, b = 100, 200
print(a, b)
print(type(a), type(b))