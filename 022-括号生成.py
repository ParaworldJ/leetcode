from collections import Counter
def generateParenthesis(n: int) -> list:
    b = ''
    a = []
    if n == 0: return []
    j = 2 * n
    left(j - 1 , b + '(',a ,n)
    return a
def right(n:int,b:str,a:list,T:int):
    # print(n,b,a)
    if n == 1:
        if Counter(b)['('] > T or Counter(b)['('] < Counter(b)[')']:
            return None
        else: 
            a.append(b+')')
    else:
        if Counter(b)['('] >= Counter(b)[')']:
            left(n - 1, b + '(', a,T)
            right(n - 1, b + ')', a,T)
        else:
            return None
def left(n:int,b:str,a:list,T:int):
    # print(n,b,a)
    if n == 1:
        if Counter(b)['('] > T or Counter(b)['('] < Counter(b)[')']:
            return None
        else: 
            a.append(b+')') 
    else:
        if Counter(b)['('] >= Counter(b)[')']:
            left(n - 1, b + '(', a,T)
            right(n - 1, b + ')', a,T)
        else:
            return None
print(generateParenthesis(1))
