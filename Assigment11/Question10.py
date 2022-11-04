'''10. Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)'''
n=int(input("Enter a number:-"))
s=''
while n:
    s=str(n%8)+s
    n=n//8

print(s)
print()

