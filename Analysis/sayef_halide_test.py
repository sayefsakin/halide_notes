from phylanx import Phylanx, PhylanxSession
import numpy as np
import time

PhylanxSession.init(16)

N = 2048


@Phylanx
def dgemm_halide(alpha, A, B, beta, C):
    return dgemm(False, False, alpha, A, B, beta, C)


A = np.ones((N, N))
B = np.ones((N, N))
C = np.ones((N, N))

c_halide = dgemm_halide(2, A, B, 1, C)

b_halide = time.time()
c_halide = dgemm_halide(2, A, B, 1, C)
e_halide = time.time()

print('halide', e_halide - b_halide)


@Phylanx
def dgemm_halide_in(N):
    alpha = 2
    beta = 1
    A = np.ones((N, N))
    B = np.ones((N, N))
    C = np.ones((N, N))
    return dgemm(False, False, alpha, A, B, beta, C)

c_halide_in = dgemm_halide_in(N)

b_halide_in = time.time()
c_halide_in = dgemm_halide_in(N)
e_halide_in = time.time()

print('halide_in', e_halide_in - b_halide_in)

