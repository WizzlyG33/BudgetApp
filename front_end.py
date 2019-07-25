#Imports
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk


#Set Window
window = Tk()
window.title('BudgetApp')
window.geometry('800x500')
window.resizable(width=False, height=False)

#Login

#Notebook
nb = ttk.Notebook(window, height=500, width=800)
nb.pack()
#nb.grid(row=1, column=0, rowspan=49, columnspan=50, sticky='NESW')

##################################################################
#                           Profile                              #
##################################################################

#Profile Page
profilePage = ttk.Frame(nb)
nb.add(profilePage, text='Profile')

#Profile Logout Button
logoutBtn = Button(profilePage, text='Logout')
logoutBtn.pack(pady=10, ipadx=7, padx=(720,0))

#Profile Image
profilePic = PhotoImage(file='user.png')
profileLabel = Label(profilePage, image=profilePic)
profileLabel.pack(pady=(100, 20))

#Profile Info Label Frame
infoLabelFrame = LabelFrame(profilePage, text='Info')
infoLabelFrame.pack()

#Profile Info Labels
nameLabel = Label(infoLabelFrame, text='Name:')
nameLabel.grid(row=0, column=0, sticky='W', padx=(5, 0))

passwordLabel = Label(infoLabelFrame, text='Password:')
passwordLabel.grid(row=1, column=0, sticky='W', padx=(5, 0))

salaryLabel = Label(infoLabelFrame, text='Salary:')
salaryLabel.grid(row=2, column=0, sticky='W', padx=(5, 0))

#Profile Info Entries
nameEntry = Entry(infoLabelFrame)
nameEntry.grid(row=0, column=1, padx=10, pady=3)

passwordEntry = Entry(infoLabelFrame)
passwordEntry.grid(row=1, column=1, pady=3)

salaryEntry = Entry(infoLabelFrame)
salaryEntry.grid(row=2, column=1, pady=(3, 10))

#Profile Info Edit Button
profileEditBtn = Button(infoLabelFrame, text='Edit')
profileEditBtn.grid(row=0, column=2, ipadx=7, padx=(5, 10))

##################################################################
#                           Transactions                         #
##################################################################

#Transactions Page
transactionsPage = ttk.Frame(nb)
nb.add(transactionsPage, text='Transactions')

#Transaction Listbox
transListbox = Listbox(transactionsPage)
transListbox.insert(1, "a")
transListbox.insert(1, "b")
transListbox.insert(1, "c")
transListbox.insert(1, "d")
transListbox.insert(1, "e")
transListbox.grid(row=0, column=0, padx=(15,0))

#-------------Middle Frame-------------#
transMidFrame = ttk.Frame(transactionsPage)
transMidFrame.grid(row=0, column=1)

#Add Transaction Button
transAddBtn = Button(transMidFrame, text='Add', width=10)
transAddBtn.pack(padx=(10, 450))

#Delete Transaction Button
transDelBtn = Button(transMidFrame, text='Delete', width=10)
transDelBtn.pack(padx=(10, 450), pady=(10,0))

#Edit Transaction Button
transModBtn = Button(transMidFrame, text='Edit', width=10)
transModBtn.pack(padx=(10, 450), pady=(10,65))

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
#                           Income                               #
##################################################################

#Income Page
incomePage = ttk.Frame(nb)
nb.add(incomePage, text='Income')

##################################################################
#                           Budget                               #
##################################################################

#Budget Page
budgetPage = ttk.Frame(nb)
nb.add(budgetPage, text='Budget')

##################################################################
#                           History                              #
##################################################################

#History Page
historyPage = ttk.Frame(nb)
nb.add(historyPage, text='History')

##################################################################
#                           Goals                                #
##################################################################

#Goals Page
goalsPage = ttk.Frame(nb)
nb.add(goalsPage, text='Goals')

##################################################################
#                           Suggestions                          #
##################################################################

#Suggestions Page
suggestionsPage = ttk.Frame(nb)
nb.add(suggestionsPage, text='Suggestions')

#Main Loop
window.mainloop()

#End Program
