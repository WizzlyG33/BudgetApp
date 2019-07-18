#Imports
from tkinter import *

#Window
window = Tk()
window.title('Medium Component')
window.geometry('500x500')

##################################################################
#                             CODE                               #
##################################################################

#Profile Logout Button
logoutBtn = Button(window, text='Logout')
logoutBtn.pack(pady=10, ipadx=7, padx=(440,10))

#Profile Image
profilePic = PhotoImage(file='user.png')
profileLabel = Label(window, image=profilePic)
profileLabel.pack(pady=(100, 20))

#Profile Info Label Frame
infoLabelFrame = LabelFrame(window, text='Info')
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
#                           END CODE                             #
##################################################################

#Main Loop
window.mainloop()
