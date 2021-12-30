## class와 object의 이해 
### class 
#### 속성(attribute)와 동작(method)을 갖는 데이터 타입
#### 특정기능을 하는 함수들과 변수들을 모아서 하나의 뭉텅이로 관리하여 새로운 태입처럼 만들어 데이터를 관리



### object(instance)
#### 클래스로 생성되어 구체화된 객체(인스턴스)
#### class가 틀이라면 object(instance)는 틀에의해 실체화 된 것, 또는 틀에 의해서 만들어진 것



### class 선언하기
#### 객체(object, instance)를 생성하기 위해서는 class 정의가 먼저 필요함
class person:
    pass      # 클래스 정의는 하되 구현은 비워놓을때 "pass"

james = person()
jack = person()

print(type(james),type(jack))



### init(self)
#### class의 instance가 생성될 때 호출됨
#### self는 항상 첫번째에 오며 자기 자신을 가리킴(기본 파라미터) _ 관례적으로 self가 이용됨
#### 해당 클래스에서 다루는 데이터를 정의함. 

class person:
    def __init__(self):
        print(self, 'is generated')
        self.name = 'kate'
        self.age = 10
        
p1 = person()
p2 = person()

print(p1.name, p1.age)

p1 = person()
p2 = person()

print(p1.name, p1.age)

p1.name = 'loopy'
p1.age = 5

print(p1.name, p1.age)



#### 동적 속성 생성
class person:
    def __init__(self, name, age = 10):   # age는 디폴트
        self.name = name
        self.age = age

p1 = person('bob',20)
p2 = person('bbororo')
p3 = person('krong',3)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)

