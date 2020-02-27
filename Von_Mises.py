# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:39:18 2020
@author: rdenb
"""

# from aircraft_data import *
import numpy as np

def Safe_divide(a,b):
    if a == 0 or b == 0:
        x = 0
    else:
        x = a/b
    return x

def Von_Mises_Calc(Mi,q,dts=0.001,N=1000):
    C_a = 0.6
    h_a = 0.2
    CoG = [0,-0.05] # [cg_y,cg_z]
    t_sk = 1.1/1000
    t_sp = 2.9/1000
    I_zz = 1
    I_yy = 1
    
    # Geometric properties
    r = h_a/2 # Radius of leading edge
    slen = np.sqrt(r*r+(C_a-r)*(C_a-r)) # Distance top-spar to trailing edge
    
    # Functions to be used in every loop
    func = [[lambda theta: r*np.sin(theta),lambda s: r-s*r/slen,lambda s: -s*r/slen,lambda theta: -r*np.cos(theta),lambda s: r-s],
        [lambda theta: r*np.cos(theta),lambda s: -(C_a-r)*s/slen,lambda s: -(C_a-r)+(C_a-r)*s/slen,lambda theta:r*np.sin(theta) ,lambda s: 0*s]]
    bounds = [[0,np.pi/2],[0,slen],[0,slen],[0,np.pi],[0,h_a]]
    ds = [dts/r,dts,dts,dts/r,dts]
    t = [t_sk,t_sk,t_sk,t_sk,t_sp]
    
    # List to store results
    Tensile = []
    VonMises = []
    # For every x-coordinate given in N
    for i in range(N):
        # Alter shape of results-lists to mimic q
        Tensile.append([])
        VonMises.append([])
        for k in range(5):
            # Alter shape of results-lists to mimic q
            Tensile.append([])
            VonMises.append([])
            # Determine coordinates
            s = np.arange(bounds[k][0],bounds[k][1],ds[k])
            y_vec = func[0][k](s)        
            z_vec = func[1][k](s)
            Shearflow = q[i][k]
            for j in range(len(Shearflow)):
                ys = y_vec[j]
                zs = z_vec[j] - CoG[1]
                My = Mi[0][i]
                Mz = Mi[1][i]
                # Calculate stresses
                tau_yz = Shearflow[j]*t[k]
                sigma_xx = Safe_divide(-1*(My*ys),I_zz) + Safe_divide(-1*(Mz*zs),I_yy)
                # Calculate VON MISES stress
                Y = np.sqrt((sigma_xx**2)+(3*(tau_yz**2)))
                # Store results
                Tensile.append(sigma_xx)
                VonMises.append(Y)              
    return VonMises,Tensile
