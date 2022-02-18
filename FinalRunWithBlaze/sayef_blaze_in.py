from phylanx import Phylanx, PhylanxSession
import numpy as np
import time

PhylanxSession.init(16)

N = 2048


@Phylanx
def dgemm_halide_in(N):
    alpha = 2
    beta = 1
    A = np.ones((N, N))
    B = np.ones((N, N))
    C = np.ones((N, N))
    return blaze_dgemm(False, False, alpha, A, B, beta, C)

c_halide_in = dgemm_halide_in(N)

b_halide_in = time.time()
c_halide_in = dgemm_halide_in(N)
e_halide_in = time.time()

print('halide_in', e_halide_in - b_halide_in)

