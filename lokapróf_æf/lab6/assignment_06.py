import sys
sys.path.append('..')
from vec import Vec
from matutil import coldict2mat
from solver import solve


EPS = 1e-14


def is_superfluous(L, i):
    '''
    Input:
        - L: list of vectors as instances of Vec class
        - i: integer in range(len(L))
    Output:
        True if the span of the vectors of L is the same
        as the span of the vectors of L, excluding L[i].

        False otherwise.
    Examples:
        >>> D={'a','b','c','d'}
        >>> L = [Vec(D, {'a':1,'b':-1}), Vec(D, {'c':-1,'b':1}), Vec(D, {'c':1,'d':-1}), Vec(D, {'a':-1,'d':1}), Vec(D, {'b':1, 'c':1, 'd':-1})]
        >>> is_superfluous(L,2)
        True
        >>> is_superfluous([Vec({0,1}, {0:1})], 0)
        False
    '''
    if len(L) == 1:
        return L[i] == Vec(L[0].D, {})
    A = coldict2mat([L[j] for j in range(len(L)) if j != i])
    b = L[i]

    x = solve(A, b)
    residual = A*x - b
    if residual*residual < EPS:
        return True
    else:
        return False


def is_independent(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - boolean: True if vectors in L are linearly independent
    Example:
        >>> vlist = [Vec({0, 1, 2},{0: 1}), Vec({0, 1, 2},{1: 1}), Vec({0, 1, 2},{2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1})]
        >>> is_independent(vlist)
        False
        >>> is_independent(vlist[:2])
        True
    '''
    pass


def is_dependent(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - boolean: True if vectors in L are linearly independent
    Example:
        >>> vlist = [Vec({0, 1, 2},{0: 1}), Vec({0, 1, 2},{1: 1}), Vec({0, 1, 2},{2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1})]
        >>> is_dependent(vlist)
        True
        >>> is_dependent(vlist[:2])
        False
    '''
    pass


def subset_basis(T):
    '''
    Input:
        - T: a list of Vecs
    Output: 
        - list S containing Vecs from T that is a basis for the space spanned by T.
    NOTE:
        - You can use either the Grow algorithm or the Shrink algorithm.
    Examples:
        The following tests use the procedures is_superfluous and is_independent,
        written in previous problems.

        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> sb = subset_basis([a0, a1, a2, a3])
        >>> all(v in [a0, a1, a2, a3] for v in sb)
        True
        >>> is_independent(sb)
        True
        >>> all(is_superfluous([a]+sb, 0) for a in [a0, a1, a2, a3])
        True
    '''
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()