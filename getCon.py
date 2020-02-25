import numpy as np
import support_function as sup
from aircraft_data import *
from interpolate import *
"""
This is used to test and get the x values
"""

d = open("aerodynamicloada320.dat","r")
lines = d.readlines()
d.close()

"""
Reading data into list
"""

data = []

for line in range(len(lines)):
    da = lines[line]
    das = da.split(",")
    row = []
    for n in das:
        row.append(float(n))
    data.append(row)
        
#81 rows, chorwise directions and 41 spanwise stations
#len(data) = 81 ,,, len(data[i]) equals 41


"""
Calculating the coordinates
"""

Nz = len(data)
Nx = len(data[0])



thz,z,thx,x = sup.get_interp_cord(Nz,Nx,C_a,l_a)

data = np.array(data)


z = np.array(z) #returns 81 values
x = np.array(x) #returns 41 values

X = x[1] +0.001             # x value to test def below
Z = z[1] - 0.0001           # z value to test def below

#print(X)
#print(Z)

"""
This is the definition to get the constatants for certain set
Everything before was just to get x and z values to test
"""

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
    
    return interpolate()[IndexZ][index]          #[z][x]
    
print(getCon(X,Z))