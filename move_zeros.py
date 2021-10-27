"""
    [False,2,0,4,7,0,1,'a'] => [False,2,4,7,1,'a',0,0]
"""

def move_zeros(seq):
    result = []
    zeros = 0
    for i in seq:
        if i == 0 and type(i) != bool :
            zeros +=1
        else:
            result.append(i)
    result.extend([0] * zeros)
    return result
    
print(move_zeros([False,2,0,4,7,0,1,'a']))