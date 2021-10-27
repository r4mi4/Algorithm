"""
    remove min value in list:
        [5,3,1,7,-2,6,8,2] => -2 
        new list => [5,3,1,7,6,8,2]
"""
def remove_min(stack):
    storage_stack = []
    if len(stack) == 0 :
        return stack
    min = stack.pop()
    stack.append(min)
    for _ in range(len(stack)):
        val = stack.pop()
        if val <= min:
            min = val
        storage_stack.append(val)
    # we can use follow method but we didnt :| ?
    # storage_stack.remove(min)
    # storage_stack.reverse()
    # return storage_stack,min
    for i in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != min :
            stack.append(val)
    return stack,min

print(remove_min([5,3,1,7,-2,6,8,2]))
