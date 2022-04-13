times = [0.0, 1.0]
result = mesolve(H, psi0, times, [], [])
result.states # doctest: +NORMALIZE_WHITESPACE
# [Quantum object: dims = [[2], [1]], shape = (2, 1), type = ket
# Qobj data =
# [[1.]
# [0.]], Quantum object: dims = [[2], [1]], shape = (2, 1), type = ket
# Qobj data =
# [[0.80901699+0.j        ]
# [0.        -0.58778526j]]]
