
### 모듈 임포트
import requests        # HTTP 요청/응답 모듈
resp = requests.get('https://naver.com')
resp.text              # 네이버 홈의 html 추출

import math            # math : sin(), cos() 등
print(math.pi)
print(math.cos(100))



### from import
#### 모듈에서 특정한 타입만 import
from math import pi
from math import cos
print(pi)
print(cos(100))



### '* import'
#### 해당 모듈 내에 정의된 모든 것을 import
#### 권장되진 않음. 이름의 중복이 있을 수 있음
#### 모듈 전체를 import하는게 나음
from math import *
sin(100)



### as 
#### 모듈 import시, alias 지정가능
import math as m
m.exp(3)