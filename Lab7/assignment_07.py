from matutil import coldict2mat, mat2rowdict
from solver import solve
from vec import Vec


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
    if any(is_superfluous(L, i) for i in range(len(L))):
        return False
    else:
        return True


def is_dependent(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - boolean: True if vectors in L are linearly dependent
    Example:
        >>> vlist = [Vec({0, 1, 2},{0: 1}), Vec({0, 1, 2},{1: 1}), Vec({0, 1, 2},{2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1})]
        >>> is_dependent(vlist)
        True
        >>> is_dependent(vlist[:2])
        False
    '''
    return not is_independent(L)


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
    res = T.copy()
    ind = 0
    while ind < len(res):
        if is_superfluous(res, ind):
            del res[ind]
        else:
            ind += 1
    assert is_independent(res), "{}\n{}".format(T, res)
    return res


def in_span(L, v):
    '''
    Input: 
        - L: a list of Vecs
        - v: a vector
    Output: 
        - boolean: True if v is in span L
    Example:
        >>> D={'a','b','c','d'}
        >>> L = [Vec(D, {'a':1,'b':-1}), Vec(D, {'c':-1,'b':1}), Vec(D, {'a':-1,'d':1}), Vec(D, {'b':1, 'c':1, 'd':-1})]
        >>> v = Vec(D, {'c':1,'d':-1})
        >>> in_span(L, v)
        True
        >>> in_span([], Vec({0,1}, {0:1}))
        False
    '''
    span = L[:]
    span.append(v)

    return is_dependent(span)


def my_rank(L):
    '''
    Input: 
        - L: a list of Vecs
    Output: 
        - the rank of the list of Vecs
    Example:
        >>> my_rank([Vec({0,1,2}, {0:1, 1:0, 2:0}), Vec({0,1,2}, {0:0, 1:1, 2:0}), Vec({0,1,2}, {0:0, 1:0, 2:1})])
        3
    '''
    return len(subset_basis(L))



def is_invertible(M):
    '''
    Input:
        - A matrix, M
    Output:
        - A boolean indicating if M is invertible.
    Examples:
        >>> from mat import Mat
        >>> M = Mat(({0,1,2},{0,1,2}),{(0,0):1,(0,2):2,(1,2):3,(2,2):4})
        >>> is_invertible(M)
        False
    '''
    if M.D[0] != M.D[1]:
        return False


    invert = []

    row_dict = mat2rowdict(M)

    for val in row_dict.values():
        invert.append(val)

    return is_independent(invert)


def exchange(S, A, z):
    '''
    Input:
        - S: a list of vectors, as instances of your Vec class
        - A: a list of vectors, each of which are in S, with len(A) < len(S)
        - z: an instance of Vec such that A + [z] is linearly independent
    Output: 
        - a vector w in S but not in A such that Span(S) = Span(({z} ∪ S) - {w})
    Examples:
        >>> from vec import Vec
        >>> S = [Vec({'x', 'y'}, {'x': 1, 'y': 0}), Vec({'x', 'y'}, {'x': 0, 'y': 1})]
        >>> A = [Vec({'x', 'y'}, {'x': 1, 'y': 0})]
        >>> z = Vec({'x', 'y'}, {'x': 1, 'y': 1})
        >>> exchange(S, A, z) == Vec({'x', 'y'}, {'x': 0, 'y': 1})
        True
    '''
    newl = S[:]
    newl.append(z)

    for vec in newl:
        if vec in A:
            continue
        elif is_superfluous(newl,newl.index(vec)):
            return vec


def morph(S, B):
    '''
    Input:
        - S: a list of distinct Vecs
        - B: a list of linearly independent Vecs all in Span S
    Output: a list of pairs of vectors to inject and eject
    Example:
        >>> from vec import Vec
        >>> S = [Vec({'x', 'y'}, {'x': 1, 'y': 0}), Vec({'x', 'y'}, {'x': 0, 'y': 1})]
        >>> B = [Vec({'x', 'y'}, {'x': 2, 'y': 0}), Vec({'x', 'y'}, {'x': 0, 'y': 2})]
        >>> morph(S, B) == [(Vec({'x', 'y'}, {'x': 2, 'y': 0}), Vec({'x', 'y'}, {'x': 1, 'y': 0})), (Vec({'x', 'y'}, {'x': 0, 'y': 2}), Vec({'x', 'y'}, {'x': 0, 'y': 1}))]
        True
    '''

    morphlist = []

    for vec1, vec2 in zip(S, B):
        temp = vec2, vec1
        morphlist.append(temp)

    return morphlist




if __name__ == "__main__":
    import doctest
    doctest.testmod()

