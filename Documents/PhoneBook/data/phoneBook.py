from tkinter import *


def addPerson():
    name = enterName.get()
    tel = enterTelephone.get()
    if name == "" or tel == "":
        labelEditInformation.config(text="Fields are empty")
    else:
        contactsList.insert(END, name + " - " + tel)
        enterName.delete(0, END)
        enterTelephone.delete(0, END)
        labelEditInformation.config(text="")


def delelePerson():
    index = contactsList.curselection()[0]
    contactsList.delete(index)


def editPerson():
    index = contactsList.curselection()[0]
    name = enterName.get()
    telephoneNumber = enterTelephone.get()
    if name == "" or telephoneNumber == "":
        labelEditInformation.config(text="Fields are empty")
    else:
        contactsList.delete(index)
        contactsList.insert(index, name + " - " + telephoneNumber)
        enterName.delete(0, END)
        enterTelephone.delete(0, END)
        labelEditInformation.config(text="")


wn = Tk()
wn.title("Phone book")
wn.geometry("330x500")

topFrames = Frame(wn)
topFrames.pack()

labelName = Label(topFrames, text="Name")
labelName.grid(row=0, column=0)

enterName = Entry(topFrames)
enterName.grid(row=0, column=1)

labelTelephone = Label(topFrames, text="Telephone")
labelTelephone.grid(row=1, column=0)

enterTelephone = Entry(topFrames)
enterTelephone.grid(row=1, column=1)

functionsFrame = Frame(wn)
functionsFrame.pack()

addButton = Button(functionsFrame, text="Add contact", command=addPerson)
addButton.grid(row=0, column=0)

delButton = Button(functionsFrame, text="Delete contact", command=delelePerson)
delButton.grid(row=0, column=1)

editButton = Button(functionsFrame, text="Edit contact", command=editPerson)
editButton.grid(row=0, column=2)

belowFrame = Frame(wn)
belowFrame.pack()

scroll = Scrollbar(belowFrame)
scroll.pack(side=RIGHT)

contactsList = Listbox(belowFrame, yscrollcommand=scroll.set)
scroll.config(command=contactsList.yview)

contactsList.pack(side=LEFT)

labelEditInformation = Label(belowFrame, text="", fg="red")
labelEditInformation.pack()

contactsList.insert(END, "Natalia - 513-434-345", "Krzysztof - 908-456-435", "Andrzej - 895-654-909",
                    "Wojtek - 578-879-412",
                    "Magda - 984-323-423", "Karolina - 787-432-213", "Weronika - 432-908-234", "Lucyfer - 231-432-236",
                    "Zbyszek - 432-657-433",
                    "Patrycja - 321-657-875", "Mateusz - 984-476-456")
# wn.mainloop()
