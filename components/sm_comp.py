#Imports
from tkinter import *
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk

#Window
window = Tk()
window.title('Small Component')
window.geometry('800x500')
window.resizable(width=False, height=False)

##################################################################
#                             CODE                               #
##################################################################

#Transactrions Page
transactionsPage = ttk.Frame(window)
#nb.add(transactionsPage, text='Transactions')
transactionsPage.pack()

#Transaction Listbox
transListbox = Listbox(transactionsPage)
transListbox.insert(1, "a")
transListbox.insert(1, "b")
transListbox.insert(1, "c")
transListbox.insert(1, "d")
transListbox.insert(1, "e")
transListbox.grid(row=0, column=0)

#-------------Middle Frame-------------#
transMidFrame = ttk.Frame(transactionsPage)
transMidFrame.grid(row=0, column=1)

#Add Transaction Button
transAddBtn = Button(transMidFrame, text='Add', width=5)
transAddBtn.pack(padx=(10, 490))

#Delete Transaction Button
transDelBtn = Button(transMidFrame, text='Delete', width=5)
transDelBtn.pack(padx=(10, 490), pady=(10,0))

#Edit Transaction Button
transModBtn = Button(transMidFrame, text='Edit', width=5)
transModBtn.pack(padx=(10, 490), pady=(10,65))

#-------------Right Frame-------------#
transRightFrame = ttk.Frame(transactionsPage)
transRightFrame.grid(row=0, column=2)

#Category 1 Label
cat1Label = Label(transRightFrame, text='Category 1')
cat1Label.pack(pady=(30,0))

#Category 1 Progress Bar
cat1ProgBar = Progressbar(transRightFrame, orient=HORIZONTAL, length=100, mode='determinate')
cat1ProgBar.pack()

#Category 2 Label
cat2Label = Label(transRightFrame, text='Category 2')
cat2Label.pack()

#Category 2 Progress Bar
cat2ProgBar = Progressbar(transRightFrame, orient=HORIZONTAL, length=100, mode='determinate')
cat2ProgBar.pack()

#Category 3 Label
cat3Label = Label(transRightFrame, text='Category 3')
cat3Label.pack()

#Category 3 Progress Bar
cat3ProgBar = Progressbar(transRightFrame, orient=HORIZONTAL, length=100, mode='determinate')
cat3ProgBar.pack()

#Category 4 Label
cat4Label = Label(transRightFrame, text='Category 4')
cat4Label.pack()

#Category 4 Progress Bar
cat4ProgBar = Progressbar(transRightFrame, orient=HORIZONTAL, length=100, mode='determinate')
cat4ProgBar.pack()

#Category 5 Label
cat5Label = Label(transRightFrame, text='Category 5')
cat5Label.pack()

#Category 5 Progress Bar
cat5ProgBar = Progressbar(transRightFrame, orient=HORIZONTAL, length=100, mode='determinate')
cat5ProgBar.pack()

##################################################################
#                           END CODE                             #
##################################################################

#Main Loop
window.mainloop()
