def find_max(x, y):
    temp = x / (x + y)
    k = round(temp)

    return k * x + (1 - k) * y


if __name__ == '__main__':
    x = int(input("first number: "))
    y = int(input("second number: "))

    max_number = find_max(x, y)

    print("max number is: " + str(max_number))

