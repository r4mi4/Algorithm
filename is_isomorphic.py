"""
    is isomprphic
        foo, bar => False
        foo, bee => True
        
        paper, title => True
"""

def is_isomorphic(s,t):
    dict = {}
    set_value = set()
    if len(s) != len(t) :
        return False
    for i in range(len(s)):
        print(set_value,dict)
        if s[i] not in dict:
            if t[i] in set_value:
                return False
            dict[s[i]] = t[i]
            set_value.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False
    return True
print(is_isomorphic('fow','bee'))