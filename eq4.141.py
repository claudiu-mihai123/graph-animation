import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
theta=np.linspace(-5,5,1000)

epsilon=0.01
def frame(x,i):
    f=(1/2)*(((x-np.cos(theta))/np.sin(theta))**2+epsilon*np.cos(theta))
    fig, ax = plt.subplots()
    plt.xlim(-5,5)
    plt.ylim(-2,10)
    ax.grid()
    plt.title('Ueff(\u03B8)')
    plt.xlabel('\u03B8') 
    plt.ylabel('Ueff(\u03B8)') 
    plt.plot(theta,f,'g')
    a="poza"
    b=i
    name=f'{a}{b}'
    plt.savefig(name,dpi=600)
    
j=0
u0=np.linspace(-2,2,100)

for i in u0:
    frame(i,j)
    j+=1

    



    



