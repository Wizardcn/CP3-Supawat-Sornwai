from tkinter import *
import math
def CalBMI(event):
    result = int(weightBox.get())/(int(heightBox.get())/100)**2
    if result >= 30:
        resultStatus.configure(text="อ้วนมาก")
    elif result >= 25 and result <= 29.9:
        resultStatus.configure(text="อ้วน")
    elif result >= 23 and result <= 24.9:
        resultStatus.configure(text="น้ำหนักเกิน")
    elif result >= 18.6 and result <= 22.9:
        resultStatus.configure(text="น้ำหนักปกติ เหมาะสม")
    elif result <= 18.5:
        resultStatus.configure(text="ผอมเกินไป")

    resultBMI.configure(text=result)

#Window
main = Tk()
main.geometry("320x140")
main.title("BMI Calculator")
#Label
heightLabel = Label(main, text="Height(cm.)", font=("Helvetica", 20))
heightLabel.grid(row=0, column=0)
weightLabel = Label(main, text="Weight(kg.)", font=("Helvetica", 20))
weightLabel.grid(row=1, column=0)
#TextBox
heightBox = Entry(main)
heightBox.grid(row=0, column=1)

weightBox = Entry(main)
weightBox.grid(row=1, column=1)
#Button
CalButton = Button(main, text="Calculate")
CalButton.bind("<Button-1>", CalBMI)
CalButton.grid(row=2, column=0)
#result
resultBMI = Label(main, text="result")
resultBMI.grid(row=3, column=0)
resultStatus = Label(main, text="")
resultStatus.grid(row=3, column=1)

main.mainloop()


