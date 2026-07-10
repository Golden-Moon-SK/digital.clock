import tkinter as tk #GUI import
from time import strftime #time import

root = tk.Tk()
root.title("Digital CLock") #title

def time():
    string = strftime('%H:%M:%S %p \n %D') #time format
    label.config(text=string) #update label with current time
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white') #designing using tkinter
label.pack(anchor='center')

time() #running everything
root.mainloop() #runs everything in a loop