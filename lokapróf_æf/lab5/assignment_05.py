from lab4.mat import Mat
from lab3.vec import Vec
from math import cos, sin, radians


def is_almost_equal(A, B):
    '''
    Input:
      - A: a matrix or vector
      - B: a matrix or vector with same domain as A
    Output:
      - True if A and B are nearly equal, False otherwise

    The doctests and auto-grader on Gradescope uses this functionality to compare equality to prevent floating-point precision errors.
    '''
    assert A.D == B.D
    s = 0
    C = A - B
    for x in C.f.values():
        y = abs(x)
        s += y*y
    return s < 1e-5


def identity_matrix(D):
    '''
    Input:
      - D: a set representing the row and column domain of the matrix
    Output:
      - A square identity matrix with domain (D, D)
    Examples:
      >>> identity_matrix({0, 1}) == Mat(({0, 1}, {0, 1}), {(0, 0): 1, (1, 1): 1})
      True
      >>> identity_matrix({'x', 'y'}) == Mat(({'x', 'y'}, {'x', 'y'}), {('x', 'x'): 1, ('y', 'y'): 1})
      True
    '''
    new_dom = {}
    for k in D:
        new_dom[(k,k)] = 1
    return Mat((D,D), new_dom)


def are_inverses(A, B):
    '''
    Input:
      - A: a matrix
      - B: a matrix
    Output:
      - True if A and B are inverses, False otherwise
    Examples:
      >>> A = Mat(({0,1}, {0,1}), {(0,0): 1, (1,1): 1})
      >>> B = Mat(({0,1}, {0,1}), {(0,0): 1, (1,1): 1})
      >>> are_inverses(A, B)
      True

      >>> C = Mat(({0,1}, {0,1}), {(0,1): 1, (1,0): 1})
      >>> are_inverses(A, C)
      False
    '''
    assert A.D[0] == B.D[1] and A.D[1] == B.D[0]
    return is_almost_equal(A*B, identity_matrix(A.D[0])) and is_almost_equal(B*A, identity_matrix(A.D[1]))
        


def rotation_matrix_2d(D, deg):
    '''
    Input:
      - D: a set of two elements representing the row and column domain of the matrix
      - deg: the angle of rotation in degrees
    Output:
      - A 2x2 rotation matrix that rotates vectors by deg degrees
    NOTE:
      - Assume that the smaller element in D appears first in the row and column ordering. Sorting D may be helpful.
    Examples:
      >>> is_almost_equal(rotation_matrix_2d({0,1}, 90), Mat(({0, 1}, {0, 1}), {(0, 0): 0.0, (0, 1): -1.0, (1, 0): 1.0, (1, 1): 0.0}))
      True

      >>> is_almost_equal(rotation_matrix_2d({'x', 'y'}, 180), Mat(({'x', 'y'}, {'x', 'y'}), {('x', 'x'): -1.0, ('x', 'y'): -0.0, ('y', 'x'): 0.0, ('y', 'y'): -1.0}))
      True
    '''
    rad = radians(deg)
    d = sorted(D)
    new_dom = {}

    new_dom[(d[0],d[0])] = cos(rad)
    new_dom[(d[0],d[1])] = -sin(rad)
    new_dom[(d[1],d[0])] = sin(rad)
    new_dom[(d[1],d[1])] = cos(rad)

    return Mat((D,D), new_dom)


def rotate_2d(v, deg):
    '''
    Input:
      - v: a 2D column vector represented as a `Vec` object
      - deg: the angle of rotation in degrees
    Output:
      - A new vector representing v rotated by deg degrees
    Examples:
      >>> v = Vec({0, 1}, {0: 1, 1: 0})  # Vector (1,0)
      >>> is_almost_equal(rotate_2d(v, 90), Vec({0, 1}, {0: 0.0, 1: 1.0}))  # Rotated to (0,1)
      True

      >>> v = Vec({0, 1}, {0: 0, 1: 1})  # Vector (0,1)
      >>> is_almost_equal(rotate_2d(v, 90), Vec({0, 1}, {0: -1.0, 1: 0.0}))  # Rotated to (-1,0)
      True
    '''
    assert len(v.D) == 2
    pass



if __name__ == "__main__":
    import doctest
    doctest.testmod()
