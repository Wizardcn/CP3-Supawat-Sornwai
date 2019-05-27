def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "1234":
        return True
    else :
        return False

def showMenu():
    print("----Welcome to iShop----")
    print("1.vat calculator")
    print("2.price calculator")
def menuSelect():
    userSelected = int(input(">> "))
    return userSelected
def vatCalculate(price):

    vat = price * 7 / 100
    result = price + vat
    return result
def priceCalculate():
    price1 = int(input("Price1(THB) : "))
    price2 = int(input("Price2(THB) : "))
    totalPrice = vatCalculate(price1 + price2)
    return totalPrice

if login() == True :
    showMenu()
    choose = menuSelect()
    if choose == 1:
        print("Price(+vat) : ", vatCalculate(int(input("Price(THB) : "))))
    elif choose == 2 :
        print("total price(+vat) : ", priceCalculate())
else : print("Error")


