from vec import Vec
from mat import Mat
from matutil import *
from nullspace import nullspace


def is_eigenpair(A, v, lam):
    '''
    Input:
        - A: a Mat representing the matrix
        - v: a Vec representing the eigenvector candidate
        - lam: a scalar value

    Output:
        - A boolean indicating whether the provided vector and scalar form an eigenpair of A
    '''
    pass


def find_eigenvalues_and_vectors(A):
    '''
    Input:
        - A: a 2x2 Mat

    Output:
        - (eigvals, eigvecs): a tuple where eigvals is a list of eigenvalues (floats),
          and eigvecs is a list of Vecs corresponding to each eigenvalue
    '''
    pass


def is_diagonalizable(A):
    '''
    Input:
        - A: a Mat

    Output:
        - True if A is diagonalizable, False otherwise
    '''
    pass


def construct_markov_matrix(a, b):
    '''
    Input:
        - a: a scalar
        - b: a scalar

    Output:
        - A: a 2x2 column-stochastic matrix with parameters a and b with D = ({0, 1}, {0, 1})
    '''
    pass


def markov_eigenvalues_and_vectors(a, b):
    '''
    Input:
        - a: scalar
        - b: scalar

    Output:
        - eigenvalues: a list of eigenvalues
        - eigenvectors: a list of corresponding eigenvectors
    '''
    pass

