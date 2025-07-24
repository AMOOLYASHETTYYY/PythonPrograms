import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.withdraw()
messagebox.showerror("Error","something went wrong")
messagebox.showerror("info","show")
messagebox.showerror("warning","show")
messagebox.showerror("critical","show")