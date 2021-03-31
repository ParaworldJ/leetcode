import math
def intToRoman(num):#-> str#
    a=[[0,0,0,0],[0,0,1,0],[0,0,2,0],[0,0,3,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,1,2,0],[0,1,3,0],[1,0,0,1]]
    c=[['','','M',''],['C','D','C','M'],['X','L','X','C'],['I','V','I','X']]
    q=math.floor(num/1000)
    Romanstring=a[q][2]*c[0][2]
    qb=num-q*1000
    b=math.floor(qb/100)
    Romanstring=Romanstring+a[b][0]*c[1][0]+a[b][1]*c[1][1]+a[b][2]*c[1][2]+a[b][3]*c[1][3]
    bs=qb-b*100
    s=math.floor(bs/10)
    Romanstring=Romanstring+a[s][0]*c[2][0]+a[s][1]*c[2][1]+a[s][2]*c[2][2]+a[s][3]*c[2][3]
    g=bs-s*10
    Romanstring=Romanstring+a[g][0]*c[3][0]+a[g][1]*c[3][1]+a[g][2]*c[3][2]+a[g][3]*c[3][3]
    return Romanstring
print(intToRoman(255))