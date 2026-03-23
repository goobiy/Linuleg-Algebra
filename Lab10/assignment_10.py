from mat import Mat
from vec import Vec
from orthogonalization import aug_orthogonalize, orthogonalize, aug_project_orthogonal
from matutil import coldict2mat, mat2coldict, mat2rowdict
from triangular import triangular_solve


def norm(v):
    '''
    Input: A Vec v
    Output: The Euclidean norm (magnitude) of v

    >>> from vec import Vec
    >>> D = {'a', 'b', 'c'}
    >>> v = Vec(D, {'a': 3, 'b': 4, 'c': 0})
    >>> round(norm(v), 6)
    5.0
    '''
    return (v*v)**0.5


def normalize(v):
    '''
    Input: A Vec v
    Output: A unit vector in the same direction as v, or the zero vector if v is zero

    >>> from vec import Vec
    >>> D = {'a', 'b', 'c'}
    >>> v = Vec(D, {'a': 1, 'b': 2, 'c': 2})
    >>> normalize(v) == Vec(D, {'a': 1/3, 'b': 2/3, 'c': 2/3})
    True
    '''
    return 1.0 / norm(v) * v if norm(v) > 0 else 0*v


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist of lists such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
            
    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> Qlist, Rlist = aug_orthonormalize(L)
    >>> from matutil import coldict2mat, mat2coldict
    >>> all(v.is_almost_zero() for v in mat2coldict(coldict2mat(Qlist) * coldict2mat(Rlist) - coldict2mat(L)).values())
    True
    '''
    Q_list = []
    R_list = []

    for i, vec in enumerate(L):
        vstar, sigmadict = aug_project_orthogonal(vec, Q_list)

        normed_vstar = norm(vstar)

        sigmadict[len(Q_list)] = normed_vstar

        Q_list.append(normalize(vstar))

        new_vec = Vec(set(range(len(L))), sigmadict)
        R_list.append(new_vec)
    
    return Q_list, R_list



def QR_factor(A):
    '''
    Input:
        - A: a Mat object representing a matrix with linearly independent columns.

    Output:
        - Q: a Mat object where columns form an orthonormal basis for the column space of A.
        - R: a Mat object representing an upper-triangular matrix encoding the transformation from 
             the original basis to the orthonormal basis.

    Example:
    >>> from matutil import mat2coldict
    >>> from mat import Mat
    >>> domain = ({'a', 'b', 'c'}, {'A', 'B'})
    >>> A = Mat(domain, {('a','A'):-1, ('a','B'):2, ('b','A'):5, ('b','B'):3, ('c','A'):1, ('c','B'):-2})
    >>> Q, R = QR_factor(A)
    >>> all(v.is_almost_zero() for v in mat2coldict(Q * R - A).values())
    True
    '''
    col_dict = mat2coldict(A)


    Q_list, R_list = aug_orthonormalize(list(col_dict.values()))

    keys = list(col_dict.keys())
    intkeys = list(range(len(Q_list)))
    Q_mat = coldict2mat(dict(zip(intkeys,Q_list)))
    R_mat = coldict2mat(dict(zip(keys,R_list)))

    return Q_mat, R_mat



def QR_solve(A, b):
    '''
    Input:
        - A: a Mat with linearly independent columns
        - b: a Vec whose domain equals the set of row-labels of A
    Output:
        - vector x that minimizes norm(b - A*x)
    Note: This procedure uses the procedure QR_factor.
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR_factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result.is_almost_zero()
        True
    '''
    Q_mat, R_mat = QR_factor(A)

    Q_inverse_mult_b = Q_mat.transpose() * b

    R_row_dict = mat2rowdict(R_mat)

    row_list = [R_row_dict[i] for i in range(len(R_row_dict))]

    label_list = list(R_mat.D[1])

    x = triangular_solve(row_list, label_list, Q_inverse_mult_b)

    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()