import numpy as np
import CGFunction as CG
import sim_geom as GEOM
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from aircraft_data import *

def plot(q,dts,dim):
    shift =0.1
    fig, axs = plt.subplots(dim[0], dim[1], sharex=True, sharey=True)
    r = h_a/2
    slen = np.sqrt(r*r+(C_a-r)*(C_a-r))

    func = [[lambda theta: r*np.sin(theta),lambda s: r-s*r/slen,lambda s: -s*r/slen,lambda theta: -r*np.cos(theta),lambda s: r-s],
        [lambda theta: r*np.cos(theta),lambda s: -(C_a-r)*s/slen,lambda s: -(C_a-r)+(C_a-r)*s/slen,lambda theta:r*np.sin(theta) ,lambda s: 0*s]]
    bounds = [[0,np.pi/2],[0,slen],[0,slen],[0,np.pi],[0,h_a]]
    ds = [dts/r,dts,dts,dts/r,dts]

    for nr in range(len(q)):
        dydxmax = -np.inf
        dydxmin = np.inf
        for k in q[nr]:
            if  k.max()>dydxmax:
                dydxmax = k.max()
            if k.min()<dydxmin:
                dydxmax = k.min()
        i = nr%dim[0]
        j = nr//dim[1]
        for k in range(5):
            s = np.arange(bounds[k][0],bounds[k][1],ds[k])
            y = func[0][k](s)        
            x = func[1][k](s)
            
            dydx = q[k]
            
            points = np.array([x, y]).T.reshape(-1, 1, 2)
            segments = np.concatenate([points[:-1], points[1:]], axis=1)
            norm = plt.Normalize(dydxmin, dydxmax)
            
            lc = LineCollection(segments, cmap='viridis', norm=norm)
            lc.set_array(dydx)
            lc.set_linewidth(2)
            line = axs[i][j].add_collection(lc)
        fig.colorbar(line, ax=axs[i][j])
        axs[0][0].set_xlim(-(C_a-r)-shift,r+shift)
        axs[0][0].set_ylim(-r-shift, r+shift)
        axs[i][j].set_aspect(1)
    plt.show()
