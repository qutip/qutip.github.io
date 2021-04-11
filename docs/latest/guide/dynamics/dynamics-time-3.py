H = [H0,[H1, H1_coeff]]
output = mesolve(H, psi0, t, c_ops, [ada, sigma_UU, sigma_GG])