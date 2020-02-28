import numpy as np

def get_arm(r,cl,ts,tb,dt,s_space):
    slen = np.sqrt(r*r+(cl-r)*(cl-r))
    y1 = []
    y1_bounds = []
    y1_dt_list = []
    #yi.append are the arms of the shearflow

    y1_bounds.append([0,np.pi/2])
    y1.append(lambda theta: r*r)
    y1_dt_list.append(dt/r)

    y1_bounds.append([0,2*r])
    y1.append(lambda s: 0)
    y1_dt_list.append(dt)


    y1_bounds.append([-np.pi/2,0])
    y1.append(lambda theta: r*r)
    y1_dt_list.append(dt/r)

    y2 = []
    y2_bounds = []
    y2_dt_list = []

    y2_bounds.append([0,r])
    y2.append(lambda s: 0)
    y2_dt_list.append(dt)

    y2_bounds.append([0,slen])
    y2.append(lambda s: r)
    y2_dt_list.append(dt)

    y2_bounds.append([0,slen])
    y2.append(lambda s: r)
    y2_dt_list.append(dt)

    y2_bounds.append([0,r])
    y2.append(lambda s: 0)
    y2_dt_list.append(dt)

    y_a = [[y1,y1_bounds,y1_dt_list],[y2,y2_bounds,y2_dt_list]]
    return [y_a]
