"""
    search insert 
        [1,3,5,6] , 3  => 1  (index 3) 
        [1,3,5,6] , 2  => 2 (index 2 if be available)
        [1,3,5,6] , 7  => 4 (index 7 if be available)
        [1,3,5,6] , 0  => 0 (index 0 if be available)
        complexity : O(log n)
"""
def search_insert(arr,val):
    low = 0
    high = len(arr) - 1
    mid = high//2
    while low <= high:
        if val > arr[mid] :
            mid +=1
            low = mid

        else:
            mid -= 1
            high = mid
    return low

print(search_insert([1,3,5,6],7))