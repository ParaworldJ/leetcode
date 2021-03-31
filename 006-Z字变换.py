from collections import defaultdict
def convert(s, numRows):
    if numRows == 1:
        return s
    d=defaultdict(list)
    rows=numRows if len(s)> numRows else len(s)
    cycle=2*rows-2
    Zs=[]
    for i in range(len(s)):
        if i%cycle<rows:
            d[i%cycle].append(s[i])
        elif i%cycle>=rows:
            d[rows-1-(i%cycle-rows+1)].append(s[i])
    for i in range(rows):
        Zs = Zs + d[i]
    Zs=''.join(Zs)
    return Zs
s=convert("PAYPALISHIRING",4)
print(s) 