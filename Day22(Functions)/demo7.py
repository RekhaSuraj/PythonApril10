# Write a program to find factorial of a number using function

def fact_function(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
        # print(fact)
    print(fact)


fact_function(5)
# 120

fact_function(int(input('Enter the number to find factorial')))
# Enter the number to find factorial4
# 24

# Enter the number to find factorial6
# 720

# hw - write a program to find prime number using function