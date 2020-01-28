largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        num = int(num)
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
        elif largest is None:
            largest = num
        elif num > largest:
            largest = num
        else:
            pass
    except:
        print("Invalid input")
print("Maximum", largest)
print("Minimum", smallest)
