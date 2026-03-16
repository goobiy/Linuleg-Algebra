from mat import Mat
from vec import Vec
from orthogonalization import orthogonalize
import math


EPS = 1e-10


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
    return math.sqrt((sum(x**2 for x in v.f.values())))


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
    n = norm(v)
    if n < EPS:
        return Vec(v.D, {})
    return (1 / n) * v


def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list Lstar of len(L) orthonormal Vecs such that, for all i in range(len(L)),
            Span L[:i+1] == Span Lstar[:i+1]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> result = orthonormalize(L)
    >>> expected = [Vec(D, {'a': 0.73, 'b': 0.548, 'c': 0.183, 'd': 0.365}), Vec(D, {'a': 0.187, 'b': 0.403, 'c': -0.566, 'd': -0.695}), Vec(D, {'a': 0.528, 'b': -0.653, 'c': -0.512, 'd': 0.181})]
    >>> all(round(result[i] * expected[i], 3) == 1 for i in range(len(L)))
    True
    '''
    return [normalize(v) for v in orthogonalize(L)]


def inner_product(u, v):
    '''
    Input: Two Vecs u and v
    Output: The inner (dot) product of u and v

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> u = Vec(D, {'x': 3, 'y': 4})
    >>> v = Vec(D, {'x': 2, 'y': -1})
    >>> inner_product(u, v)
    2
    '''
    return u * v


def projection(u, v):
    '''
    Input: Two Vecs u and v
    Output: The projection of u onto v

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> u = Vec(D, {'x': 3, 'y': 4})
    >>> v = Vec(D, {'x': 1, 'y': 0})
    >>> projection(u, v) == Vec(D, {'x': 3.0, 'y': 0.0})
    True
    '''
    vec_norm = inner_product(v,v)

    if vec_norm < EPS:
        return Vec(u.D, {})
    return (inner_product(u,v) / vec_norm) * v


def is_orthogonal(u, v):
    '''
    Input: Two Vecs u and v
    Output: True if u and v are orthogonal (inner product is close to zero), otherwise False

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> u = Vec(D, {'x': 1, 'y': 2})
    >>> v = Vec(D, {'x': -2, 'y': 1})
    >>> is_orthogonal(u, v)
    True
    '''
    return abs(inner_product(u,v)) < EPS


def distance_to_subspace(L, u):
    '''
    Input: 
        - L: A list of Vecs forming a basis for a subspace
        - u: A Vec to compute the shortest distance to the subspace spanned by L
    Output: The shortest distance from u to the subspace spanned by L

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> L = [Vec(D, {'x': 1, 'y': 0})]
    >>> u = Vec(D, {'x': 3, 'y': 4})
    >>> round(distance_to_subspace(L, u), 6)
    4.0
    '''
    if not L:
        return norm(u)
    
    orth_basis = [v for v in orthogonalize(L) if norm(v) > EPS]
    onb = [normalize(v) for v in orth_basis]
    proj = Vec(u.D, {})


    for i in onb:
        proj = proj + inner_product(u,i) * i

    return norm(u - proj)


def is_orthonormal_basis(L):
    '''
    Input: A list L of Vecs
    Output: True if L forms an orthonormal basis (each vector has unit norm and all are mutually orthogonal), otherwise False

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> L = [Vec(D, {'x': 1, 'y': 0}), Vec(D, {'x': 0, 'y': 1})]
    >>> is_orthonormal_basis(L)
    True
    '''
    for i, u in enumerate(L):
        if abs(norm(u)- 1) > EPS:
            return False
        for j, v in enumerate(L):
            if i != j and not is_orthogonal(u,v):
                return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

