"""
    rotate:
        rotate("hello", 2) return "llohe"
        rotate("hello", 5) return "hello"
        rotate("hello", 6) return "elloh"
        rotate("hello", 7) return "llohe"
"""

def rotate(string,key):
    double_string = string + string # hellohello
    if key <= len(string):
        return double_string[key:len(string)+key]
    else:
        return double_string[key - len(string):key]
        
print(rotate("hello", 7))