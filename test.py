
def solution(s):
    startIndex = 0
    endIndex = 0
    count = 0
    max = 0
    w = 0 # walker
    
    while w < len(s):
        print("1", startIndex, endIndex, s[startIndex:endIndex+1])
        if s[w] in s[startIndex:endIndex+1]:
            startIndex += 1
        w += 1
        endIndex = w 
        count = len(s[startIndex:endIndex+1])
        if count > max:
            print("2", s[startIndex:endIndex+1])
            max = count
        
    return count

solution("nndfddf")