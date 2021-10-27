"""
    binary search :
        [2,3,4,6,12,19,20,21] 12 => index 4 in list
"""

def binary_search(array, element):
    low, high = 0, len(array)-1

    while low <= high:
        mid = (high + low)//2
        val = array[mid]
        if val == element:
            return mid
        elif val < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print(binary_search([5,8,8,8,8,8,8,10],8))
# output : 3

#True ?
# """
#     binary search :
#         [2,3,4,6,12,19,20,21] 12 => index 4 in list
# """

# def binary_search(array, element):
#     low, high = 0, len(array)-1

#     while low < high:
#         mid = (high + low)//2
#         val = array[mid]
#         if val < element:
#             low = mid + 1
#         else:
#             high = mid
#     if low :
#         return low
#     return -1

# print(binary_search([5,8,8,8,8,8,8,10],5))