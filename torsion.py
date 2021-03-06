import numpy as np
import support_function as sup
import shear2 as SHEAR
from aircraft_data import *
from interpolate import *
import Shearcenter as SC_center

def get_q_mat():
    A_1 = 0.5*np.pi*r*r
    A_2 = r*(C_a-r)
    St_1 = np.pi*r/t_sk + h_a/t_sp
    St_2 = 2*np.sqrt(r*r+(C_a-r)*(C_a-r))/t_sk+h_a*t_sp
    St_12 = h_a/t_sp
    A = np.array([[2*A_1,2*A_2],[St_1/A_1+St_12/A_2,-(St_2/A_2+St_12/A_1)]]) 
    return np.linalg.inv(A)

def q_reshape(q):
    return [q[0][1],q[1][1],q[1][2],q[0][2],q[0][1]]


def get_q(V,N,I,dtx,dtz,dts,Vr,Va):
    A = get_q_mat()
    h = sup.Aileron_Sectionwidth(l_a,N)
    Nt = int(C_a/dtz)
    N_x1,N_ac_1,N_x2,N_ac_2,N_x3 = sup.Find_attach_N(N,l_a,x_1,x_2,x_3,x_a)
    T = np.array([0.0]*N)
    q = SHEAR.get_q_shear(dts)
    K, zl, xl = interpolate()
    other = [xl,zl,K]
    new_q = np.empty([N,2,4]).tolist()
    out_q = [[]]*N
    SC = SC_center.get_sc(dts)
    q0 = np.zeros([N,2])
    for i in range(1,N):
        if i== N_x1:
            T[i] = -Vr[0][0]*(r+SC)
        if i == N_ac_1:
            T[i] = -np.cos(theta)*Va*r + np.sin(theta)*Va*SC
        if i == N_x2:
            T[i] = -Vr[0][1]*(r+SC)
        if i == N_ac_2:
            T[i] = np.cos(theta)*-P*r+np.sin(theta)*-P*SC
        if i == N_x3:
            T[i] = -Vr[0][2]*(r+SC)
        for k in range(Nt):
            T[i]+=sup.integrate(sup.slice_func_x(sup.interp_funct,dtz*k,other),dtx,[i*h,(i+1)*h])[-1]*dtz*(k*dtz-SC)
        T[i] += T[i-1]
        q0[i] = np.dot(A,np.array([T[i],0]))

        #----- COMBINE SHEAR FROM TORSION AND INTERNAL SHEAR -----
        for ci in range(2):
            for ei in range(len(q[0][ci])):
                if ci == 0:
                    if ei == 0:
                        qz = q[1][1][0]*V[1][i]/I[1]
                    elif ei == 1:
                        qz = np.append(np.flip(q[1][0][0])[:-1],q[1][0][0])*V[1][i]/I[1]
                    else:
                        qz = -np.flip(q[1][1][0]*V[1][i]/I[1])
                else:
                    if ei == 0:
                        qz = q[1][0][0]*V[1][i]/I[1]
                    elif ei == 1:
                        qz = q[1][1][1]*V[1][i]/I[1]
                    elif ei == 2:
                        qz = -np.flip(q[1][1][1]*V[1][i]/I[1])
                    else:
                        qz = -np.flip(q[1][0][0]*V[1][i]/I[1])
                #print(np.shape(qz),np.shape(q[0][ci][ei]),ci,ei)
                condition = (ci==0 and ei==1) or (ci==1 and (ei==0 or ei==3))
                if condition:
                    new_q[i][ci][ei] = q[0][ci][ei]*V[0][i]/I[0] + qz + q0[i][ci]-q0[i][-ci-1]
                else:
                    new_q[i][ci][ei] = q[0][ci][ei]*V[0][i]/I[0] + qz + q0[i][ci]
        out_q[i] = q_reshape(new_q[i])
    #print(q[-1])
    """
    plt.plot(np.linspace(0,l_a,N),T)
    plt.xlabel("x coordinate [m]")
    plt.ylabel("Torsion under even distributed load [Nm]")
    plt.show()"""
    return new_q

"""
N = 1000
V = np.ones([2,N])
test = get_q(V,N,[1,1],0.01,0.01,0.001,[[0.,0.,0.],[0.,0.,0.]],0.)"""