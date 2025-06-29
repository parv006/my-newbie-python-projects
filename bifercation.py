# # n=int(input())
# import matplotlib.pyplot as plt
# import numpy as np
# # x=float(input('enter initial iteration'))
# x=0.4

# r = np.linspace(2.5,3.5, 1000) 
# p=[]
# q=[]
# for l in r:
#     for i in range(20):
#         x=l*x*(1-x)
#         p.append(x) 
#         q.append(l)
# print(p)   
# m=[]
# for t in range(1000):
#     m.append(p[19*t])
# print(len(q))
# print(len(m))    
# print(len(p))
# n=[]
# for j in range(1000):
#     n.append(q[19*j])
# print(q)
# # fig, ax = plt.subplots(1, 4, figsize=(15, 5))
# # ax[0].plot(p,q , color='red')
# # ax[0].legend()
# # ax[1].plot(q,m , color='blue')
# # ax[1].legend()
# # ax[2].plot(n,m , color='green')
# # ax[2].legend()
# # ax[3].plot(n,p , color='violet')
# # ax[3].legend()

# plt.plot(n,m)
# plt.show() 
# print(m)
import numpy as np
import matplotlib.pyplot as plt

# Parameters
r_min = 2.5
r_max = 4.0
r_values = np.linspace(r_min, r_max, 10000)
iterations = 1000
last = 100

# Prepare the bifurcation diagram data
x = 1e-5 * np.ones(len(r_values))

# Create the plot
plt.figure(figsize=(10, 7))
for i in range(iterations):
    x = r_values * x * (1 - x)
    if i >= (iterations - last):
        plt.plot(r_values, x, ',k', alpha=0.25)
        
plt.title('Bifurcation diagram')
plt.xlabel('r')
plt.ylabel('x')
plt.show()
