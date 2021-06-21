number = 700851475140
i = 2

while i<= number:
    if number % i == 0:
        number = number / i
    else:
        i += 1

print(i)
