import math

print("Smaller index first if possible")
num1 = float(input("firstnum >> "))
ind1 = int(input("firstind >> "))
num2 = float(input("secondnum >> "))
ind2 = int(input("secondind >> "))

def geo_qu_calc(num1, ind1, num2, ind2):
    sign = True
    negative = ""
    if abs(num2) != num2:
        sign = False
    print(sign)
    
    num3 = abs(num2)/num1  #-64/8 = -8
    power = (1.0/(ind2-ind1))
    r = math.pow(num3, power)   # -8 ** 1/3 = -2 arn-1 / arn-2
    print(r)

    if ind1 == 1:
        genesis_term_num = num1
    else:
        genesis_term_num = num2 / ( (r) ** (ind2-1) )
    print(f"r = {r}", f"first_term_val = {genesis_term_num}", sep="\n")
    print(f"a\u2099={genesis_term_num}({r})\u207D\u207F\u207B\u00B9\u207E")

geo_qu_calc(num1, ind1, num2, ind2)
