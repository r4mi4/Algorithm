"""
    zig zag iterator
        [1,3,5,7,9] [0,2,4,6,8] => 0,1,2,3,4,5,6,7,8,9
"""

class zigzag:
    def __init__(self,l1,l2):
        self.queue = [l1,l2]

    def next(self):
        v = self.queue.pop(0)
        t = v.pop(0)
        if v:
            self.queue.append(v)
        return t
        
    def has_queue(self):
        if self.queue:
            return True
        return False

z = zigzag([0,2,4,6,8],[1,3,5,7,9])
while z.has_queue():
    print(z.next(),end=' ')