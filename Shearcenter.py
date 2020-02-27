import numpy as np
from CGFunction import *
from aircraft_data import *
from shear2 import *
from arm2 import *
from Ifunction import *
dt = 0.01

def get_sc(dt):
    
    final_qlist = get_q_shear(dt)
    #print("final_qlist %s" % final_qlist)
    r = h_a/2
    stringer_spacing = (r*np.pi+2*np.sqrt((C_a-r)*(C_a-r)+r*r))/N_st
    
    #the geometry beeing analysed 
    #geometry = get_geom(r,C_a,t_sk,t_sp,dt,stringer_spacing)
    st_cord, cg = centroid()
    #creat the final list
    moment_list = []
    #get the arm
    arm = get_arm(r,C_a,t_sk,t_sp,dt,stringer_spacing)
    
    #ic = index cell
    for ic in range(len(final_qlist[0])):
        intermidate_mlist = []
        webs = []
        # iw = web index
        for iw in range(len(final_qlist[0][ic])):
            #obtain geometry information
            func = arm[0][ic][0][iw]
            bounds = arm[0][ic][1][iw]
            ds = arm[0][ic][2][iw]
            # The start position of the web
            dS = 0
            web = np.array([])
            # ni are the elements with stepsize ds
            for ni in range(len(final_qlist[0][ic][iw])):
                #taking the sum of the area of the shearflow * arm
                dS = dS + ds
                moment = final_qlist[0][ic][iw][ni] * func(dS) * ds
                web = np.append(web,moment)
            
            #verification check for the cross section
            if ic != 1:
                webs = np.append(webs,web)
                error = (np.sum(web)/I_zz(st_cord, cg)- (4*r)/np.pi)/np.sum(webs)/I_zz(st_cord, cg)
                print("error of the curve %s" % error)
            else:
                webs = np.append(webs,web)
                error = (np.sum(web)/I_zz(st_cord, cg)- (r - C_a))/np.sum(webs)/I_zz(st_cord, cg)
                print("error of the tail %s" % error)
            intermidate_mlist = np.append(intermidate_mlist,web)
    
        moment_list = np.append(moment_list,intermidate_mlist)
    #summing up all the elements and deviding by I_zz to get the shear center   
    eta =  np.sum(moment_list)/I_zz(st_cord, cg)
    return eta

eta =get_sc(0.01*np.pi)

st_cord, cg = centroid()
#verivication of the shear center. If the verification geometry is used the
#analytical eta needs to be compaired with eta. Else the eta2 indicates the shearcenter 
#as been taken from the aileron crossection of an boeing 737
eta_arm = .1125 - 0.119227065644352412

print("eta %s" % eta)
print("eta2 %s" % eta_arm)
eta2 = C_a*C_a*r*r*t_sp/I_zz(st_cord, cg)
print("analytical eta %s" % eta2)
print("error with analythical solution %s" % ((eta - eta2)/eta))
print("error with verification model %s" % ((eta - eta_arm)/eta))






