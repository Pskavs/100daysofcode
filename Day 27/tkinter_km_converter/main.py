import tkinter as tk

#Sets up the GUI window.
window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(300, 150)
window.config(padx=50, pady=25)


#Creates an input for converting miles to km.
input = tk.Entry()
input.insert(0,string ='0')
input.grid(column=0, row=0)

#Creating the labels for the GUI, including the final answer after calculations.
label_miles = tk.Label(padx= 5, pady = 5, text="Miles", font=("Arial", 12))
label_miles.grid(column=1, row=0)

label_equal = tk.Label(padx= 5, pady = 5, text="is equal to", font=("Arial", 12))
label_equal.grid(column=0, row=1)

label_answer = tk.Label(padx= 5, pady = 5, text="0", font=("Arial", 12))
label_answer.grid(column=1, row=1)

label_km = tk.Label(padx= 5, pady = 5, text="Km", font=("Arial", 12))
label_km.grid(column=2, row=1)

#When the button is clicked, it calculates the km and displays it.
def calc_km():
     label_answer.config(text=round(float(input.get())/1.609,2))

#Creates the button to convert miles to km.
calc_button = tk.Button(text="Calculate", command=calc_km)
calc_button.grid(column=1, row=2)
calc_button.config(padx=5, pady=5)

#Keeps window open
window.mainloop()
