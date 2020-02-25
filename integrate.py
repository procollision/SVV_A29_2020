import numpy as np

def integrate(func,dt,bounds):
    x_list = np.arange(bounds[0],bounds[1]+dt,dt)
    ix_list = np.ndarray(len(x_list)-1)
    for i in range(len(x_list)-1):
        ix_list[i]=(func(x_list[i])+func(x_list[i+1]))/2*dt
    for i in range(1,len(ix_list)):
        ix_list[i] += ix_list[i-1]
    return ix_list


