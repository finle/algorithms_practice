def firstNotRepeatingCharacter(s):
    for i in s:
        if s.find(i) == s.rfind(i):
            return i
    return '_'