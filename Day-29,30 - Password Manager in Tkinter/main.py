# ....................... Password Manager ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 08-04-2022 .....#
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # password_characters = pw_numbers + pw_symbols + pw_letters
    password_letters = [choice(letters) for _ in range(0, nr_letters)]
    password_numbers = [choice(numbers) for _ in range(0, nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(0, nr_symbols)]
    password_characters = password_letters + password_numbers + password_symbols

    # print(password_characters)
    shuffle(password_characters)

    password = "".join(password_characters)
    print(f"your password is {password}' and it's length is {len(password)}")
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get().lower()
    email = email_entry.get()
    pass_word = password_entry.get()

    new_data = {website: {
        "email": email,
        "password": pass_word
        }

    }

    if len(website) == 0 or len(pass_word) == 0:
        messagebox.showinfo(title="Error", message="Please enter correct details!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"email entered: {email}\npassword entered: {pass_word}\n"
                                                              f"Are these OK?")
        if is_ok:
            try:
                with open("password_details.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("password_details.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except JSONDecodeError:
                with open("password_details.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                # Saving updated data
                with open("password_details.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, string="@gmail.com")
                password_entry.delete(0, END)

# ---------------------------- RETRIEVE PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get().lower()
    try:
        with open("password_details.json", "r") as search_file:
            data = json.load(search_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"The passwords' data doesn't exist")
    except JSONDecodeError:
        messagebox.showinfo(title="Error", message=f"The details of {website_entry.get()} doesn't exist!")
    else:
        if website in data:
            # retrieved_data = {key: value for (key, value) in data.items() if key == website}
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {email}\nPassword: {password}")
        # except KeyError:
        #     messagebox.showinfo(title="Error", message=f"The details of {website_entry.get()} doesn't exist!")
        else:
            messagebox.showinfo(title="Error", message=f"The details of {website_entry.get()} doesn't exist!")




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 12))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Arial", 12))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 12))
password_label.grid(row=3, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=70)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string="@gmail.com")

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, sticky="w")

generate_button = Button(text="Generate Password", font=("Arial", 12), highlightthickness=0,
                         width=18, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", font=('Arial', 12), width=46, justify="left", highlightthickness=0,
                    command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", font=("Arial", 12), highlightthickness=0, width=18, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
