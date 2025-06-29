import matplotlib.pyplot as plt
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
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].plot(p,q , color='red')
ax[0].legend()
ax[1].plot(q,r , color='blue')
ax[1].legend()
ax[2].plot(r,p , color='green')
ax[2].legend()
plt.show() 
