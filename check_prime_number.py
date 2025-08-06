n = int(input("Enter a number for check prime or not:> "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count = count + 1
if count==2:
    print('its a prime ')
else:
    print('its not a prime')