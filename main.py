import tkinter as tk

window = tk.Tk()
window.title('BMI Calculator')
window.minsize(width=300, height=250)
window.config(bg='white', padx=30, pady=30)

# Entry Weight Label
weight_label = tk.Label(text='Enter Your Weight (kg)', fg='black', bg='white')
weight_label.pack()

# Weight Entry
weight_entry = tk.Entry(bg='white', fg='black', highlightbackground='white')
weight_entry.focus()
weight_entry.pack()


# height label
height_label = tk.Label(text='Enter Your Height (cm)', fg='black', bg='white')
height_label.pack()

# height entry:
height_entry = tk.Entry(bg='white', fg='black', highlightbackground='white')
height_entry.pack()

# calculation button

def calculator():
    try:
        # return weight / (height * height)
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        result = (weight) / (((height) / 100) ** 2) # BMI Formula
        if result < 16:
            result_string = "severely thin!"
        elif 16 < result <= 17:
            result_string = "moderately thin!"
        elif 17 < result <= 18.5:
            result_string = "mild thin!"
        elif 18.5 < result <= 25:
            result_string = "normal weight"
        elif 25 < result <= 30:
            result_string = "overweight"
        elif 30 < result <= 35:
            result_string = "obese class 1"
        elif 35 < result <= 40:
            result_string = "obese class 2"
        else:
            result_string = "obese class 3"
        print(result_string)
        result_label.config(text=f'Your bmi is: {round(result, 3)}. You are {result_string}.')
    except:
        result_label.config(text='Error: Please Enter Your Weight and Height Carefully.')

calculate_button = tk.Button(text='Calculate', bg='white', highlightbackground='white', command=calculator)
calculate_button.pack()

# result label
result_label = tk.Label(text='',bg='white', fg='black')
result_label.pack()

window.mainloop()