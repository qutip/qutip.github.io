b = qutip.Bloch()

pnt = [1./np.sqrt(3), 1./np.sqrt(3), 1./np.sqrt(3)]
b.add_points(pnt)
vec = [0, 1, 0]
b.add_vectors(vec)
up = qutip.basis(2, 0)
b.add_states(up)
b.render()