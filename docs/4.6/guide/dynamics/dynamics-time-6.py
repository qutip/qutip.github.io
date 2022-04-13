def H1_coeff(t, args):
      A = args['A']
      sig = args['sigma']
      return A * np.exp(-(t / sig) ** 2)