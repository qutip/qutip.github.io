tlist = np.linspace(0, 15.0, 1000)

psi0 = rand_ket(2)

e_ops = [sigmax(), sigmay(), sigmaz()]

expt_list = bloch_redfield_solve(R, ekets, psi0, tlist, e_ops)

sphere = Bloch()

sphere.add_points([expt_list[0], expt_list[1], expt_list[2]])

sphere.vector_color = ['r']

sphere.add_vectors(np.array([delta, 0, eps0]) / np.sqrt(delta ** 2 + eps0 ** 2))

sphere.make_sphere()