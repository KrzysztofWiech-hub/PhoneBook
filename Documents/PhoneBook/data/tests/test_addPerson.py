import unittest
import tkinter.constants
import data.phoneBook as phoneBook


class TestPhoneBook(unittest.TestCase):

    def test_checkEnterData(self):
        name = phoneBook.enterName = str("Jan")
        tel = phoneBook.enterTelephone = str("909-098-355")
        self.assertEqual(phoneBook.enterName, name)
        self.assertEqual(phoneBook.enterTelephone, tel)

    def test_checkInitialLastStateFromInitialList(self):
        name = phoneBook.enterName = str("Mateusz")
        tel = phoneBook.enterTelephone = str("984-476-456")
        phoneBook.contactsList.insert(tkinter.END, "Natalia - 513-434-345", "Krzysztof - 908-456-435", "Andrzej - 895-654-909",
                                      "Wojtek - 578-879-412",
                                      "Magda - 984-323-423", "Karolina - 787-432-213", "Weronika - 432-908-234", "Lucyfer - 231-432-236",
                                      "Zbyszek - 432-657-433",
                                      "Patrycja - 321-657-875", "Mateusz - 984-476-456")
        result = phoneBook.contactsList.get(tkinter.END)
        self.assertEqual(result, name + " - " + tel)



    def test_checkInsertPerson(self):
        name = phoneBook.enterName = str("Jan")
        tel = phoneBook.enterTelephone = str("909-098-355")
        phoneBook.contactsList.insert(tkinter.END, name + " - " + tel)
        result = phoneBook.contactsList.get(tkinter.END)
        self.assertEqual(result, name + " - " + tel)

    def test_checkDeleteInsertPerson(self):
        name = phoneBook.enterName = str("Jan")
        tel = phoneBook.enterTelephone = str("909-098-355")
        phoneBook.contactsList.insert(tkinter.END, name + " - " + tel)
        result = phoneBook.contactsList.get(tkinter.END)
        print(result)
        phoneBook.contactsList.delete(0, tkinter.END)
        result = phoneBook.contactsList.get(tkinter.END)
        print(result)
        self.assertEqual(result, "")

    def test_editPerson(self):
        name = phoneBook.enterName = str("Jan")
        tel = phoneBook.enterTelephone = str("909-098-355")
        phoneBook.contactsList.insert(tkinter.END, name + " - " + tel)
        phoneBook.contactsList.get(tkinter.END)

        phoneBook.contactsList.delete(0, tkinter.END)
        phoneBook.contactsList.get(tkinter.END)

        edit_name = "Andrzej"
        edit_telephone = "512-534-564"
        phoneBook.contactsList.insert(tkinter.END, edit_name + " - " + edit_telephone)
        result = phoneBook.contactsList.get(tkinter.END)

        self.assertEqual(result, edit_name + " - " + edit_telephone)
