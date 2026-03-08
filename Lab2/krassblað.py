


## 1: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    return sum(x*y for x,y in zip(voting_dict[sen_a],voting_dict[sen_b]))





## 3: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
        >>> vd == {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        True
        >>> vd = {'a': [-1,0,0], 'b': [1,0,0], 'c': [-1,1,0], 'd': [-1,1,1]}
        >>> least_similar('c', vd)
        'b'
    """
    dot_least_similar = {}

    for name in voting_dict:
        if name == sen:
            continue
        dot_least_similar[policy_compare(sen,name, voting_dict)] = name

    return dot_least_similar[min(dot_least_similar.keys())]



## 6: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein')
        True
    """
    names = list(voting_dict.keys())

    best_pair = None
    best_score = None

    for i in range(len(names)):
        for j in range(i+1, len(names)):
            sen_a = names[i]
            sen_b = names[j]
            score = policy_compare(sen_a,sen_b, voting_dict)
    
    if best_score is None or score < best_score:
        best_score = score
        best_pair = (sen_a,sen_b)
    
    return best_pair


voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}


print(bitter_rivals(voting_dict))