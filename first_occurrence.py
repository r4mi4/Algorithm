"""
    first occurrence 
        [2,2,2,3,3,4,4,5,5,5] 4 => 5
"""

def first_occurrence(array, element):
    low, high = 0, len(array)-1
    while low < high:
        mid = (high+low)//2
        val = array[mid]
        # if low == high:
        #     break
        if val < element:
            low = mid+1
        else:
            high = mid
    if array[low] == element:
        return low
    
print(first_occurrence([5,8,8,8,8,8,8,10],8))


