'''
    a1z26
        'amir' <=> [1,13,9,18]
    
'''
def encode(plain):
    return [ord(elm) for elm in plain]

def decode(encode):
    return "".join(chr(elm) for elm in encode)