# %% 
## numpy, matplotlib의 이해 

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3])
y = np.array([2,4,6])

plt.plot(x,y)

## ndarray 생성하기 (with numpy)
### np.array
x = np.array([1,2,3,4]) # 1차원
print(x)

y = np.array([[2,3,4],[1,2,5]]) 
print(y)

print( type(y) )

### np.arange 
np.arange(10)
np.arange(1,10)
np.arange(1,10,2)
np.arange(5,101,5)

### np.ones, np.zeros
np.ones((4, 5))   # 튜플을 이용한 명시
np.ones((2, 3, 4))