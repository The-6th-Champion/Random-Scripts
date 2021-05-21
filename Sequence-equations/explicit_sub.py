import math

eq_type = input("What is the equation Type? (arithmetic or geometric)\n")
solve_for = input("Solve for what? (n or an)\n")
d = float(input("What is the rate of change?\n"))
initv = float(input("What is the initial value?\n"))

def n_calc(type1, d, initv, a):
    if type1:
        n = (a-(initv- d))/d
        return n
    elif not type1:
        n = math.log((a/initv))/math.log(d) +1 
        return n
    pass

def an_calc(type1, d, initv, n):
    if type1:
        a_n = d*n+(initv-d)
        return a_n
    elif not type1:
        a_n = initv * (d ** (n-1))
        return a_n
    pass



if eq_type == "arithmetic":
    if solve_for == "n":
        a = float(input("What is the value? (give a number) "))
        print(n_calc(True, d, initv, a))
    elif solve_for == "an":
        n = float(input("What is the index (n)? (give a number) "))
        print(an_calc(True, d, initv, n))
    else:
        print("fail")
elif eq_type == "geometric":
    if solve_for == "n":
        a = float(input("What is the value? (give a number) "))
        print(n_calc(False, d, initv, a))
    elif solve_for == "an":
        n = float(input("What is the index (n)? (give a number) "))
        print(an_calc(False, d, initv, n))
    else:
        print("fail")
