import numpy as np
#from integrate import *
from aircraft_data import h_a,C_a
from interpolate import *

def integrate(func,dt,bounds):
    x_list = np.arange(bounds[0],bounds[1]+dt,dt)
    ix_list = np.ndarray(len(x_list)-1)
    for i in range(len(x_list)-1):
        ix_list[i]=(func(x_list[i])+func(x_list[i+1]))/2*dt
    for i in range(1,len(ix_list)):
        ix_list[i] += ix_list[i-1]
    return ix_list

def get_interp_cord(Nz,Nx,Ca,la):
    thz = []        #theta Z
    for t in range(1,Nz+2):
        th = (t -1)/Nz * np.pi
        thz.append(th)


    z = [] #z-coordinate
    for i in range(1,Nz+1):
        zi = -0.5 * (Ca/2*(1-np.cos(thz[i-1])) + Ca/2*(1-np.cos(thz[i])))
        z.append(zi)


    thx = []  #theta x
    for t in range(1,Nx+2):
        th = (t -1)/Nx * np.pi
        thx.append(th)


    x = []  #x-coordinate
    for i in range(1,Nx+1):
        xi = 0.5 * (la/2*(1-np.cos(thx[i-1])) + la/2*(1-np.cos(thx[i])))
        x.append(xi)
    
    return thz,z,thx,x

def interp_funct(x,z):
    k = get(x,y)
    return k[0]+k[1]*x+k[2]*z+k[3]*z*x

def slice_func_y(func,val):
    return lambda x: func(x,val)

def slice_func_x(func,val):
    return lambda y: func(val,y)

def get_w(cord,dt):
    w = np.ndarray(len(cord))
    for i in range(len(cord)):
        w[i]=integrate(slice_func_y(interp_funct,cord[i]),dt,[-h_a/2,C_a-h_a/2])[-1]
    return w


# Function to calculate aileron section length
def Aileron_Sectionwidth(l_a,N):
    # Aileron length divided by the number of section to be analyzed (N)
    h = float(l_a / N)
    return h

# Determine the x-coordinates of every discrete location N where the aileron will be analyzed
def Section_x_locations(l_a,N):
    h = Aileron_Sectionwidth(l_a,N)
    x_vector = np.zeros((N+1,1))
    for i in range(0,N+1):
        x_vector[i,0] = i*h
    return x_vector

# Function to find at which N the hinges and actuators are located
def Find_attach_N(N,l_a,x1,x2,x3,x_a):
    h = Aileron_Sectionwidth(l_a,N)
    # Divide x-coordinates by the section length, round down to evaluate at the [n+1] postion
    N_x1 = int(x1//h)
    N_ac_1 = int((x2-(x_a/2))//h)
    N_x2 = int(x2//h)
    N_ac_2 = int((x2+(x_a/2))//h)
    N_x3 = int(x3//h)
    return N_x1,N_ac_1,N_x2,N_ac_2,N_x3

def getCon(X,Z):
    
    i = 0
    
    while X >= x[i]:
        i += 1
    index = i-1
    
    #print(index)
    I = 0
    
    while Z <= z[I]:
        I += 1
    
    IndexZ = I-1
    #print(IndexZ)
    
    return interpolate()[IndexZ][index]  
