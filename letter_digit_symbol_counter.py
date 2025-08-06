a = "cabfh489#$%^&*()afcjx239r8"
char = 0
digit = 0
symbol = 0
for i in a:
    if i.isdigit():
        digit = digit + 1
    elif i.isalpha():
        char = char + 1
    else:
        symbol = symbol + 1
print(f"The digits are {digit}\nThe charachters are {char}\nThe symbols are {symbol}")