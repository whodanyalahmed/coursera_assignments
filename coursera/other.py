def computepay(h , rate):
    if (h > 40):
        result = h * rate
        sec = (h - 40)*(rate*0.5)
        fin = sec + result
        return fin
    else:
        result = h * rate
        return result

hrs = input("Enter Hours:")
h = float(hrs)

rate = float(input("Enter rate: "))

print(computepay(h,rate))