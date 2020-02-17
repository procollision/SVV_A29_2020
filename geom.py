def get_geom(r,cl):
    y1 = []
    y1_bounds = []
    y1_bounds.append([0,pi/2])
    y1.append(lambda theta: r*r*np.sin(theta))
    y1_bounds.append([0,2*r])
    y1.append(lambda s: -r*s+r)
    y1_bounds.append([-pi/2,0])
    y1.append(lambda theta: r*r*np.sin(theta))

    y2 = []
    y2_bounds = []
    y2_bounds.append([0,r])
    y2.append(lambda s: s)
    y2_bounds.append([0,2*np.sqrt(r*r+(cl-r)*(cl-r))])
    y2.append(lambda s: -r/(np.sqrt(r*r+(cl-r)*(cl-r)))*s+r)
    y2_bounds.append([0,r])
    y2.append(lambda theta: s-r)

    y_s= [[y1,y1_bounds],[y2,y2_bounds]]
    z_s = []
    return[y_s,z_s]


