import numpy as np
import support_function as sup
from aircraft_data import * 


def get_q_mat():
    A_1 = 0.5*np.pi*r*r
    A_2 = r*(C_a-r)
    St_1 = np.pi*r/t_sk + h_a/t_sp
    St_2 = 2*np.sqrt(r*r+(C_a-r)*(C_a-r))/t_sk+h_a*t_sp
    St_12 = h_a/t_sp
    A = np.array([[2*A_1,2*A_2],[St_1/A_1+St_12/A_2,-(St_2/A_2+St_12/A_1)]]) 
    return np.inv(A)

def get_q(V,N,dtx,dtz,dts):
    A = get_q_mat()
    h = sup.Aileron_Sectionwidth(l_a,N)
    Nt = int(C_a/dtz)
    N_x1,N_ac_1,N_x2,N_ac_2,N_x3 = sup.Find_attach_N(N,l_a,x_1,x_2,x_3,x_a)
    T = np.array([0]*N)
    SC = r
    q0 = np.ndarray(N,2)
    for i in range(N):
        '''if N == N_x1:
            w[i] = -Vy_ext_1*SC
        if N == N_ac_1:
            w[i] = cos(theta)*R_ac_1*r - np.sin(theta)*R_ac_1*SC
        if N == N_x2:
            w[i] = -Vy_ext_2*SC
        if N == N_ac_2:
            w[i] = cos(theta)*P*r-sin(theta)*P*SC
        if N == N_x3:
            T[i] = Vy_ext_3*SC'''
        x_cord = i*h
        for k in range(Nt):
            T[i]+=sup.integrate(sup.slice_func_x(sup.interp_funct,Nt),dtx,[i*h,(i+1)*h])[-1]*dtz*(-k*dtz+SC)
        q0[i] = A*np.array([T,0]))
    q = get_q_shear()
return q0



