
## 1: (Problem 1.7.3) Python Comprehensions: Function Composition
def my_function_composition(f, g):
    '''
    Input:
    -f: a function represented as a dictionary such that g of f exists
    -g: a function represented as a dictionary such that g of f exists
    Output:
    -a dictionary that represents a function g of f
    Examples:
    >>> f = {0:'a',1:'b'}
    >>> g = {'a':'apple','b':'banana'}
    >>> my_function_composition(f,g) == {0:'apple',1:'banana'}
    True
    >>> a = {'x':24,'y':25}
    >>> b = {24:'twentyfour',25:'twentyfive'}
    >>> my_function_composition(a,b) == {'x':'twentyfour','y':'twentyfive'}
    True
    '''
    return {key: g[val] for key, val in f.items()}

## 2: Image of a function
def image(f, D):
    '''
    Input:
    -f: a function represented as a dictionary
    -D: a set representing the domain of f
    Output:
    -the image of f as a set
    Examples:
    >>> f = {0: 3, 1: 4, 2: 5}
    >>> D = {0, 1}
    >>> image(f, D)
    {3, 4}
    >>> f = {3: 10, 4: 20}
    >>> D = {3, 4}
    >>> image(f, D)
    {10, 20}
    '''
    return {val for key, val in f.items() if key in D}

## 3: Image cardinality of a function
def image_cardinality(f, D):
    '''
    Input:
    -f: a function represented as a dictionary
    -D: a set representing the domain of f
    Output:
    -an integer that represents the cardinality of the image of f
    Examples:
    >>> f = {0: 3, 1: 4, 2: 5}
    >>> D = {0, 1}
    >>> image_cardinality(f, D)
    2
    >>> f = {3: 10, 4: 20, 5: 10}
    >>> D = {3, 4, 5}
    >>> image_cardinality(f, D)
    2
    '''
    return len(image(f, D))


## 4: One-to-one functions
def is_one_to_one(f, D):
    '''
    Input:
    -f: a function represented as a dictionary
    -D: a set representing the domain of f
    Output:
    -a boolean representing whether the function f is one-to-one
    Examples:
    >>> f = {0: 'a', 1: 'b', 2: 'c'}
    >>> D = {0, 1, 2}
    >>> is_one_to_one(f, D)
    True
    >>> f = {0: 'a', 1: 'a', 2: 'b'}
    >>> D = {0, 1, 2}
    >>> is_one_to_one(f, D)
    False
    '''
    check = []

    for key, val in f.items():
        if val in check:
            return False
        check.append(val)
    return True

## 5: Onto functions
def is_onto(f, D, C):
    '''
    Input:
    -f: a function represented as a dictionary
    -D: a set representing the domain of f
    -C: a set representing the co-domain of f
    Output:
    -a boolean representing whether the function f is onto
    Examples:
    >>> f = {0: 'a', 1: 'b', 2: 'c'}
    >>> D = {0, 1, 2}
    >>> C = {'a', 'b', 'c'}
    >>> is_onto(f, D, C)
    True
    >>> f = {0: 'a', 1: 'b'}
    >>> D = {0, 1}
    >>> C = {'a', 'b', 'c'}
    >>> is_onto(f, D, C)
    False
    '''
    return {f[x] for x in D if x in f} == C


## 6: Invertible functions
def is_invertible(f, D, C):
    '''
    Input:
    -f: a function represented as a dictionary
    -D: a set representing the domain of f
    -C: a set representing the co-domain of f
    Output:
    -a boolean representing whether the function f is invertible
    Examples:
    >>> f = {0: 'a', 1: 'b', 2: 'c'}
    >>> D = {0, 1, 2}
    >>> C = {'a', 'b', 'c'}
    >>> is_invertible(f, D, C)
    True
    >>> f = {0: 'a', 1: 'a', 2: 'b'}
    >>> D = {0, 1, 2}
    >>> C = {'a', 'b', 'c'}
    >>> is_invertible(f, D, C)
    False
    '''
    return is_one_to_one(f,D) and is_onto(f,D,C)


## 7: Caesar Cipher Encoder
def encode(s):
    '''
    Input:
    -s: a string consisting only of capitalized letters from the english alphabet
    Output:
    -a string representing the Caesar cipher encoded version of the original
    string s, shifted by 3 places
    Examples:
    >>> encode("MATRIX")
    'PDWULA'
    >>> encode("XYZ")
    'ABC'
    '''
    result = []

    for char in s:
        shifted = (ord(char) - ord("A") + 3) % 26
        result.append((chr(shifted + ord("A"))))
    return "".join(result)

## 8: Caesar Cipher Decoder
def decode(s):
    '''
    Input:
    -s: a string consisting only of capitalized letters from the english alphabet
    Output:
    -a string representing the Caesar cipher decoded version of the original
    string s, shifted by 3 places
    Examples:
    >>> decode("PDWULA")
    'MATRIX'
    >>> decode("ABC")
    'XYZ'
    '''
    result = []

    for char in s:
        shifted = (ord(char) - ord("A") - 3) % 26
        result.append((chr(shifted + ord("A"))))
    return "".join(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
