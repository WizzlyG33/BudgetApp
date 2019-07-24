#Imports
from tkinter import *
from tkinter import ttk

#Set Window
window = Tk()
window.title('BudgetApp')
window.geometry('500x500')
window.resizable(width=False, height=False)

#Initialize Grid
rows = 0
while rows < 50:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows, weight=1)
    rows += 1

#Login

#Notebook
nb = ttk.Notebook(window)
nb.grid(row=1, column=0, rowspan=49, columnspan=50, sticky='NESW')

##################################################################
#                           Profile                              #
##################################################################

#Profile Page
profilePage = ttk.Frame(nb)
nb.add(profilePage, text='Profile')

#Profile Logout Button
logoutBtn = Button(profilePage, text='Logout')
logoutBtn.pack(pady=10, ipadx=7, padx=(440,10))

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
