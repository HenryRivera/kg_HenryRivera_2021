import sys


def mapping(s1, s2):
    vals = {}
    # Checking to see if lengths are the same
    if len(s1) != len(s2):
        return False
    # If lengths are the same
    for i in s1:
        if i not in vals:
            vals[i] = 1
        else:
            # If duplicates in s1 return False
            return False
    # End of loops, no duplicates found in s1, return True
    return True


def main(s1, s2):
    res = mapping(s1, s2)
    if res:
        print("true")
    else:
        print("false")


main(sys.argv[1], sys.argv[2])
