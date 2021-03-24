import numpy as np

#string as input, list as output
def split_hex(strings):
    aux = []
    for i in range(0,len(strings)):
        aux.append(int(strings[i],16))
    return np.array(aux)


def p_pow(n, p):
  return np.array([p**i for i in range(n)])



def get_combination (x, coeff, modulo):
    return sum(x*coeff)%modulo


def has_function1(hex_string, p, prime):
    m = {}
    hex_splitted =split_hex(hex_string)
    coeff = p_pow(len(hex_splitted), p)
    keys  = get_combination(hex_splitted, coeff, prime)
    return format(keys, 'b').zfill(64)
