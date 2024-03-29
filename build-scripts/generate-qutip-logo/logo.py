# QuTiP Logo script.
# Requires Python 2.7 since using mayavi2

import numpy as np
from qutip import *
import mayavi.mlab as mlab


N=20
psi=(basis(N,0)+basis(N,2)+basis(N,6)).unit()
xvec=np.linspace(-3.0,3.0,300)
W=wigner(psi,xvec,xvec)

fig=mlab.figure(size=(2048,1536))
X, Y = np.meshgrid(xvec,xvec)
mlab.surf(W, warp_scale="auto",colormap='cool',figure=fig)
mlab.show()
