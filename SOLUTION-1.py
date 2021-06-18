store = []
for number1 in range(999, 100, -1):
    for number2 in range(999, 100, -1):
        str_number = str(number1*number2)[::-1]

        if str_number == str(number1*number2):
            store.append(number1*number2)
        else:
            pass

store.sort()

print(store[len(store)-1])
