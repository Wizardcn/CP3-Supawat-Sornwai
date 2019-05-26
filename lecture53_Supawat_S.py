def vatCalculate(totalPrice):
    totalPrice = int(input("Price : "))
    result = totalPrice * 1.07
    return result
print(vatCalculate(0))
