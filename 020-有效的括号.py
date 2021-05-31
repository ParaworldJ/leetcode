def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    a = []
    linein = ['{','(','[']
    for i in range(len(s)):
        if s[i] in linein:
            a.append(s[i])
        elif i > 0 and s[i] == '}':
            if len(a)>0 and a[len(a)-1] == '{':
                a.pop()
            else: return False
        elif i > 0 and s[i] == ')':
            if len(a)>0 and a[len(a)-1] == '(':
                a.pop()
            else: return False
        elif i > 0 and s[i] == ']':
            if len(a)>0 and a[len(a)-1] == '[':
                a.pop()
            else: return False
    else:
        if len(a) == 0:
            return True
        else:
            return False
print(isValid("()()}{"))