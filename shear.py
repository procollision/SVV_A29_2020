import numpy as np 
from integrate import *
from geom import *
from CGfubction import *
from aircraft_data import *

V = [1,1]
# Izz, Iyy
I = [1,1]
dt = 0.1
r = h_a/2
#compute stringer spacing over the skin
stringer_spacing = (r*np.pi+2*np.sqrt((C_a-r)*(C_a-r)+r*r))/N_st
#import coordiantes of stringer
stringer_cord_array = centroid_y(h_a, C_a, t_sk, h_st, w_st, t_st, N_st, t_sp)
#compute stringer area
stringer_area = (w_st+h_st)*w_st


final_qlist = []
#import geometry
geometry = get_geom(r,C_a,t_sk,t_sp,dt,stringer_spacing)
#di = dimension index
for di in range(np.shape(geometry)[0]):
    #ci = cell index
    for ci in range(np.shape(geometry)[1]):
        intermidate_qlist = np.array([])
        #for carrying over number of stringers over elements
        B_final = 0
        #element index
        for ei in range(np.shape(geometry[di][ci][0])[0]):
            #obtain geometry information
            func = geometry[di][ci][0][ei]
            bounds = geometry[di][ci][1][ei]
            stringer = geometry[di][ci][2][ei]
            t = geometry[di][ci][3][ei]
            ds = geometry[di][ci][4][ei]
            offset = geometry[di][ci][5][ei]
            
            
            s_list = np.arange(bounds[0],bounds[1]+ds,ds)
            B_list = np.ndarray(len(s_list))
            B_list[0] = 0
            #evaluate integral int y ds
            q_list = I[di]*t*integrate(func,ds,bounds)
            #generate the number of B's included in the domain
            for i in range(len(s_list)):
                if stringer == 1:
                    B_list[i] = int((s_list[i]+offset)/stringer_spacing)+B_final
                else:
                    B_list[i]=B_list[i-1]
            #add the terms for the stringers
            for i in range(len(s_list)):
                q_list[i] += I[di]*stringer_area*np.sum(stringer_cord_array[0][:B_list[i]])

            intermidate_qlist.append[q_list]
            B_final = B_list[-1]
            intermidate_qlist = np.append(intermidate_qlist,q_list)
        final_qlist.append(intermidate_qlist)



