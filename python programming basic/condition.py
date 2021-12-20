
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

### 아 겁나 하기 싫네 
