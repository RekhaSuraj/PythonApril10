# Factorial of a number

def fact_fun(num): #Function Definitiom
    if num < 1: # Exit condition
        return 1

    else:
        return num * fact_fun(num-1)  # Recursive case

print(fact_fun(5))

# =5*fact_fun(4)
# =5*4*fact_fun(3)
# =5*4*3*fact_fun(2)
# =5*4*3*2*fact_fun(1)
# =5*4*3*2*1*fact_fun(0)
# =5*4*3*2*1*1
# =120


# hw - Adding numbers upto n using recursion

