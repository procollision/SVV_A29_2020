import numpy as np 
from integrate import *
r = 1
cl = 4
stringer_ds
stringer_cord_array
stringer_area
Vy,Vz,Ixx,Iyy,ts,tb, dt
stringer_spacing
#definition of geometr functions in terms of y(s) and z(s)
y1 = []
y1_bounds = []
y1_bounds.append([0,np.pi/2])
y1.append(lambda theta: r*r*np.sin(theta))
y1_bounds.append([0,2*r])
y1.append(lambda s: -r*s+r)
y1_bounds.append([-np.pi/2,0])
y1.append(lambda theta: r*r*np.sin(theta))
#thickness from the three sections
t1_list = [ts,tb,ts]
#step list
dt_list = [dt,dt,dt]
#if stringers are apllied or not
stringer = [1,0,1]
y2 = []
y2_bounds = []
y2_bounds.append([0,r])
y2.append(lambda s: s)
y2_bounds.append([0,2*np.sqrt(r*r+(cl-r)*(cl-r))])
y2.append(lambda s: -r/(np.sqrt(r*r+(cl-r)*(cl-r)))*s+r)
y2_bounds.append([0,r])
y2.append(lambda s: s-r)
t2 = [tb,ts,tb]

final_qlist = []

for y_element in y_s:
    intermidate_qlist = np.array([])
    B_final = 1
    for i inrange(len(y_elemet[0]))
        #obtain geometry information
        bounds = y_s[0,i,1]
        ds = ds_list[i]
        t = t_list[i]
        func = y_s[0,i,0]
        s_list = np.arange(bounds[0],bounds[1]+ds,ds)
        s_list_copy = np.copy(s_list)
        B_list = np.ndarray(len(s_list))
        B_list[0] = 0
        #evaluate integral int y ds
        q_list = Vy/Izz*t*integrate(func,ds,bounds)
        Shift_value = False
        #generate the number of B's included in the domain
        for i in range(len(s_list)):
            if stringer[i] = 1:
                B_list[i] = int((s_list_copy[i]+offset)/stringer_spacing)+B_final
            else:
                B_list[i]=B_list[i-1]
        #add the terms for the stringers
        for i in range(s_list):
            q_list[i] += Vy/Izz*stringer_area*np.sum[stringer_cord_array[0][:B_list[i]]]

        intermidate_qlist.append[q_list]
        B_final = B_list[-1]
        intermidate_qlist = np.append(intermidate_qlist,q_list)
    final_qlist.append(intermidate_qlist)
