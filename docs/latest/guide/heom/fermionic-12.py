from qutip.nonmarkov.heom import FermionicBath

# Padé expansion:
bath_L = FermionicBath(Q, ck_plus_L, vk_plus_L, ck_minus_L, vk_minus_L)
bath_R = FermionicBath(Q, ck_plus_R, vk_plus_R, ck_minus_R, vk_minus_R)