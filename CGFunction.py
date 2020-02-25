# -*- coding: utf-8 -*-
"""
Editor: Luuk van der Mark

Last Updated: 17-02-2020

This document contains a function to calculate the CG of the cross section of
a aileron given by the group assignment of the SVV course (AE3212-II).
"""
import numpy as np

def centroid(h_a, C_a, t_sk, h_st, w_st, t_st, N_st, t_sp):
    "This function calculates the y location of the aileorn's cross section w.r.t. the centroid of the spars."
    # Rewrite all variable for unit x to meters.
    h_a = h_a/100
    t_sk = t_sk/1000
    h_st = h_st/100
    w_st = w_st/100
    t_st = t_st/1000
    t_sp = t_sp/1000
    
    # Creating radius variable to make code more readable.
    r_a = 0.5*h_a
    
    # Creating empty list to store calculated values
    A = []
    y_til = []
    st_ycord = []
    st_zcord = []
    cg = []
    
    # Calculating the area of the semicircle.
    A_sc = 0.5*np.pi*((r_a)**2-((r_a)-t_sk)**2)
    A.append(A_sc)
    print('Area of the semicircle is ' + str(A_sc))
    
    # Calculatin the length & area of the skin.
    L_sk = ((r_a)**2+(C_a-r_a)**2)**0.5    # Length of the skin, using pythagoras.
    A_sk = L_sk*t_sk
    A += 2*[A_sk]
    print(L_sk, A_sk)
    # Calculating the area of the spar.
    A_sp = h_a*t_sp
    A.append(A_sp)
    
    # Calculating the area of the stringer.
    A_st = (h_st*t_st)+(w_st*t_st)
    # Append A_st, N_st times to a list.
    A += N_st*[A_st]
    print(A_st)
    # Calculating y_tilde for the semicircle.
    y_tsc = (4*r_a)/(3*np.pi)
    y_til.append(y_tsc)
    print(y_tsc)
    # Calculating y_tilde for the skin.
    phi = np.arctan((r_a)/(C_a - r_a))
    y_tsk = -0.5*L_sk*np.cos(phi)
    y_til += 2*[y_tsk]
    
    print(y_tsk)
    # Calculating y_tilde for the spar.
    y_tsp = 0                               # Due to reference frame this will always be zero.
    y_til.append(y_tsp)                     # Done such that both the list A and y_til will be of equal length.
    
    # Calculating y_tilde for the stringers
    d_st = (np.pi*r_a + 2*L_sk)/N_st
    
    # Checking in which of the four segments the stringer is.
    for i in range(N_st):
        # Checking if the stringer is in the 1st segment.
        if i*d_st <= 0.5*np.pi*r_a:
            # Calculating y_tst for stringers in the 1st segment (z coordinate).
            theta = i*d_st/r_a
            y_tst = np.cos(theta)*r_a
            y_til.append(y_tst)
            st_zcord.append(y_tst)

            # Calculating z_tst coordinate for stringers in the 1st segment (y coordinate).
            z_tst = np.sin(theta)*r_a
            st_ycord.append(z_tst)
            
        # Checking if stringer is in the 2nd segment.
        if i*d_st > 0.5*np.pi*r_a and i*d_st <= 0.5*np.pi*r_a + L_sk:
            # Calculating y_tst for stringers in the 2nd segment.
            Q = i*d_st - 0.5*np.pi*r_a
            y_tst = Q*np.cos(phi)*-1
            y_til.append(y_tst)
            st_zcord.append(y_tst)

            # Calculating z_tst for stringers in the 2nd segment.
            z_tst = r_a - Q*np.sin(phi)
            st_ycord.append(z_tst)
            
        # Checking if stringer is in the 3rd segment.
        if i*d_st > 0.5*np.pi*r_a + L_sk and i*d_st <= 0.5*np.pi*r_a + 2*L_sk:
            # Calculating y_tst for stringers in the 3rd segment.
            P = i*d_st - ( 0.5*np.pi*r_a + L_sk )
            y_tst = (C_a - r_a - P*np.cos(phi))*-1
            y_til.append(y_tst)
            st_zcord.append(y_tst)
        
            # Calculating z_tst for stringers in the 3rd segment.
            z_tst = P*np.sin(phi)*-1
            st_ycord.append(z_tst)
            
        # Checking if stringers is in the 4th segment.
        if i*d_st > 0.5*np.pi*r_a + 2*L_sk:
            # Calculating y_tst for stringers in the 4th segment.
            R = i*d_st - (0.5*np.pi*r_a + 2*L_sk)
            alpha = R / r_a
            y_tst = r_a*np.sin(alpha)
            y_til.append(y_tst)
            st_zcord.append(y_tst)
      
            # Calculating z_tst for stringers in the 4th segment.
            z_tst = r_a*np.cos(alpha) * -1
            st_ycord.append(z_tst)
    
    st_cord = list(zip(st_zcord,st_ycord))
    # Multiply all elements of the area list with the y_til list
    Ay_til = [a*b for a, b in zip(A, y_til)]
    print(Ay_til)
    print(sum(Ay_til))
    # Divide the elements of the Ay_til list with the A list, to obtain z coordinate of the cg. 
    cg_z = sum(Ay_til)/sum(A)
    cg.append(cg_z)
    cg += [0]
    
    return(st_cord, cg)

