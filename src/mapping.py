# Jialun Bao
# 11/13/15

import numpy as num
import numpy.linalg as LA
import time as time

# constants
p = num.pi
A = 0.1
epsilon = 0.25
w = p/5
Delta = 0.0001
delta = 0.01
dt = 0.1
T = 20
L = 400
H = 200


start_time = time.time()

# wave function that defines the characteristics of 
# double gyre
def phi(x,y,t):
    temp = A*num.sin(p*f(x,t))*num.sin(p*y)
    return temp

def f(x,t):
    temp = epsilon*num.sin(w*t)*x**2+(1-2*epsilon*num.sin(w*t))*x
    return temp

# function that computes velocity of particle at each point
def update(r,t):
    x = r[:,0]
    y = r[:,1]
    vx = (phi(x,y+Delta,t)-phi(x,y-Delta,t))/(2*Delta)
    vy = (phi(x-Delta,y,t)-phi(x+Delta,y,t))/(2*Delta)
    return num.column_stack((-1*vx,-1*vy))
            
     
        
  
shift = 1.1*delta
# y-coordinate of the grid
h = num.linspace(shift,1,H)
# evolution time 0-10s
tau = num.linspace(0,9.9,100)

# getting 100 mapping data files
for n in range(0,100):
    output = open('mapping%d.txt'%n,'ab')
    for i in h:
	
		# initialize grid horizontally
        x = num.linspace(shift,2,L)
        y = num.linspace(i,i,L)
        r = num.column_stack((x,y))
		
		# perform RK4 to get position of particle 20s later
        for t in num.arange(0+tau[n],T+tau[n],dt):
             k1 = dt*update(r,t)
             k2 = dt*update(r+0.5*k1,t+0.5*dt)
             k3 = dt*update(r+0.5*k2,t+0.5*dt)
             k4 = dt*update(r+k3,t+dt)
             r += (k1+2*k2+2*k3+k4)/6
		
		# append data to the file	
        num.savetxt(output,r)       
    output.close()
    
print(time.time()-start_time)
