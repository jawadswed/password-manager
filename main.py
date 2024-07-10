from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_list += [random.choice(symbols) for i in range(nr_symbols)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_list += [random.choice(numbers) for i in range(nr_numbers)]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # method to copy to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        empty_fields = messagebox.askretrycancel(title="Error",
                                                 message="Please make sure the fields are filled.\n"
                                                         "Please Retry or Cancel")
        if empty_fields:
            return
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            return

    ok_to_save = messagebox.askokcancel(title=f"{website}",
                                        message=f"These are the details entered. \nEmail: {email} \nPassword: {password} \n"
                                                f"are you sure you want to save them? ")
    if ok_to_save:
        with open("password-manager.txt", 'a') as file:
            file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(300, 300)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW)
website_entry.focus()

email_username_Label = Label(text="Email/Username:")
email_username_Label.grid(column=0, row=2)

email_username_entry = Entry()
email_username_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
email_username_entry.insert(0, "swed.jawad@gmail.com")

password_Label = Label(text="Password:")
password_Label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky=EW)

generate_password_button = Button(text="Generate Password", command=generate_password, fg="yellow", bg="green")
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save, fg="yellow", bg="green")
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
