from vec import Vec
from mat import Mat
from matutil import *
import math
import svd


def reconstruct_from_svd(U, S, V):
    '''
    Input: 
        - U: a Mat representing the left singular vectors
        - S: a diagonal Mat with singular values
        - V: a Mat representing the right singular vectors

    Output:
        - A Mat representing the reconstructed matrix A
    '''
    transposed_v = V.transpose()
    return U * S * transposed_v


def frobenius_norm(A):
    '''
    Input:
        - A: a Mat

    Output:
        - A float representing the Frobenius norm of A
    '''
    values = []
    for val in A.f.values():
        values.append(val)
    
    return math.sqrt(sum(val**2 for val in values))


def rank1_approx(U, S, V):
    '''
    Input:
        - U: a Mat of left singular vectors
        - S: a diagonal Mat of singular values
        - V: a Mat of right singular vectors

    Output:
        - A Mat representing the best rank-1 approximation of the original matrix
    '''
    all_keys = sorted(S.f.keys())
    first_key = all_keys[0][0]

    new_S_dict = {}
    for key, val in S.f.items():
        if key == (first_key, first_key):
            new_S_dict[key] = val
        else:
            new_S_dict[key] = 0
    
    new_S = Mat((S.D[0], S.D[1]), new_S_dict)

    return reconstruct_from_svd(U, new_S, V)
        



def frobenius_norm_rank1_approx(U, S, V):
    '''
    Input:
        - U: a Mat of left singular vectors
        - S: a diagonal Mat of singular values
        - V: a Mat of right singular vectors

    Output:
        - A float representing the Frobenius norm of the best rank-1 approximation
    '''
    return frobenius_norm(rank1_approx(U,S,V))


def solve_least_squares(A, b):
    '''
    Input:
        - A: a Mat representing the matrix in the system Ax ≈ b
        - b: a Vec representing the right-hand side vector

    Output:
        - A Vec representing the least-squares solution x
    '''
    pass

