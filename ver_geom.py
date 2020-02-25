import numpy as np

def get_geom(r,cl,ts,tb,dt,s_space):
    y1 = []
    y1_bounds = []
    y1_thickness = []
    y1_stringer = []
    y1_dt_list = []
    y1_offset = []

    y1_bounds.append([0,2*r])
    y1.append(lambda s: r-s)
    y1_thickness.append(ts)
    y1_stringer.append(1)
    y1_dt_list.append(dt)
    y1_offset.append(0)


    y_s = [[y1,y1_bounds,y1_stringer,y1_thickness,y1_dt_list,y1_offset]]
    return[y_s]


