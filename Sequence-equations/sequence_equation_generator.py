num1 = int(input("firstnum >> "))
ind1 = int(input("firstind >> "))
num2 = int(input("secondnum >> "))
ind2 = int(input("secondind >> "))


d = (num2-num1)/(ind2-ind1)

if ind1 == 1:
    genesis_term_num = num1
else:
    genesis_term_num = num2 + (d*(1-ind2))
print(f"d = {d}", f"first_term_val = {genesis_term_num}", sep="\n")
print(f"a\u2099={d}n+{genesis_term_num-d}")
