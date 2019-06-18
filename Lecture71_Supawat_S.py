def showBill():
    print("-----Thai Food-----")
    for i in range(len(menuList)):
        print(menuList[i], priceList[i], 'Baht')
        total = 0
        for x in range(len(priceList)):
            total += priceList[x]
    print('Total' , total, 'Baht')
    print('-------------------')




menuList = []
priceList = []
while True:
    menuName = input("Please Your Menu : ")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = int(input('Price : '))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
