import numpy as np

def centroid_y(h_a, C_a, t_sk, h_st, w_st, t_st, N_st, t_sp):
    "This function calculates the y location of the aileorn's cross section w.r.t. the centroid of the spars."
    
    # Creating empty list to store calculated area's
    A = []
    y_til = []
    st_ycord = []
    st_zcord = []  
    
    # Calculating the area of the semicircle.
    A_sc = np.pi*(h_a**2-(h_a-t_sk)**2)
    A.append(A_sc)
    
    # Calculatin the length & area of the skin.
    L_sk = ((0.5*h_a)**2+(C_a-h_a)**2)**0.5    # Length of the skin, using pythagoras.
    A_sk = L_sk*t_sk
    A.append(A_sk)
    
    # Calculating the area of the spar.
    A_sp = h_a*t_sp
    A.append(A_sp)
    
    # Calculating the area of the stringer.
    A_st = (h_st*t_st)+(w_st*t_st)
    # Append A_st, N_st times to a list.
    A += N_st*[A_st]
    
    # Calculating y_tilde for the semicircle.
    y_tsc = (4*h_a)/(3*np.pi)
    y_til.append(y_tsc)
    
    # Calculating y_tilde for the skin.
    phi = np.arctan((0.5*h_a)/(C_a-h_a))
    y_tsk = 0.5*L_sk*np.cos(phi)
    y_til.append(y_tsk)
    
    # Calculating y_tilde for the spar.
    y_tsp = 0                               # Due to reference frame this will always be zero.
    y_til.append(y_tsp)                     # Done such that both the list A and y_til will be of equal length.
    
    # Calculating y_tilde for the stringers
    d_st = (np.pi*h_a+2*L_sk)/N_st

    # Checking in which of the four segments the stringer is.
    for i in range(N_st):
        # Checking if the stringer is in the 1st segment.
        if i*d_st <= 0.5*np.pi*h_a:
            # Calculating y_tst for stringers in the 1st segment (z coordinate).
            theta = i*d_st/(0.5*np.pi*h_a)
            y_tst = np.cos(theta)*0.5*h_a
            y_til.append(y_tst)
            st_zcord.append(y_tst)
            print(1)
            # Calculating z_tst coordinate for stringers in the 1st segment (y coordinate).
            z_tst = np.sin(theta)*0.5*h_a
            st_ycord.append(z_tst)
            
        # Checking if stringer is in the 2nd segment.
        if i*d_st > 0.5*np.pi*h_a and i*d_st <= 0.5*np.pi*h_a + L_sk:
            # Calculating y_tst for stringers in the 2nd segment.
            Q = i*d_st - 0.5*np.pi*h_a
            y_tst = Q*np.cos(phi)
            y_til.append(y_tst)
            st_zcord.append(y_tst)
            print(2)
            # Calculating z_tst for stringers in the 2nd segment.
            z_tst = Q*np.sin(phi)
            st_ycord.append(z_tst)
            
        # Checking if stringer is in the 3rd segment.
        if i*d_st > 0.5*np.pi*h_a + L_sk and i*d_st <= 0.5*np.pi*h_a + 2*L_sk:
            # Calculating y_tst for stringers in the 3rd segment.
            P = i*d_st - 0.5*np.pi*h_a - L_sk
            y_tst = (C_a - 0.5*h_a) - P*np.cos(phi)
            y_til.append(y_tst)
            st_zcord.append(y_tst)
            print(3)
            # Calculating z_tst for stringers in the 3rd segment.
            z_tst = ((C_a - 0.5*h_a) - P*np.sin(phi))*-1
            st_ycord.append(z_tst)
            
        # Checking if stringers is in the 4th segment.
        if i*d_st > 0.5*np.pi*h_a + 2*L_sk:
            # Calculating y_tst for stringers in the 4th segment.
            R = i*d_st - 0.5*np.pi*h_a - 2*L_sk
            alpha = R / 0.5*np.pi*h_a
            y_tst = 0.5*h_a*np.sin(alpha)
            y_til.append(y_tst)
            st_zcord.append(y_tst)
            print(4)
            # Calculating z_tst for stringers in the 4th segment.
            z_tst = 0.5*h_a*np.cos(alpha) * -1
            st_ycord.append(z_tst)
    
    st_cord = list(zip(st_zcord,st_ycord))
    
    
    return(st_cord)