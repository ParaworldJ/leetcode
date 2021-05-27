from itertools import product
def letterCombinations(digits):
    DtoNumList = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }
    use = []
    letter = []
    for i in range(len(digits)):
        if digits[i] == '1' or digits[i] == '0' and digits[i] in use:
            continue
        else:
            use = use + [digits[i]]
            letter = letter + [DtoNumList[digits[i]]]
    result = []
    for i in use:
        for k in product(*letter): ##还未理解 这里为什么要用* 号 解压？
            result = result + ["".join(k)]
    result = list(set(result))
    return result
print(letterCombinations('1121310'))