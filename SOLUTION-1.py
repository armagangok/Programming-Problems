store = []

for number1 in range(999, 100, -1):
    for number2 in range(999, 100, -1):
        number = number1*number2
        str_number = str(number)[::-1]
        if str_number == str(number):
            store.append(number1)
        else:
            pass

store.sort()
print(store[len(store)-1])
