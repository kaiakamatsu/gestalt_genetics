import sys
import numpy as np
from maxgcp import fit_heritability

P = np.loadtxt(sys.argv[1])
PE = np.loadtxt(sys.argv[2])
G = P - PE

W = fit_heritability(G.T @ G, P.T @ P)
sums_and_diffs = np.ones((P.shape[1],2))
sums_and_diffs[::2,1] = -1

np.savetxt(sys.argv[3],P @ W)
np.savetxt(sys.argv[4],P @ sums_and_diffs)
