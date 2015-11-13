import numpy as num
import numpy.linalg as LA
import time as time

L = 400
H = 200
delta = 0.01

start_time = time.time()


def Jacobian(X,Y):
    J = num.empty([2,2],float)
    FTLE = num.empty([H-2,L-2],float)
    
    for i in range(0,H-2):
        for j in range(0,L-2):
            J[0][0] = (X[(1+i)*L+2+j]-X[(1+i)*L+j])/(2*delta)
            J[0][1] = (X[(2+i)*L+1+j]-X[i*L+1+j])/(2*delta)
            J[1][0] = (Y[(1+i)*L+2+j]-Y[(1+i)*L+j])/(2*delta)
            J[1][1] = (Y[(2+i)*L+1+j]-Y[i*L+1+j])/(2*delta)
            D = num.dot(num.transpose(J),J)
            lamda = LA.eigvals(D)
            FTLE[i][j] = max(lamda)
    return FTLE

for i in range(10,20):
    Input = open('mapping%d.txt'%i,'r')
    X,Y = num.loadtxt(Input,unpack=True)
    Input.close()
    FTLE = Jacobian(X,Y)
    FTLE = num.log(FTLE)
    num.savetxt('FTLE%d.txt'%i,FTLE)

print(time.time()-start_time)

