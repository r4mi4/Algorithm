"""
    bead sort
        [4,7,2,9,3,6,7] => [2,3,4,6,7,7,9]
"""

def bead_sort(sequence):
    if any(not isinstance(x,int) or x<0 for x in sequence):
        raise TypeError('sequence must be list of non-negative integers')
    for _ in range(len(sequence)):
        print(sequence)
        print(list(enumerate(zip(sequence,sequence[1:]))))
        for i,(rod_upper,rod_lower) in enumerate(zip(sequence,sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper-rod_lower
                # 7 -=7-2 =>2
                # 2 += 7-2 =>7
                sequence[i+1] += rod_upper - rod_lower
    return sequence

print(bead_sort([4,7,2,9,3,6,7]))