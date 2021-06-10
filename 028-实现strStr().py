class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if haystack == '':
            return -1
        if len(needle) > len(haystack):
            return -1
        hl = len(haystack)
        nl = len(needle)
        pos = -1
        for i in range(hl):
            if len(needle) > len(haystack[i :]):
                break
            if haystack[i] == needle[0]:
                k = i
                for j in range(nl):
                    if needle[j] == haystack[k]:
                        if j == nl - 1:
                            pos = i
                            break
                        k = k +1
                    else:
                        break
            else:
                continue
            if pos != -1:
                break
        return pos
         