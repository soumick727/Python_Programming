## factorial number

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * factorial(n-1)


# Write a recursive function to calculate the sum of first n natural numbers.

def sum_natural(n):
    if n==1:
        return 1
    else:
        return n + sum_natural(n-1)


n = int(input("Enter the number for which you want sum : "))

print(sum_natural(n))