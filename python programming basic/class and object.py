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



### self
#### 파이썬의 method는 항상 첫번째 인자로 self를 전달
#### self는 현재 해당 매쏘드가 호출되는 객체 자신을 가리킴
#### 이름이 self 인것은 관용적인 표현이며 꼭 self일 필요는 없음.
#### 위치는 항상 맨 청므의 parameter임

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sleep(self):
        print(self.name, '은 잠을 잔다')

a = person('bob','20')

print(a)
a.sleep()



### Method 정의
#### 멤버함수라고도 하며 해당 클래스의 object에서만 호출가능
#### method는 객체 레벨에서 호출되며, 해당 객체의 속성에 대한 연산을 행함
#### {obj}.{method}()형태로 호출됨
class counter : 
    def __init__(self):
        self.num = 0
    def print_current_value(self):
        print('현재값은:',self.num)
    def increment(self):
        self.num += 1
    def reset(self):
        self.num = 0

c1 = counter()
c1.print_current_value()
c1.increment()
c1.increment()
c1.print_current_value()

c1.reset()
c1.print_current_value()



### method type
#### instance method - 객체로 호출 : 메쏘드는 객체 레벨로 호출 되기 때문에, 해당 메쏘드를 호출한 객체에만 영향을 미침
#### class method - class로 호출 : 클래스 레벨로 호출되기 때문에 클래스 멤버 변수만 변경 가능

##### 다음은 class method가 사용된 경우이다.
class math : 
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def multiply(a,b):
        return a * b
    
print(math.multiply(3,5))
print(math.add(3,5))



### class inheritance
#### 클래스 상속. 기존에 정의해둔 클래스의 기능을 그대로 물려받을 수 있음
#### 기존 클래스에 기능을 일부 추가하거나 변경하여 새로운 클래스를 정의함
#### 코드를 재사용할 수도 있음
#### 상속 받고자 하는 대상인 기존 클래스는 (parent, super, base class라고 부른다)
#### 상속 받는 새로운 클래스는 (child, sub, derived class)
#### 의미적으로 is-a관계를 가짐 

class person:
    def __init__(self, name, age):
            self.name = name
            self.age = age
    def eat(self, food):
        print('{}은 {}를 먹습니다'. format(self.name, food))
    def sleep(self, minute):
        print('{}은 {}분동안 잡니다'. format(self.name, minute))
    def work(self, minute):
        print('{}는 {}분동안 일 합니다'. format(self.name, minute))
    
class student(person):      # 기존 클래스(person)를 상속받은 새 클래스(student)
    def __init__(self,name,age):
        self.name = name
        self.age = age

class employee(person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

kate = student('kate',20)
suri = employee('suri',33)
kate.eat()   # food가 없어서 error
kate.eat('rice')
suri.work(500)



### method override
#### 부모 클래스의 method를 재정의(override)
#### 하위 클래스(자식 클래스)의 인스턴스로 호출시, 재정의된 메소드가 호출됨
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self, food):
        print('{}는 {}를 먹습니다'. format(self.name, food))
    def sleep(self, minute):
        print('{}는 {}분동안 잡니다'. format(self.name, minute))
    def work(self, minute):
        print('{}는 {}분동안 일합니다.'. format(self.name, minute))

class student(person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self, minute):
        print('{}는 {}분동안 공부합니다.'. format(self.name, minute))

class employee(person):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def work(self, minute):
        print('{}은 {}분동안 업무를 합니다.'. format(self.name, minute))


bob = student('bob',25)
bob.eat('BBQ')
bob.sleep(40)
bob.work(60)

moly = student('moly',30)
moly.eat('rice')
moly.sleep('60')
moly.work('200')




### super 
#### 하위클래스에서 부모클래스의 method를 호출할때 사용
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self, food):
        print('{}는 {}를 먹습니다'. format(self.name, food))
    def sleep(self, minute):
        print('{}는 {}분동안 잡니다'. format(self.name, minute))
    def work(self, minute):
        print('{}는 {}분동안 준비합니다.'. format(self.name, minute))


class student(person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self, minute):
        super().work(minute)
        print('{}은 {}분 동안 공부합니다'. format(self.name, minute))

class employee(person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self, minute):
        super().work(minute)
        print('{}은 {}분 동안 업무를 합니다'. format(self.name, minute))


bob = student('bob', 25)
bob.eat('cake')
bob.sleep(40)
bob.work(60)   # 두개의 결과가 나옴 

kate = employee('kate',42)
kate.eat('buger')
kate.sleep(50)
kate.work(100)  # 두개의 결과가 나옴



### special method
#### __로 시작해서 __로 끝나는 특수 함수
#### 함수 목록은 다음을 참고 https://docs.python.org/3/reference/datamodel.html
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, pt):
        new_x = self.x + pt.x
        new_y = self.y + pt.y
    
    def __add__(self, pt):
        new_x = self.x + pt.x
        new_y = self.y + pt.y
        return point(new_x, new_y)

    def __sub__(self, pt):
        new_x = self.x - pt.x
        new_y = self.y - pt.y
        return point(new_x, new_y)

    def __str__(self):
        return '({},{})' .format(self.x, self.y)

    def __mul__(self, factor):
        return point(self.x * factor, self.y * factor)

    def __len__(self):
        return self.x ** 2 + self.y ** 2


p1 = point(3,4)
p2 = point(2,7)        

print(p1)
print(p2)

p3 = p1+p2
print(p3)    # 정의한 class를 내장함수처럼 사용하기 

p4 = p1-p2
print(p4)

p5 = p1 * 3
print(p5)

print(len(p1))
