import numpy as np
from cython_sandbox import py_matrix_multiplication
import time

"""
This is a simple demo of multiplying two matrices using a cython wrapper to a C subrountine
"""

if __name__ == '__main__':
    # Get random matrices A and B of compatible sizes
    A = np.random.randint(10, size=(1000, 500)).astype(np.float32)
    B = np.random.randint(10, size=(500, 10)).astype(np.float32)

    time_start = time.time()

    # Insure that both A and B have C contiguous format; This will cause arrays to be copied if they do not.
    A = np.ascontiguousarray(A)             # Ensures C contiguous format
    B = np.ascontiguousarray(B)             # Ensures C contiguous format
    # Compute matrix multiplication using cython wrapper
    C1 = py_matrix_multiplication(A, B)     # Requires that 2D np.ndarrays that are floats with C contiguous format

    time_end = time.time()
    print("Output from cython matrix multiplication:")
    print(C1)
    print("Cython computation time: %f sec\n" % (time_end - time_start))

    # Compute matrix multiplication using numpy
    time_start = time.time()
    C2 = np.dot(A, B)
    time_end = time.time()
    print("Output from numpy matrix multiplication:")
    print(C2)
    print("numpy computation time: %f sec\n" % (time_end - time_start))

    # Print error
    err = np.sum((C1 - C2) ** 2)
    print("L2 difference between cython and numpy.dot matrix product: %f" % err)

