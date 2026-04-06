from vec import Vec
from mat import Mat
from matutil import *
from nullspace import nullspace
import math

def is_eigenpair(A, v, lam):
    '''
    Input:
        - A: a Mat representing the matrix
        - v: a Vec representing the eigenvector candidate
        - lam: a scalar value

    Output:
        - A boolean indicating whether the provided vector and scalar form an eigenpair of A
    '''
    return A * v == lam * v


def find_eigenvalues_and_vectors(A):
    '''
    Input:
        - A: a 2x2 Mat

    Output:
        - (eigvals, eigvecs): a tuple where eigvals is a list of eigenvalues (floats),
          and eigvecs is a list of Vecs corresponding to each eigenvalue
    '''
    trace = A[0,0] + A[1,1]
    det = A[0,0]*A[1,1] - A[1,0]*A[0,1]

    eigvals = []
    eigvecs = []

    discrim = (trace**2 - 4*det)
    if discrim > 0:
        lam1 = (trace + math.sqrt(discrim)) / 2
        lam2 = (trace - math.sqrt(discrim)) / 2

        eigenvec1 = nullspace(A - lam1*identity(A.D[1], 1))
        eigenvec2 = nullspace(A - lam2*identity(A.D[1], 1))

        eigvals.append(lam1)
        eigvals.append(lam2)

        eigvecs.append(eigenvec1[0])
        eigvecs.append(eigenvec2[0])

    elif discrim == 0:
        lam = trace / 2

        eigvec = nullspace(A - lam*identity(A.D[1], 1))

        for vec in eigvec:
            eigvecs.append(vec)
            eigvals.append(lam)

    return (eigvals, eigvecs)


def is_diagonalizable(A):
    '''
    Input:
        - A: a Mat

    Output:
        - True if A is diagonalizable, False otherwise
    '''
    eigvals, eigvecs = find_eigenvalues_and_vectors(A)

    
    return len(A.D[0]) == len(eigvecs)


def construct_markov_matrix(a, b):
    '''
    Input:
        - a: a scalar
        - b: a scalar

    Output:
        - A: a 2x2 column-stochastic matrix with parameters a and b with D = ({0, 1}, {0, 1})
    '''
    dom = {}

    dom[(0,0)] = 1-a
    dom[(0,1)] = b
    dom[(1,0)] = a
    dom[(1,1)] = 1-b

    return Mat(({0,1}, {0,1}), dom)


def markov_eigenvalues_and_vectors(a, b):
    '''
    Input:
        - a: scalar
        - b: scalar

    Output:
        - eigenvalues: a list of eigenvalues
        - eigenvectors: a list of corresponding eigenvectors
    '''
    mat = construct_markov_matrix(a,b)

    return find_eigenvalues_and_vectors(mat)

