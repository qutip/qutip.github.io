T = 2*np.pi / omega
f_modes_0, f_energies = floquet_modes(H, T, args)
f_energies # doctest: +NORMALIZE_WHITESPACE
# array([-2.83131212,  2.83131212])
f_modes_0 # doctest: +NORMALIZE_WHITESPACE
# [Quantum object: dims = [[2], [1]], shape = (2, 1), type = ket
# Qobj data =
# [[ 0.72964231+0.j      ]
# [-0.39993746+0.554682j]],
# Quantum object: dims = [[2], [1]], shape = (2, 1), type = ket
# Qobj data =
# [[0.39993746+0.554682j]
# [0.72964231+0.j      ]]]
