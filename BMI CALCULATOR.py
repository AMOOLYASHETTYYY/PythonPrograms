import tkinter

def cal_bmi():
    h = float(ht_val.get())
    w = float(wt_val.get())
    h1 = h / 100
    bmi = w / (h1 ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        status = "Normal"
    elif 25.0 <= bmi <= 29.9:
        status = "Overweight"
    else:
        status = "Obese"

    res.config(text=f"BMI IS {bmi} ({status})", bg="light green")

root = tkinter.Tk()
root.geometry("500x500")
root.title("BMI Calculator")
root.configure(bg="#FFE5B4")

head = tkinter.Label(root, text="BMI Calculator", font=("arial", 20, "bold"),bg="light pink")
head.pack(pady=50)

fr = tkinter.Frame(root, bg="light pink")
fr.pack(pady=5)

ht = tkinter.Label(fr, text="Height (cm)", font=("arial", 15),bg="yellow")
ht.grid(row=0, column=0, padx=5, pady=5)

ht_val = tkinter.Entry(fr)
ht_val.grid(row=0, column=1, padx=5, pady=5)

wt = tkinter.Label(fr, text="Weight (kg)", font=("arial", 15),bg="yellow")
wt.grid(row=1, column=0, padx=5, pady=5)

wt_val = tkinter.Entry(fr)
wt_val.grid(row=1, column=1, padx=5, pady=5)

bt = tkinter.Button(fr, text="Calculate", font=("Arial", 12, "bold"), command=cal_bmi)
bt.grid(row=2, column=0, columnspan=2, pady=10)

res = tkinter.Label(text="Your BMI will appear here", bg="light green", font=("Arial", 10, "bold"))
res.pack(pady=10)

root.mainloop()
