"""
    search range :
        [5,7,7,8,8,8,10], 8 => [3,5]
        [5,7,7,8,8,8,10], 11 => [None, None]
"""
def search_range(nums,target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high-low) // 2 # why?
        # mid = (low + high) //2 
        if target > nums[mid]:
            low = mid +1
        elif target < nums[mid]:
            high = mid - 1
        else:
            break
    for i in range(len(nums)-1 ,-1, -1):
        if target == nums[i]:
            return [mid, i]
    return [None, None]

print(search_range([5,8,8,8,8,8,8,10],8 ))

# output : [3, 6]
# i think this is the right answer :
"""
    search range :
        [5,7,7,8,8,8,10], 8 => [3,5]
        [5,7,7,8,8,8,10], 11 => [None, None]
"""
def search_range(nums,target):
    low = 0
    high = len(nums) - 1
    while low < high:
        # mid = low + (high-low) // 2 # why?
        mid = (low + high) //2 
        if target > nums[mid]:
            low = mid +1
        else:
            high = mid 
        # else:
        #     break
    for i in range(len(nums)-1 ,-1, -1):
        if target == nums[i]:
            return [low, i]
    return [None, None]

print(search_range([5,7,7,8,8,8,10],8 ))

# output : [1, 6]