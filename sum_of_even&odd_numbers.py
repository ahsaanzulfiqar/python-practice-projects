n = int(input("Ente a number that sum of all even and odd numbers: "))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even + i
    elif i%2!=0:
        odd = odd + i
print(f"The sum of even nmbers is {even} and the sum of odd numbers is {odd}")