def exp_current(aux, exp):
    """ Calculate the current for a single exponent. """
    sign = 1 if exp.type == exp.types["+"] else -1
    op = exp.Q if exp.type == exp.types["+"] else exp.Q.dag()
    return 1j * sign * (op * aux).tr()

def heom_current(tag, ado_state):
    """ Calculate the current between the system and the given bath. """
    level_1_ados = [
        (ado_state.extract(label), ado_state.exps(label)[0])
        for label in ado_state.filter(tags=[tag])
    ]
    return np.real(sum(exp_current(aux, exp) for aux, exp in level_1_ados))

heom_left_current = lambda t, ado_state: heom_current("L", ado_state)
heom_right_current = lambda t, ado_state: heom_current("R", ado_state)