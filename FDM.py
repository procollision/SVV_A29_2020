# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:00:04 2020

@author: rdenb
"""
import numpy as np
from scipy.sparse import csr_matrix, linalg
import matplotlib.pyplot as plt
import support_function as sup
from aircraft_data import *
from interpolate import *

def bending_solve(N,I,dtz):
    h = l_a/N
    EXT = 3
    COM = 1
    # Create (empty) sparse matrix of the required size

    V = np.zeros((N*2+EXT*2+COM,1))
    M = csr_matrix((N*2+EXT*2+COM,N*2+EXT*2+COM))
    #Finite diffrence schemes defenition
    fx4 = [[-2,-1,0,1,2],[1,-4,6,-4,1]]
    fx3 = [[0,1,2,3,4],[-5,18,-24,14,-3]]
    fx2 = [[0,1,2,3],[2,-5,4,-1]]
    fx2c = [[-1,0,1],[1,-2,1]]
    fx1c = [[-1,1],[-1,1]]
    fx1s = [[0,1,2],[-3,4,-1]]
    #other defenitions
    shift =[0,N+EXT]
    
    turn = [np.cos(theta),np.sin(theta)]
    rturn = [np.sin(theta),np.cos(theta)]

    K,zl,xl = interpolate()
    other = [xl,zl,K]
    #--- Aerodynimc data
    for i in range(0,N):
        V[i] = sup.get_w([h*i],dtz,other)/(E*I[0])
        #V[i] = 0
    

    for dim in range(len(shift)):
        sh = shift[dim]
        # Fill matrix with fintite diffrence scheme for x''''
        for i in range(2,N-2):
            for k in range(len(fx4[0])):
                M[sh+i,sh+i+fx4[0][k]] = fx4[1][k]/(h**4)
        
        #---- Boundary conditions ----
        #-- Shear BC
        
        for k in range(len(fx3[0])):
            M[sh+1,sh+fx3[0][k]] = fx3[1][k]/(2*h**3)
        
        for k in range(len(fx3[0])):
            M[sh+N-2,sh+N-1-fx3[0][k]] = fx3[1][k]/(h**3)
        
        #-- Moment BC
        for k in range(len(fx2[0])):
            M[sh+0,sh+fx2[0][k]] = fx2[1][k]/(h**2)
        
        for k in range(len(fx2[0])):
            M[sh+N-1,sh+N-1-fx2[0][k]] = fx2[1][k]/(h**2)


        #-- Vector standrd BCs
        for i in [0,1,N-1,N-2]:
            V[sh+i,0] = 0
        
        #--- Vector Displacements
        N_sp = [[round(x_1/h),round(x_2/h),round(x_3/h)],[d_1*turn[dim],d_2*turn[dim],d_3*turn[dim]]]
        for i in range(len(N_sp[0])):
            V[sh+N+i,0] = N_sp[1][i]
            M[sh+N_sp[0][i],sh+N+i] = -1/(E*I[dim]*h)
            M[sh+N+i,sh+N_sp[0][i]] = 1

        #--- additional coupling for the actuators
        N_a1 = round((x_2-(x_a/2))/h)
        N_a2 = round((x_2+(x_a/2))/h)
        M[sh+N_a1,-1] = -1/(E*I[dim]*h)*rturn[dim]
        M[-1,sh+N_a1] = rturn[dim]
        V[-1,0] = 0
        V[sh+N_a2,0] -= rturn[dim]*P/(E*I[dim]*h)

        
    
    X = linalg.spsolve(M,V)
    

    d = [X[:-N-2*EXT-COM],X[N+EXT:-EXT-COM]]
    Z = d[0]
    Vr = [X[N:N+EXT],X[2*N+EXT:2*N+2*EXT]]
    Va = X[-1]
    #-- Compute moments by taking the second derivative of deflection
    Mi = np.zeros([2,np.shape(Z)[0]])
    for j in range(2):
        for i in range(1,len(Z)-1):
            for k in range(len(fx2c[0])):
                Mi[j][i] += fx2c[1][k]*d[j][i+fx2c[0][k]]/(h**2)*E*I[j]
        
        for k in range(len(fx2[0])):
                Mi[j][0] += fx2[1][k]*d[j][0+fx2[0][k]]/(h**2)*E*I[j]
            
        for k in range(len(fx2[0])):
                Mi[j][-1] += fx2[1][k]*d[j][-1-fx2[0][k]]/(h**2)*E*I[j]

    #-- Compute Shear by taking first derivative of Moment 
    Vi = np.zeros([2,np.shape(Z)[0]])
    for j in range(2):
        for i in range(1,len(Z)-1):
            for k in range(len(fx1c[0])):
                Vi[j][i] += fx1c[1][k]*Mi[j][i+fx1c[0][k]]/(2*h)

        for k in range(len(fx1s[0])):
                Vi[j][0] += fx1s[1][k]*Mi[j][0+fx1s[0][k]]/(2*h)
            
        for k in range(len(fx1s[0])):
                Vi[j][-1] += fx1s[1][k]*Mi[j][-1-fx1s[0][k]]/(2*h)

    plt.plot(np.arange(0,l_a,h),Mi[0])
    plt.plot(np.arange(0,l_a,h),Mi[1])
    plt.show()
    plt.plot(np.arange(0,l_a,h),Vi[0])
    plt.plot(np.arange(0,l_a,h),Vi[1])
    plt.show()
    return Mi,Vi,Vr,Va






