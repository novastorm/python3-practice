def match(first, second):
    if not first and not second:
        return True

    if not first or not second:
        return False

    si = len(second) - 1
    fi = len(first) - 1
    m = None
    
    # start at end and work way forward.
    while fi >= 0 and si >= 0:
        print("{}, {}, {}".format(second[si], first[fi], first[fi - 1] if fi - 1 > 0 else None))
        if first[fi] == second[si] or first[fi] == '?' and si >= 0:
            fi -= 1
            si -= 1
        elif first[fi] == '*' and fi >=0 and first[fi - 1] != second[si]:
            if not m:
                m = fi
            si -= 1
        elif first[fi] == '*' and fi >=0 and first[fi - 1] == second[si]:
            fi -= 2
            si -= 1
        elif m:
            fi = m
            m = None
        else:
            return False

        if fi < 0 and si >= 0:
            fi = m

    print("fi: {}, si: {}".format(fi, si))
    return fi <= 0 and si <= 0


F = 'first'
S = 'second'
E = 'expected'

tests = [
    {
        F: "fi*de",
        S: "firecode",
        E: True  
    },
    {
        F: "fi?de",
        S: "firecode",
        E: False
    },
    {
        F: "fi*de",
        S: "fifirecode",
        E: True  
    },
    {
        F: "fi????de",
        S: "firecode",
        E: True  
    },
]

for t in tests:
    print(match(t[F], t[S]) == t[E])