def are_isomorphic(input1, input2):
    if input1 is None or not input2 is None or len(input1) != len(input2):
        return False
        
    if len(input1) == 0:
        return True
        
    memo = {}
    seen = set()
    
    for i in range(len(input1)):
        a = input1[i]
        b = input2[i]
        
        if (a in memo and b != memo[a]) or (a not in memo and b in seen):
            return False

        memo[a] = b
        seen.add(b)

    return True
            
