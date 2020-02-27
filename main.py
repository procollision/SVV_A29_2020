import FDM_test as FDM
import torsion as TORS
import CGFunction as CG
import Ifunction as IFUNC
import plotter as PLOT

N = 1000
dtx = 0.001
dtz = 0.001
dty = 0.001
dts = 0.001


st_cord,cg = CG.centroid()
I = [IFUNC.I_zz(st_cord,cg),IFUNC.I_yy(st_cord,cg)]
print(I)
Mi,Vi,Ti,Vr,Va = FDM.bending_solve(N,I,dtz,dtx)
print("bending done")
q = TORS.get_q(Vi,Ti,N,I,dtx,dtz,dts,Vr,Va)
print("shear done")
PLOT.plot([q[round()],q[2],q[3]],dts,[2,2])
