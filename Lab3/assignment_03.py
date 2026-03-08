from vec import Vec


def secret_function(u, v, w):
    """
    Input: u, v, w: Vec objects that have the same domain.

    Output: A Vec object based on the following logic:

        1. Adds the three vectors (u, v, w) together.
        2. Scales the added vector by the dot product of u and v.
        3. Uses conditions to adjust the final result:
            - If any two vectors from (u, v, w) are equal, returns the scaled vector 
            - Otherwise, returns the scaled vector negated

    NOTE:
        - Do not directly call methods like `equal()`, `add()`, `dot()`, `scalar_mul()`, or `neg()`.  
        - Instead, use the corresponding operators: `==`, `+`, `*`, and `-`.  

    Example:
        >>> D = {'a', 'b'}
        >>> u = Vec(D, {'a': 1, 'b': 2})
        >>> v = Vec(D, {'a': 3, 'b': 4})
        >>> w = Vec(D, {'a': 5, 'b': 6})
        >>> secret_function(u, v, w) == Vec(D, {'a': -99, 'b': -132})
        True

    Example Explanation:
        1. The sum of the three vectors is Vec(D, {'a': 9, 'b': 12}).
        2. The dot product of u and v is 11, so the added vector scaled is Vec(D, {'a': 99, 'b': 132}).
        3. Since none of the input vectors are equal, the final result is the negated scaled vector: Vec(D, {'a': -99, 'b': -132}).
    """

    summed_vec = u + v + w

    dot_product = u * v

    scaled_vec = dot_product * summed_vec

    if (u == v) or (u == w) or (v == w):
        return scaled_vec
    
    return -scaled_vec


if __name__ == "__main__":
    import doctest
    doctest.testmod()
