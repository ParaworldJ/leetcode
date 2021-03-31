def romanToInt(s):
    num=0
    i=-1
    temp=s
    while(temp):
        if temp[i]=='V':
            if len(temp)>1:
                if temp[i-1]=='I':
                    num=num+4
                    temp=temp[: -2]
                else:
                    num=num+5
                    temp=temp[: -1]
            else:
                num=num+5
                temp=temp[: -1]
        elif temp[i]=='X':
            if len(temp)>1:
                if temp[i-1]=='I':
                    num=num+9
                    temp=temp[: -2]
                else:
                    num=num+10
                    temp=temp[: -1]
            else:
                num=num+10
                temp=temp[: -1]
        elif temp[i]=='L':
            if len(temp)>1:
                if temp[i-1]=='X':
                    num=num+40
                    temp=temp[: -2]
                else:
                    num=num+50
                    temp=temp[: -1]
            else:
                num=num+50
                temp=temp[: -1]
        elif temp[i]=='C':
            if len(temp)>1:
                if temp[i-1]=='X':
                    num=num+90
                    temp=temp[: -2]
                else:
                    num=num+100
                    temp=temp[: -1]
            else:
                num=num+100
                temp=temp[: -1]
        elif temp[i]=='D':
            if len(temp)>1:
                if temp[i-1]=='C':
                    num=num+400
                    temp=temp[: -2]
                else:
                    num=num+500
                    temp=temp[: -1]
            else:
                num=num+500
                temp=temp[: -1]
        elif temp[i]=='M':
            if len(temp)>1:
                if temp[i-1]=='C':
                    num=num+900
                    temp=temp[: -2]
                else:
                    num=num+1000
                    temp=temp[: -1]
            else:
                num=num+1000
                temp=temp[: -1]
        elif temp[i]=='I':
            num=num+1
            temp=temp[: -1]
    return num
print(romanToInt('MCMXCIV'))