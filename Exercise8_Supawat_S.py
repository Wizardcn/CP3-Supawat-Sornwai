username = input("Username : ")
password = input("Password : ")
if username == "cat" and password == "555":
    print("-----Welcome to helloShop-----")
    print("รหัส รายการสินค้า     ราคา")
    print(" 1 ลูกอม        5 THB ")
    print(" 2 Chocolate 29 THB ")
    item = int(input("กรอกรหัสสินค้าที่ต้องการ(ex.1) : "))
    if item == 1:
        num = int(input("จำนวน : "))
        total = num * 5
        print("--------------------")
        print("Order :")
        print("ลูกอม จำนวน", num, "ชิ้น", "รวม", total, "THB")
        print("--------------------")
        print("Total : ", total, "THB")

    if item == 2:
        num = int(input("จำนวน : "))
        total = num * 29
        print("------------------------")
        print("Order")
        print("Choccolate จำนวน", num, "ชิ้น", "รวม", total, "THB")
        print("------------------------")
        print("Total : ", total, "THB")
else:
    print("Error !!!")