import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
theta=np.linspace(-5,5,1000)

epsilon=0.01
def frame(x,i): #x is the free parameter I need to plot the function for. 
    f=(1/2)*(((x-np.cos(theta))/np.sin(theta))**2+epsilon*np.cos(theta))  #parametric equation to be plotted, here I used the equation of the effective potential of a gyroscope. 
    fig, ax = plt.subplots()
    plt.xlim(-5,5) #setting graph limits that suit my needed domain
    plt.ylim(-2,10)
    ax.grid()
    plt.title('Ueff(\u03B8)')
    plt.xlabel('\u03B8') 
    plt.ylabel('Ueff(\u03B8)') 
    plt.plot(theta,f,'g') #here I plot the equation f(theta) for the arbitrary value of x
    a="poza"
    b=i
    name=f'{a}{b}' #change the name of the file iteratively in order to have consecutive frames
    plt.savefig(name,dpi=600)
    
j=0
u0=np.linspace(-2,2,100) #array of values for the free parameter x

for i in u0:
    frame(i,j) #calling the function for all values in u0, j is the increment for the file number
    j+=1

    



    



