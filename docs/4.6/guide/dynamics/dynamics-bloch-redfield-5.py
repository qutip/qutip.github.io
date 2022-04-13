ohmic = "{gamma1} / 2.0 * (w / (2 * pi)) * (w > 0.0)".format(gamma1=gamma1)

output = brmesolve(H, psi0, tlist, a_ops=[[sigmax(),ohmic]], e_ops=e_ops)