class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0:
            dividend = dividend * -1
            flagend = -1
        else: flagend = 1
        if divisor < 0:
            divisor = divisor * -1
            flagsor = -1
        else: flagsor = 1
        if divisor > dividend:
            return 0
        if divisor == dividend:
            return 1 * flagend * flagsor
        step = divisor
        total = dividend
        tempstep = divisor
        num = 0
        start = 0
        p = 1
        while(start + step <= total):
            if tempstep + tempstep + start > total:
                start = start + tempstep
                num = num + p
                tempstep = step
                p = 1
            else:
                tempstep = tempstep + tempstep
                p = p + p
        num = num * flagend * flagsor
        if num <= pow(2,31)-1 and num >= pow(-2,31):
            return num
        else:
            if num < 0:return pow(-2,31) 
            else: return pow(2,31)-1
a = Solution()
print(a.divide(217778,1))


