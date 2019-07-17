from tkinter import *
from tkinter import ttk

window = Tk()
window.title('BudgetApp')
window.geometry('500x500')

rows = 0
while rows < 50:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows, weight=1)
    rows += 1

nb = ttk.Notebook(window)
nb.grid(row=1, column=0, rowspan=49, columnspan=50, sticky='NESW')

profilePage = ttk.Frame(nb)
nb.add(profilePage, text='Profile')

transactionsPage = ttk.Frame(nb)
nb.add(transactionsPage, text='Transactions')

incomePage = ttk.Frame(nb)
nb.add(incomePage, text='Income')

budgetPage = ttk.Frame(nb)
nb.add(budgetPage, text='Budget')

historyPage = ttk.Frame(nb)
nb.add(historyPage, text='History')

goalsPage = ttk.Frame(nb)
nb.add(goalsPage, text='Goals')

suggestionsPage = ttk.Frame(nb)
nb.add(suggestionsPage, text='Suggestions')


window.mainloop()
