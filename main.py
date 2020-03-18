def mapping(s1, s2):
    vals = {}
    if len(s1) != len(s2):
        print("false")
        return
    for i in s1:
        if i not in vals:
            vals[i] = 1
        else:
            print("false")
            return
    print("true")


mapping("for", "foo")