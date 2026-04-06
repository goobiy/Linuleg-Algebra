from echelon import transformation
from matutil import mat2rowdict
from vec import Vec


def nullspace(A, eps=1e-15):

    M = transformation(A)
    U = M * A
    rowlist = list(mat2rowdict(U).values())
    col_labels = sorted(A.D[1], key=repr)

    pivot_cols = []
    for row in rowlist:
        for col in col_labels:
            if abs(row[col]) > eps:
                pivot_cols.append(col)
                break

    free_cols = [col for col in col_labels if col not in pivot_cols]
    null_basis = []

    for free_col in free_cols:
        v = Vec(set(col_labels), {free_col: 1})
        for row in reversed(rowlist):
            for col in pivot_cols:
                if abs(row[col]) > eps:
                    v[col] = -row * v / row[col]
                    break
        null_basis.append(v)

    return null_basis

    