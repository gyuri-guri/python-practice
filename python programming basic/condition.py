
## 조건문의 이해 및 활용
if 6 >= 5 :
    print('6 is greater than 5')
    print('Yeah, it is true')
    print('This code is not belongs to if statements')

if 6 == 5:
    print('6 is greater than 5')
    print('Yeah it is true')
    print('it is really true')       # IF절이 Ture가 아니므로 결과 x



### logical AND, OR, NOT : 조건문에 상요되는 조건의 경우 논리식 사용 가능 
### 논리표 AND -> T AND T :T, T AND F : F, F AND T : F, F AND F :F
###        OR  -> T OR T : T, T OR F : T, F OR T : T, F OR F : T
###        NOT -> NOT T : F, NOT F : T
### 우선순위 NOT > AND > OR
a = 10
b = 8
c = 11
if a == 10 and b != 9:
    print('that is true. T and T = T')

if a == 10 and b == 9:
    print('that is true, T AND F = F')

if a == 10 or b == 9 : 
    print('that is true. T OR F = T')

if a == 10 or b == 9 and c == 12 :
    print('that is true. AND > 0R')

if (a == 10 or b == 9) and c == 12 :    # 우선순위 변경
    print('that is true. OR > AND')



 ### if의 조건이 book이 아닌 경우
 ### 조건문에는 주로 book이 주로 위치하지만 정수,실수,문자열 리스트 등 기본 타입도 가능
 ### false로 간주되는 값 : none, 0, 0.0, '':빈문자열, []:빈리스트, ():빈튜플, {}:빈딕셔너리, set():빈집합   
 ### 이 외에는 모두 true로 간주
if 3.5:
     print('3333')

a = 0
if a:
    print('a is not zero')

a = [1,2,3]
if a:
    print('a is list')

a = []
if a:
    print('false')



### if,else
#### 이문법에서 사용되며 if가 아닌 나머지 조건은 else 사용
#### 단, if와 else사이에 다른 코드는 삽입 불가

a = 11
if a%2 == 0 :
    print(a/2)   # 2로 나눠서 0이면 a/2 출력
else:
    print(a+1)   # 2로 나눠서 0이 아니면 a+1 출력



### if,elif,else
#### 조건이 여러개일 경우 elif에 명시
#### 각 조건을 확인 후 True 조건의 코드블락을 실행 후 전체 if.elif.else 문 종료
#### 모두 쌍으로 적용되며 조건은 if,elif문에만 사용.
#### elsee는 '그 외 조건'의 의미이며 조건은 쓰지 않음
#### 무조건 if > elif > else

a =  16
if a%4 == 0:
    print('a is divicible by 4')
elif a%4 == 1:
    print('a % 4 is 1')
elif a%4 == 2:
    print('a % 4 is 2')
else:
    print('a % 4 is 3')

#### if만 쓰면 if마다 비교하여 출력. false이면 pass
if a%4 == 0:
    print('a is divisible by  4')
if a%4 == 1:
    print('a % 4 is 1')
if a%4 == 2:
    print('a % 4 is 2')
else: 
    print('a % 4 is 3')



### 중첩 조건문(nested condition)
a = 10
b = 9
c = 8

if a == 10:
    if c ==  8:
        if b == 8:
            print('a is then and b is eight')
        else:
            print('a is ten and b is not eight')  # 마지막 if 문이 false 임으로 else문 출력
        