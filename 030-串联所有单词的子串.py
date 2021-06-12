#不在里面的，直接跳过到从下一个匹配的开始
#子串大部分符合，但有某个多了，那么快进到符合个数的坐标
#子串在表中，那么数量-1，记录到已存在表中
from collections import Counter
from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        step = len(words[0])
        FstHash = Counter(words) # Hash表
        total = len(s)
        i = 0 #检验的坐标
        k = {} #words有重复的时候的位置
        a = Counter(words) #每次检查的hash表
        start = i #检测的初始位置
        result = []
        #print(a)
        while(True):
            #print(s[i],a[s[i : i+step]],i)
            if start + len(words) * step > total:
                break
            if s[i : i+step] in FstHash:
                if FstHash[s[i : i+step]] > 1 and FstHash[s[i : i+step]] == a[s[i : i+step]]:
                    k[s[i : i+step]] = i + 1
                if s[i : i+step] in a:
                    a[s[i : i+step]] = a[s[i : i+step]] - 1
                    if a[s[i : i+step]] == 0:
                        del(a[s[i : i+step]])
                        if len(a) == 0:
                            result.append(start)
                            i = start + 1
                            start = i
                            a = Counter(words)
                            k = {}
                            continue
                    i = i + step
                else:
                    if s[i : i+step] in k:
                        i = k[s[i : i+step]]
                        start = i
                        a = Counter(words)
                        k = {}
                        continue
                    else:
                        i = start + 1
                        start = i
                        a = Counter(words)
                        k = {}
                        continue
            else:
                i = start + 1
                start = i
                a = Counter(words)
                k = {}
                continue
        return result



