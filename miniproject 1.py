from tkinter import *

def open_calculator_window():
    # New window
    calc_win = Toplevel(root)
    calc_win.title("Calculator + Grade Calculator")
    calc_win.geometry("400x600")

    Label(calc_win, text="Student Details", fg="white", bg="purple", font=("Arial", 14)).pack(fill=X, pady=5)

    # ------------------ Student Details ------------------
    Label(calc_win, text="Student Name:").pack()
    stu_name = Entry(calc_win)
    stu_name.pack()

    Label(calc_win, text="Roll Number:").pack()
    stu_roll = Entry(calc_win)
    stu_roll.pack()

    # ------------------ Calculator ------------------
    Label(calc_win, text="Python Calculator", fg="white", bg="blue", font=("Arial", 14)).pack(fill=X, pady=5)

    Label(calc_win, text="Enter first number:").pack()
    entry_calc1 = Entry(calc_win)
    entry_calc1.pack()

    Label(calc_win, text="Enter second number:").pack()
    entry_calc2 = Entry(calc_win)
    entry_calc2.pack()

    Label(calc_win, text="Enter operator (+, -, *, /):").pack()
    operator = Entry(calc_win)
    operator.pack()

    lbl_calc_result = Label(calc_win, text="Result will appear here", fg="red")
    lbl_calc_result.pack(pady=5)

    def calculate():
        try:
            a = float(entry_calc1.get())
            b = float(entry_calc2.get())
            op = operator.get()

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b
            else:
                result = "Invalid operator"

            lbl_calc_result.config(text=f"Result: {result}")
        except:
            lbl_calc_result.config(text="Error! Enter valid numbers.")

    Button(calc_win, text="Calculate", command=calculate, bg="lightblue").pack(pady=5)

    # ------------------ Grade Calculator ------------------
    Label(calc_win, text="Grade Calculator", fg="white", bg="green", font=("Arial", 14)).pack(fill=X, pady=10)

    Label(calc_win, text="MATHS marks:").pack()
    maths = Entry(calc_win)
    maths.pack()

    Label(calc_win, text="CPS marks:").pack()
    cps = Entry(calc_win)
    cps.pack()

    Label(calc_win, text="CHE marks:").pack()
    che = Entry(calc_win)
    che.pack()

    Label(calc_win, text="EEE marks:").pack()
    eee = Entry(calc_win)
    eee.pack()

    Label(calc_win, text="History marks:").pack()
    Hitory = Entry(calc_win)
    Hitory.pack()

    Label(calc_win, text="Master your mind marks:").pack()
    Master_your_mind = Entry(calc_win)
    Master_your_mind.pack()

    lbl_grade_result = Label(calc_win, text="Grade result here", fg="purple")
    lbl_grade_result.pack(pady=5)

    def grade_calculate():
        try:
            m = float(maths.get())
            c = float(cps.get())
            h = float(che.get())
            e = float(eee.get())
            H= float(Hitory.get())
            M= float(Master_your_mind.get())
            name = stu_name.get()
            roll = stu_roll.get()

            # FAIL condition < 20
            if m < 20 or c < 20 or h < 20 or e < 20 or H < 20 or M < 20:
                lbl_grade_result.config(text=f"Name: {name}\nRoll: {roll}\nResult: FAIL (F Grade)")
                return

            total = m + c + h + e + H + M
            percent = total / 6

            if percent >= 90:
                grade = "A"
            elif percent >= 75:
                grade = "B"
            elif percent >= 60:
                grade = "C"
            elif percent >= 50:
                grade = "D"
            else:
                grade = "E"

            lbl_grade_result.config(
                text=f"Name: {name}\nRoll: {roll}\nTotal: {total}, %: {percent:.2f}\nGrade: {grade}"
            )
        except:
            lbl_grade_result.config(text="Enter valid marks")


    Button(calc_win, text="Calculate Grade", command=grade_calculate, bg="lightgreen").pack(pady=5)



# ------------------ MAIN WINDOW ------------------
root = Tk()
root.title("Main Menu")
root.geometry("300x200")

Label(root, text="Click below to open Calculator", font=("Arial", 12)).pack(pady=20)

Button(root, text="Open Calculator", font=("Arial", 14), bg="orange", command=open_calculator_window).pack(pady=20)

root.mainloop()
# ------------------ END OF CODE ------------------



#| Tkinter Component | Purpose           |
#| ----------------- | ----------------- |
#| Tk()            | Main window       |
#| Toplevel()      | New sub-window    |
#| Label           | Display text      |
#| Entry           | Input box         |
#| Button          | Buttons           |
#| pack()          | Layout manager    |
#| config()        | Update label text |
