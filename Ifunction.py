# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:37:51 2020

@author: Luuk van der Mark
"""
import numpy as np

def I_zz(h_a, C_a, t_sk, h_st, w_st, t_st, N_st, t_sp, st_cord, cg):
    
    h_a = h_a/100
    t_sk = t_sk/1000
    h_st = h_st/100
    w_st = w_st/100
    t_st = t_st/1000
    t_sp = t_sp/1000
    
    # Create a list to store all elements which need to be summed.
    I_zz = []
    # Defines the list for the z coordinates of the stringers and the z location of the cg.
    y_cord = [cord[1] for cord in st_cord]
    cg_y = cg[1]
    
    # Calculate the MOI zz of the semicircle element.
    I_sc = 1/8*np.pi*((0.5*h_a)**4-(0.5*h_a-t_sk)**4)
    I_zz.append(I_sc)
    
    # Calculate the MOI zz of the skin elements.
    phi = np.arctan((0.5*h_a)/(C_a - 0.5*h_a))
    L_sk = ((0.5*h_a)**2+(C_a-0.5*h_a)**2)**0.5
    I_sk = 1/12*t_sk*(L_sk**3)*(np.sin(phi))**2
    I_zz += 2*[I_sk]
    
    # Calculate the Steiner term of the skin elements. 
    A_sk = L_sk*t_sk
    cg_ysk = 0.5*L_sk*np.sin(phi)
    S_sk = A_sk*(abs(cg_y-cg_ysk))**2
    I_zz += 2*[S_sk]
    
    # Calculate the MOI zz of the spar element.
    I_sp = 1/12*t_sp*(h_a)**3
    I_zz.append(I_sp)
    
    # Calculate the Steiner term of the stringers.
    A_st = (h_st*t_st)+(w_st*t_st)
    
    for i in range(N_st):
        dy_st = abs(cg_y - y_cord[i])
        S_st = A_st * dy_st**2
        I_zz.append(S_st)
         
    I_zz = sum(I_zz)
    return(I_zz)

def I_yy(h_a, C_a, t_sk, h_st, w_st, t_st, N_st, t_sp, st_cord, cg):
    
    h_a = h_a/100
    t_sk = t_sk/1000
    h_st = h_st/100
    w_st = w_st/100
    t_st = t_st/1000
    t_sp = t_sp/1000
    
    # Create a list to store all elements which need to be summed.
    I_yy = []
    # Defining list of z coordinates and the z location of the cg.
    z_cord = [cord[0] for cord in st_cord]
    cg_z = cg[0]
    
    # Calculate the MOI zz of the semicircle element.
    I_sc = 1/8*np.pi*((0.5*h_a)**4-(0.5*h_a-t_sk)**4)
    I_yy.append(I_sc)
    
    # Calculate Steiner term for the semicircle
    cg_zsc = (4*0.5*h_a)/(3*np.pi)
    dy_sc = abs(cg_z - cg_zsc)
    A_sc = 0.5*np.pi*((0.5*h_a)**2-(0.5*h_a-t_sk)**2)
    S_sc = A_sc*(dy_sc**2)
    I_yy.append(S_sc)
    
    # Calculate the MOI zz of the skin elements.
    phi = np.arctan((0.5*h_a)/(C_a - 0.5*h_a))
    L_sk = ((0.5*h_a)**2+(C_a-(0.5*h_a))**2)**0.5
    I_sk = 1/12*t_sk*(L_sk**3)*(np.cos(phi))**2
    I_yy += 2*[I_sk]
    
    # Calculate the Steiner term of the skin elements. 
    A_sk = L_sk*t_sk
    cg_zsk = 0.5*L_sk*np.cos(phi)*-1
    S_sk = A_sk*(abs(cg_z-cg_zsk))**2
    I_yy += 2*[S_sk]
    
    # Calculate the MOI zz of the spar element.
    I_sp = 1/12*(h_a)*t_sp**3
    I_yy.append(I_sp)
    
    # Calculate the Steiner term of the skin element.
    A_sp = h_a*t_sp
    dz_sp = abs(cg_z)
    S_sp = A_sp*dz_sp**2
    I_yy.append(S_sp)
    
    # Calculate the Steiner term of the stringers.
    A_st = (h_st*t_st)+(w_st*t_st)
    
    for i in range(N_st):
        dz_st = abs(cg_z - z_cord[i])
        S_st = A_st * dz_st**2
        I_yy.append(S_st)
        
    I_yy = sum(I_yy)
    return(I_yy)
