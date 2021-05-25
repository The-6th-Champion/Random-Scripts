print("Smaller index first if possible")

num1 = float(input("firstnum >> "))
ind1 = float(input("firstind >> "))
num2 = float(input("secondnum >> "))
ind2 = float(input("secondind >> "))

def arth_eq_calc(num1, ind1, num2, ind2):
    d = (num2-num1)/(ind2-ind1)

    if ind1 == 1:
        genesis_term_num = num1
    else:
        genesis_term_num = num2 + (d*(1-ind2))
    print(f"d = {d}", f"first_term_val = {genesis_term_num}", sep="\n")
    print(f"a\u2099={d}n+{genesis_term_num-d}")

arth_eq_calc(num1, ind1, num2, ind2)
