import FDM
import torsion as TORS
import CGFunction as CG
import Ifunction as IFUNC

N = 1000
dtx,dtz,dty,dts =

st_cord,cgy = CG.centroid()
I = [IFUNC.I_zz(st_cord,cgy),IFUNC.I_yy(st_cord,cg)]
Mi,Vi,Vr,Va = FDM.bending_solve(N,I,dtz)
q = TORS.get_q(Vi,N,I,dtx,dtz,dts)