#Import libraries.
from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Creates a randomly generated password with 8-10 letters, 2-4 numbers, and 2-4 special characters."""
    import random
    #if the user has data in the password field, it clears it.
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    #Adds the letters, symbols, and numbers to a password list and then it shuffles them.
    password_list.extend([random.choice(letters)for letter in range(random.randint(8,10))])
    password_list.extend([random.choice(symbols) for symbol in range(random.randint(2,4))])
    password_list.extend([random.choice(numbers) for number in range(random.randint(2,4))])
    random.shuffle(password_list)

    #Puts the password together and puts it in the password input box.
    password = ''.join(password_list)
    pass_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    try:
        with open('data.json', 'r') as data_file:
            # Reading old data, updating with new data, saving.
            data = json.load(data_file)
            website = web_input.get().lower()
            if website in data:
                print_email = data[website]['email']
                print_password = data[website]['password']
                messagebox.showinfo(title=website, message=f"Email: {print_email}\n Password:{print_password}")

                #puts the username and password into the fields so that they can be copied.
                email_input.delete(0, END)
                pass_input.delete(0, END)
                email_input.insert(0, print_email)
                pass_input.insert(0, print_password)
            elif website =='' or website not in data:
                messagebox.showerror(title="Error", message="Password not found")
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="Please save a password.")
def save_information():
    #Writes what is in the input boxes to a json file.
    website = web_input.get().lower()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    #Makes sure all fields are filled.
    if website == '' or email == '' or password == '':
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"You entered:\n \n Username:{email}\n Password:{password}\n \n"
                                                     f"Is it ok to save?")
        if is_ok:
            #Creates a json file and handles errors in creating it.
            try:
                with open('data.json', 'r') as data_file:
                    # Reading old data, updating with new data, saving.
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open('data.json','w') as data_file:
                    json.dump(new_data, data_file, indent=4)
                    print(data)
            finally:
                messagebox.showinfo("Saved", "Data saved successfully")
                # clears the fields
                web_input.delete(0, END)
                email_input.delete(0, END)
                pass_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

ui_font = ("Times", 10, "bold")
#Creates a window with UI in it.
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#Creates the logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo)
canvas.grid(row=0, column=1)

#Sets up website label.
web_label = Label(text="Website:",font=ui_font)
web_label.grid(row=1, column=0)

#Sets up the email label.
email_label = Label(text="Email/Username:",font=ui_font)
email_label.grid(row=2, column=0)

#Sets up the password label.
pass_label = Label(text="Password:",font=ui_font)
pass_label.grid(row=3, column=0)

#Sets up the entry box for the users to put the website they need the password for.
web_input=Entry(width=35)
web_input.grid(row=1, column=1,sticky="w")
web_input.focus()
search_button= Button(text="Search",font=ui_font,command=find_password)
search_button.grid(row=1, column=2,sticky="w")

#Sets up username entry box.
email_input=Entry(width=35)
email_input.grid(row=2, column=1,columnspan=2,sticky="w")

#Sets up password entry box and password generator
pass_input=Entry(width=21)
pass_input.grid(row=3, column=1,sticky="w")
pass_generator= Button(text="Generate Password",font=ui_font,command=generate_password)
pass_generator.grid(row=3, column=2,sticky="w")

#Enables copy and pasting from the text boxes

#Creates the add button which allows users to add password information to a text file.
add_button = Button(text="Add",font=ui_font,command=save_information)
add_button.grid(row=4,column=1)

#Keeps the window open until user exits.
mainloop()