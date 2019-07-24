#Imports
from tkinter import *

#Window
window = Tk()
window.title('Small Component')

##################################################################
#                             CODE                               #
##################################################################

#Transactrions Page
transactionsPage = ttk.Frame(nb)
nb.add(transactionsPage, text='Transactions')

transLeftFrame = ttk.Frame(transactionsPage)



##################################################################
#                           END CODE                             #
##################################################################

#Main Loop
window.mainloop()
