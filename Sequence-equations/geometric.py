import math
print("Smaller index first if possible")
num1 = int(input("firstnum >> "))
ind1 = int(input("firstind >> "))
num2 = int(input("secondnum >> "))
ind2 = int(input("secondind >> "))


r = math.pow((num2/num1),1/(ind2-ind1))


if ind1 == 1:
    genesis_term_num = num1
else:
    genesis_term_num = num2 / ( (r) ** (ind2-1) )
print(f"r = {r}", f"first_term_val = {genesis_term_num}", sep="\n")
print(f"a\u2099={genesis_term_num}({r})\u207D\u207F\u207B\u00B9\u207E")