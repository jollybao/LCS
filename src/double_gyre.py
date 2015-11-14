# Jialun Bao
# Jerry Qiu
# 11/13/15

import pylab as plt
import numpy as num
import matplotlib.animation as animation


fig, ax = plt.subplots(1,1,figsize=(10,5))
#plt.rcParams['animation.ffmpeg_path'] = 'C:/ffmpeg/bin/ffmpeg'
#mywriter = animation.FFMpegWriter()

# constants
p = num.pi
A = 0.1
epsilon = 0.25
w = p/5
delta = 0.0001
dt = 0.1
partition = 20
N = int(input("Enter number of particles: "))
col = ['r','y','b','g','k','c','m','r','y','b',
       'g','k','c','m','r','y','b','g','k','c','m',
       'r','y','b','g','k','c','m']

# wave function that defines the characteristics of 
# double gyre
def phi(x,y,t):
    temp = A*num.sin(p*f(x,t))*num.sin(p*y)
    return temp

def f(x,t):
    temp = epsilon*num.sin(w*t)*x**2+(1-2*epsilon*num.sin(w*t))*x
    return temp

def velocity(x,y,t):
    vx = (phi(x,y+delta,t)-phi(x,y-delta,t))/(2*delta)
    vy = (phi(x-delta,y,t)-phi(x+delta,y,t))/(2*delta)
    return -1*vx,-1*vy
	
# function that computes velocity of particle at each point
def update(r,t):
    x = r[0]
    y = r[1]
    vx = (phi(x,y+delta,t)-phi(x,y-delta,t))/(2*delta)
    vy = (phi(x-delta,y,t)-phi(x+delta,y,t))/(2*delta)
    return num.array([-1*vx,-1*vy],float)

# make a 2D mesh grid of size 40*20
X,Y = plt.meshgrid(num.arange(0,2,1/partition),num.arange(0,1,1/partition))
Vx,Vy = velocity(X,Y,0.1)

# vector arrows
Q = ax.quiver(X,Y,Vx,Vy,scale=10)

# initialize array of particles
C = num.empty([N],plt.Circle)
for i in range(0,N):
    C[i] = plt.Circle((-1,-1),radius = 0.03, fc = col[i])
    
R = num.empty([N,2],float)
for i in range(0,N):
    print("Enter x and y coordinates of the circle ",i+1)
    R[i][0] = float(input())
    R[i][1] = float(input())
    C[i].center = (R[i][0],R[i][1])
    ax.add_patch(C[i])
    

# animation for particle moving along the vector field
def animate(num,Q,X,Y,C,R,N):
    t = num/1
    dt = 1/10
    Vx,Vy = velocity(X,Y,t)
    Q.set_UVC(Vx,Vy)  
    
	# update particles' positions
    for i in range(0,N):
        for j in range(0,10):
            r = R[i][:]
            k1 = dt*update(r,t)
            k2 = dt*update(r+0.5*k1,t+0.5*dt)
            k3 = dt*update(r+0.5*k2,t+0.5*dt)
            k4 = dt*update(r+k3,t+dt)
            R[i][:] += (k1+2*k2+2*k3+k4)/6
    
        C[i].center = (R[i][0],R[i][1])
    return Q,C

ani = animation.FuncAnimation(fig, animate,
         fargs=(Q,X,Y,C,R,N),
    interval=100,blit=False)

#ani.save('VF_demo.mp4',writer = mywriter)

plt.show()

