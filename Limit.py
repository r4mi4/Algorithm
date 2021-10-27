"""
    [1,2,3,4,5]
        min 3 => [3,4,5]
        max 3 => [1,2,3]
        min ,max 3 => [3]

    complexity : O(n)
"""

def limit(arr,min= None,max=None):
    min_check = lambda val : True if min is None else (min <= val)
    max_check = lambda val : True if max is None else (max >= val)

    return [val for val in arr if min_check(val) and max_check(val)]

print(limit([1,2,3,4,5],1,4))