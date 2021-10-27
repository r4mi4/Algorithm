"""
    For Example : top_1([1,1,2,2,3,4,5]) will returne [1,2]
    
    complexity : O(n)
"""

def top_1(arr):
    values = {}
    # revese each value which first apears on keys
    # revese how many time each value apears by index number on value
    result = []
    f_val = 0
    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1
    f_val = max(values.values())
    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue
    return result

# print(top_1([1,1,2,2,3,4,5]))