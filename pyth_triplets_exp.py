import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
n=int(input())
p=[]
q=[]
r=[]
for a in range(1,n):
    for b in range(1,n):
        for c in range(1,n):
            if (((a**2)+(b**2))**(1/2))%1==0 and c==((a**2)+(b**2))**(1/2):
                p.append(a)
                q.append(b)
                r.append(c)
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d')
ax.plot(p, q, r, label='3D line') 
ax.legend()
plt.show()
aa=[]
print(p)
print(q)
print(r)
