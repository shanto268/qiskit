from matplotlib import pyplot as plt
import numpy as np
from qiskit import *
from qiskit.visualization import plot_bloch_vector

plt.figure()
ax = plt.gca()
ax.quiver([3], [5], angles='xy', scale_units='xy', scale=1)
ax.set_xlim([-1, 10])
ax.set_ylim([-1, 10])
#plt.draw()
#plt.show()

plot_bloch_vector([1, 0, 0])

"""
Matrices:
    A unitary matrix is very similar. Specifically, it is a matrix such that the inverse matrix is equal to the conjugate transpose of the original matrix.
    A Hermitian matrix is simply a matrix that is equal to its conjugate transpose (denoted with a †  symbol).
"""
