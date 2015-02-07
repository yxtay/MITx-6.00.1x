def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    len_min = min(len(s1), len(s2))
    
    s_out = ''
    for i in range(len_min):
        s_out += s1[i] + s2[i]
    
    s_out += s1[len_min:] + s2[len_min:]
    
    return s_out