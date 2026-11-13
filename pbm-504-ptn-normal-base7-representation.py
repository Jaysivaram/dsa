

def convertToBase7(num:int) -> str:

    isNegative = False
    out = ""
    if num == 0:
        return "0"

    if num < 0:
        isNegative = True
        num = -num

    while num > 0:
        quotiant = num % 7
        num = num // 7

        out += str(quotiant)


    out = out[::-1]

    return "-" + out if isNegative else out


print(convertToBase7(-7))
