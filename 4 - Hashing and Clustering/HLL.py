import re
import numpy as np
from math import log, sqrt
from tqdm import tqdm


def alpha_costant(m):
    if m == 16:
        return 0.673
    if m == 32:
        return 0.697
    if m == 64:
        return 0.709

    if m >= 128:
        return 0.7213/(1+1.079/m)


def leftmost_one(bits):

    result = re.search('0*1', bits)

    return result.end(0)


def get_bucket_size(e):

    m_1 = (1.04/e)**2
    k = int(log(m_1, 2)) + 1

    return 2**k, k


def HyperLogLog(stream, error):

    m, k = get_bucket_size(error)

    M = np.zeros(m, 'd')

    for x in tqdm(stream):

        x = x[:-1]

        j = int(x[:k], 2)

        M[j] = max(M[j], leftmost_one(x[k:]))


    E = alpha_costant(m)*(m**2)/sum(2**(-M))

    # corrections
    if E <= (5/2)*m:

        if 0 in M:
            E = m*log(m/sum(M == 0), 10) # small range correction

            return E, E*1.04/sqrt(m)

        else:
            return E, E*1.04/sqrt(m)

    if E <= (2**64)/30:

        return E, E*1.04/sqrt(m) # no correction

    if E > (2**64)/30:

        E = -(2**64)*log(1-E/(2**64)) # large range correction

        return E, E*1.04/sqrt(m)
