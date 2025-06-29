import matplotlib.pyplot as plt
import numpy as np
x=0.00001
a=[0.00001]
b=[0]
for i in range(100):
    x=x-(((np.exp(-x)+np.log(x))/(-(np.exp(-x))+(1/x))))
    print(x)
    a.append(x)
    b.append(i+1)
n = np.linspace(0,5, 1000) 
    
plt.plot(n,((np.exp(-n)+np.log(n))))
plt.plot(b,a)
plt.show()

