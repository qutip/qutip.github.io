def H1_coeff(t, args):
    return args['A'] * np.exp(-(t/args['sigma'])**2)