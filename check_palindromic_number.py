a = int (input("Enter a number for chek palidrom "))
b = a
rev = 0
while a>0:
    rev = rev * 10 + a % 10
    a = a // 10
if rev == b:
    print("its a palindromic numbers")
else:
    print("its not a palindromic number")