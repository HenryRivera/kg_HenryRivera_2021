def mapping(s1, s2):
    vals = {}
    # Checking to see if lengths are the same
    if len(s1) != len(s2):
        print("false")
        return
    # Lengths the same
    for i in s1:
        if i not in vals:
            vals[i] = 1
        else:
            # If duplicates in s1 return False
            print("false")
            return
    # End of loops, no duplicates in s1, return True
    print("true")