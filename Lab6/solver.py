from mat import Mat
from vec import Vec
from matutil import *


def _triangular_solve(rowlist, row_label_list, col_label_list, b):
    x = Vec(set(col_label_list), { })
    cind = len(col_label_list) - 1
    rind = len(row_label_list) - 1
    while rind >= 0:
        r = row_label_list[rind]
        row = rowlist[r]
        cind = 0
        while cind < len(col_label_list):
            c = col_label_list[cind]
            if row[c] == 0:
                cind += 1
            else:
                break
        if cind >= len(col_label_list):
            rind -= 1
            continue
        if cind > 0 and row[col_label_list[cind-1]] != 0:
            cind -= 1
        x[c] = (b[r] - x * row) / row[c]
        rind -= 1
        cind -= 1
            
    return x

def _list2dict(L, keylist):
    return dict(zip(keylist, L))


def _solve(A, b, eps = (1e-15,)):
    col_label_list = sorted(A.D[1], key=repr)
    row_label_list = sorted(A.D[0], key=repr)
    M = Mat(A.D, A.f.copy()) # copy
    rhs = Vec(b.D, b.f.copy())
    
    remaining_rows = set(row_label_list.copy())
    new_row_order = []

    upper_bound = min(len(col_label_list), len(row_label_list))
    for i in range(upper_bound):
        # Gauss transformation per column
        c = col_label_list[i]
        r1 = max(remaining_rows, key=lambda x: abs(M[(x,c)]))

        if M[r1, c] == 0:
            continue
        new_row_order.append(r1)
        remaining_rows.remove(r1)
        T = Mat((set(row_label_list), set(row_label_list)), {(rr,rr): 1 for rr in row_label_list})
        for r2 in remaining_rows:
            T[(r2,r1)] = -(M[(r2,c)] / M[(r1,c)])
        M = T*M
        rhs = T*rhs
    row_label_list = new_row_order + list(remaining_rows)
    x = _triangular_solve(mat2rowdict(M), row_label_list, col_label_list, rhs)
    x.D = A.D[1]
    return x

def solve(A, b, eps = 1e-15):
    """Solve the matrix-vector equation Ax = b.
    
    If a solution to Ax = b does not exist, then the vector returned by
    solve(A, b) is not a solution.  Please verify that Ax = b.
    
    Args:
        A: A matrix of type Mat.
        b: A vector of type Vec.
        eps: A threshold.  Optional.
    
    Returns:
        x: A vector of type Vec.
    
    Raises:
        AssertionError: An error occurs when A is not a matrix of type Mat.
        AssertionError: An error occurs when b is not a vector of type Vec.
        AssertionError: An error occurs when A.D[0] != b.D.
    
    Example 1: Solve Ax = b and verify that x is close to b.
    >>> A = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 2, (2, 0): 10, (1, 0): 3, (0, 0): 1, (1, 1): 4})
    >>> b = Vec({0, 1, 2},{0: 1, 1: 5, 2: 30})
    >>> A.D[0] == b.D
    True
    >>> x = solve(A, b)
    >>> A.D[1] == x.D
    True
    >>> (b-A*x).is_almost_zero()
    True
    
    Example 2: Solve Ax = b and see that x is not a valid solution.
    >>> A = Mat(({0, 1}, {0, 1}), {(1, 1): 1})
    >>> b = Vec({0, 1},{0: 2, 1: 3})
    >>> A.D[0] == b.D
    True
    >>> x = solve(A, b)
    >>> A.D[1] == x.D
    True
    >>> (b-A*x).is_almost_zero()
    False

    Example 3: Solve when A and b are over GF(2).
    >>> from GF2 import one
    >>> A = Mat(({'a','b'},{'A','B'}), {('a','A'):one, ('a','B'):one, ('b','B'):one})
    >>> b = Vec({'a','b'}, {'a':one})
    >>> x = solve(A, b)
    >>> A*x==b
    True
    >>> (b-A*x).is_almost_zero()
    True

    """
    if not isinstance(A, Mat):
        raise AssertionError
    if not isinstance(b, Vec):
        raise AssertionError
    if not A.D[0] == b.D:
        raise AssertionError
    solve.__calls__ += 1
    A = Mat(A.D, A.f)
    b = Vec(b.D, b.f)
    try:
        return _solve(A, b, eps)
    except ZeroDivisionError as e:
        return Vec(A.D[1], { })

solve.__calls__ = 0
solve.__version__ = 'instrumented'
