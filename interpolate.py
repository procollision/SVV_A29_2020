import numpy as np
import support_function as sup
from aircraft_data import *

def interpolate():
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
    
    
    
    """
    print("x values  ",x[0],x[1])
    print("z values",z[0],z[1],z[2])
    print("data values",data[1,0],data[1,1],data[2,0],data[2,1])

    ####### Was used to check values ########

    print("SECOND   ",x[2],z[2])
    print("These are the x values and data values for second k row")
    print("Second     ",data[0,1],data[0,2],data[1,1],data[1,2])
    """


    """
    Bivariate Interpolation
    """
    K = np.ndarray((80,40,4)) #creates starting array so appending goes easier, should be (1,40)

    for c in range(80): # these are the rows, z direction, 80, if you want to check for the first set of constants change to 1
        Kk = np.ones((4,1))  #creates new array to start new row,
        for j in range(40):     #should be 40    #if you want to check for first set of constants change range to 1
            
            M = np.ones((4,1))
            i = j 
            while i == j:
                X = np.transpose(np.array([[x[i],x[i],x[i+1],x[i+1]]]))
                Z = np.transpose(np.array([[z[c],z[c+1],z[c],z[c+1]]]))
                XZ = X*Z
                D = np.transpose(np.array([[data[c,i],data[c,i+1],data[c+1,i],data[c+1,i+1]]])) #change this, to go from left to right
                i += 1
            
            """
            print("X matrix of x values",X)  ### This was used to check values
            print("Matrix of z values",Z)
            
            print("Matrix of xz values",XZ)
            print("matrix of data values",D)
            """
            
            M = np.append(M,X,axis =1)   
            M = np.append(M,Z,axis = 1)
            M= np.append(M,XZ,axis=1)
            
            
            
            k = np.linalg.solve(M,D)
            #print(k) #was used to test 
            """
            print("full matrix",M)
            """
            
            for l in range(4):
                K[c][j][l] = k[l]    #creates the constants for 40 sets of points, thus creates a row
    return K,z,x
   
#print(interpolate()[1][1])
