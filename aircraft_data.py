import numpy as np
C_a = 0.547
l_a = 2.771
x_1 = 0.153
x_2 = 1.281
x_3 = 2.681
x_a = 28
h_a = 22.5
t_sk = 1.1 
t_sp = 2.9
t_st = 1.2
h_st = 1.5
w_st = 2.0
N_st = 17
d_1 = 1.103
d_2 = 0
d_3 = 1.642
theta = 26
P = 91.7
E=72
data_name="aerodynamicloada320.dat"

x_a = x_a/100
h_a = h_a/100
r = h_a/2
t_sk = t_sk/1000
t_sp = t_sp/1000
t_st = t_st/1000
h_st = h_st/100
w_st = w_st/100
d_1 = d_1/100
d_2 = d_2/100
d_3 = d_3/100
theta = theta*np.pi/180
P = P*1000
E=E*10**6



