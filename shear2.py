import numpy as np 
import matplotlib.pyplot as plt
import support_function as sup
from sim_geom import *
from CGFunction import *
from aircraft_data import *

#dt should be a multiple of 0.075
tb = 0.01


def get_q_shear(dt):
    r = h_a/2
    #compute stringer spacing over the skin
    stringer_spacing = (r*np.pi+2*np.sqrt((C_a-r)*(C_a-r)+r*r))/N_st
    #print("stringer_spacing value %s" % stringer_spacing)
    #stringer_spacing = r/2
    #import coordiantes of stringer
    stringer_cord_array,CG = centroid()
    #stringer_cord_array = [[r/2,0],[0,0],[-r/2,0]]
    #compute stringer area
    stringer_area = (w_st+h_st)*w_st
    

    final_qlist = [[[[],[],[]],[[],[],[],[]]],[[[],[],[]],[[],[],[],[]]]]
    #import geometry
    geometry = get_geom(r,C_a,t_sk,t_sp,dt,stringer_spacing,CG[1])
    #geometry = get_geom(h,lw,tb,dt)
    #di = dimension index
    for di in range(np.shape(geometry)[0]):
        #ci = cell index
        for ci in range(np.shape(geometry)[1]):
            #for carrying over number of stringers over elements
            B_final = np.array([])
            #element index
            for ei in range(np.shape(geometry[di][ci][0])[0]):
                #obtain geometry information
                func = geometry[di][ci][0][ei]
                bounds = geometry[di][ci][1][ei]
                stringer = geometry[di][ci][2][ei]
                t = geometry[di][ci][3][ei]
                ds = geometry[di][ci][4][ei]
                offset = geometry[di][ci][5][ei]
                B_list = geometry[di][ci][6][ei]
                
                
                s_list = np.arange(bounds[0],bounds[1]+ds,ds)
                B_index = [[]]*len(s_list)
        
                
                #evaluate integral int y ds
                
                if ei!= 0:
                    #q_list = sup.integrate(func,ds,bounds)*t + final_qlist[di][ci][ei-1][-1] #for the correct shear flow 
                    q_list = sup.integrate(func,ds,bounds)*t + q_list[-1] #for the correct shear flow 
                    #print("final_qlist %s" % final_qlist[di][ci][ei-1][-1])
                elif ci == 1 and ei ==0:
                    q_list = sup.integrate(func,ds,bounds)*t + final_qlist[0][0][1][round(len(final_qlist[0][0][1])/2)]
                else:
                    q_list = sup.integrate(func,ds,bounds)*t
                
                #generate the number of B's included in the domain
                
                for i in range(len(s_list)):
                    if stringer == 1:
                        #print(int((s_list[i]+offset)/(stringer_spacing*ds/dt)))
                        #print(ds/dt)
                        B_index[i] = np.append(B_final,B_list[:int((s_list[i]+offset)/(stringer_spacing*ds/dt))])
                    else:
                        B_index[i]= B_final
                
                #add the terms for the stringers
                sq_list = q_list.copy()
                for i in range(len(sq_list)):
                    tempsum = 0
                    for k in B_index[i]:
                        #print(CG)                     
                        tempsum += stringer_cord_array[int(k)][di]#+CG[di]
                    sq_list[i] = stringer_area*tempsum
                
                B_final = B_index[-1]
                

                final_qlist[di][ci][ei]=q_list+sq_list
                str_label = "dim"+str(di)+" ci"+str(ci)+" ei"+str(ei)
                if False:
                    plt.plot(np.arange(bounds[0],bounds[1],ds),final_qlist[di][ci][ei],label=str_label)
    #plt.legend()
    #plt.show()
    return final_qlist

final_qlist = get_q_shear(0.001)
