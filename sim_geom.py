import numpy as np

def get_geom(r,cl,ts,tb,dt,s_space,CG_z):
    y1 = []
    y1_bounds = []
    y1_thickness = []
    y1_stringer = []
    y1_dt_list = []
    y1_offset = []
    y1_stringer_index = []

    y1_bounds.append([0,np.pi/2])
    y1.append(lambda theta: r*r*np.sin(theta))
    y1_thickness.append(ts)
    y1_stringer.append(1)
    y1_dt_list.append(dt/r)
    y1_offset.append(s_space/r)
    y1_stringer_index.append(range(0,3))

    y1_bounds.append([0,2*r])
    y1.append(lambda s: -r*s+r)
    y1_thickness.append(tb)
    y1_stringer.append(0)
    y1_dt_list.append(dt)
    y1_offset.append(0)
    y1_stringer_index.append([0])

    y1_bounds.append([0.0,np.pi/2])
    y1.append(lambda theta: r*r*np.sin(theta-r))
    y1_thickness.append(ts)
    y1_stringer.append(1)
    y1_dt_list.append(dt/r)
    y1_offset.append((0.5*np.pi*r)%s_space/r)
    y1_stringer_index.append(range(15,17))


    y2 = []
    y2_bounds = []
    y2_thickness = []
    y2_stringer = []
    y2_dt_list = []
    y2_offset = []
    y2_stringer_index = []

    y2_bounds.append([0,r])
    y2.append(lambda s: s-CG_y)
    y2_thickness.append(tb)
    y2_stringer.append(0)
    y2_dt_list.append(dt)
    y2_offset.append(0)
    y2_stringer_index.append([0])

    y2_bounds.append([0,np.sqrt(r*r+(cl-r)*(cl-r))])
    y2.append(lambda s: -r/(np.sqrt(r*r+(cl-r)*(cl-r)))*s+r)
    y2_thickness.append(ts)
    y2_stringer.append(1)
    y2_dt_list.append(dt)
    y2_offset.append(s_space-(0.5*np.pi*r)%s_space)
    y2_stringer_index.append(range(3,9))

    y2_bounds.append([0,np.sqrt(r*r+(cl-r)*(cl-r))])
    y2.append(lambda s: -r/(np.sqrt(r*r+(cl-r)*(cl-r)))*s)
    y2_thickness.append(ts)
    y2_stringer.append(1)
    y2_dt_list.append(dt)
    y2_offset.append(s_space-(0.5*np.pi*r)%s_space)
    y2_stringer_index.append(range(9,15))


    y2_bounds.append([0,r])
    y2.append(lambda s: s-r)
    y2_thickness.append(tb)
    y2_stringer.append(0)
    y2_dt_list.append(dt)
    y2_offset.append(0)
    y2_stringer_index.append([0])



    z1 = []
    z1_bounds = []
    z1_thickness = []
    z1_stringer = []
    z1_dt_list = []
    z1_offset = []
    z1_stringer_index = []

    z1_bounds.append([0,np.pi/2])
    z1.append(lambda theta: r*r*np.cos(theta)-CG_z)
    z1_thickness.append(ts)
    z1_stringer.append(1)
    z1_dt_list.append(dt/r)
    z1_offset.append(s_space/r)
    z1_stringer_index.append(range(0,3))

    z1_bounds.append([0,2*r])
    z1.append(lambda s: 0-CG_z)
    z1_thickness.append(tb)
    z1_stringer.append(0)
    z1_dt_list.append(dt)
    z1_offset.append(0)
    z1_stringer_index.append([0])

    z1_bounds.append([0,np.pi/2])
    z1.append(lambda theta: r*r*np.cos(theta)-r-CG_z)
    z1_thickness.append(ts)
    z1_stringer.append(1)
    z1_dt_list.append(dt/r)
    z1_offset.append((0.5*np.pi*r)%s_space/r)
    z1_stringer_index.append(range(15,17))



    z2 = []
    z2_bounds = []
    z2_thickness = []
    z2_stringer = []
    z2_dt_list = []
    z2_offset = []
    z2_stringer_index = []

    z2_bounds.append([0,r])
    z2.append(lambda s: 0-CG_z)
    z2_thickness.append(tb)
    z2_stringer.append(0)
    z2_dt_list.append(dt)
    z2_offset.append(0)
    z2_stringer_index.append([0])

    z2_bounds.append([0,np.sqrt(r*r+(cl-r)*(cl-r))])
    z2.append(lambda s: -s*np.sqrt((cl/r-1)*(cl/r-1)+1)-CG_z)
    z2_thickness.append(ts)
    z2_stringer.append(1)
    z2_dt_list.append(dt)
    z2_offset.append(s_space-(0.5*np.pi*r)%s_space)
    z2_stringer_index.append(range(3,9))

    z2_bounds.append([0,np.sqrt(r*r+(cl-r)*(cl-r))])
    z2.append(lambda s: s*np.sqrt((cl/r-1)*(cl/r-1)+1)-(cl-r)-CG_z)
    z2_thickness.append(ts)
    z2_stringer.append(1)
    z2_dt_list.append(dt)
    z2_offset.append(0.5*s_space)
    z2_stringer_index.append(range(9,15))

    z2_bounds.append([0,r])
    z2.append(lambda s: 0-CG_z)
    z2_thickness.append(tb)
    z2_stringer.append(0)
    z2_dt_list.append(dt)
    z2_offset.append(0)
    z2_stringer_index.append([0])

    y_s = [[y1,y1_bounds,y1_stringer,y1_thickness,y1_dt_list,y1_offset,y1_stringer_index],[y2,y2_bounds,y2_stringer,y2_thickness,y2_dt_list,y2_offset,y2_stringer_index]]
    z_s = [[z1,z1_bounds,z1_stringer,z1_thickness,z1_dt_list,z1_offset,z1_stringer_index],[z2,z2_bounds,z2_stringer,z2_thickness,z2_dt_list,z2_offset,z2_stringer_index]]
    return[y_s,z_s]
