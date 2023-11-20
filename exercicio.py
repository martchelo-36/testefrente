for i in range(1,101):
    x: str = ""
    if i % 5 == 0: x += "Fizz"
    if i % 3 == 0: x += "Buzz"
    
    print(x)
    # print(str(i) + ": " + str(x))