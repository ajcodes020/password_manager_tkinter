import tkinter as tk
from tkinter import messagebox
import random
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    rand_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    rand_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random_password = rand_letter + rand_number + rand_symbol
    random.shuffle(random_password)
    password_input.delete(0, tk.END)
    final_password = "".join(random_password)
    password_input.insert(0, final_password)


def save_all():
    site_data = website_input.get().title()
    eu_data = email_username_input.get()
    pass_data = password_input.get()
    new_data = {
        site_data: {
            "email": eu_data,
            "pass": pass_data,
        }
    }

    if site_data.strip() == "" or eu_data.strip() == "" or pass_data.strip() == "":
        messagebox.showinfo(title="Empty Field", message="Don't leave empty field/s")
    else:
        is_ok = messagebox.askokcancel(title="Press OK to save", message=f"Verify to continue:\nWebsite: {site_data}\nEmail: {eu_data}\nPassword: {pass_data}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, tk.END)
                password_input.delete(0, tk.END)


def find_password():
    site_data = website_input.get().title()
    try:
        with open("data.json") as file:
            data = json.load(file)
            file_data = data[site_data]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title=site_data, message=f"No details for the {site_data} exists")
    else:
        eu_data = file_data['email']
        pass_data = file_data['pass']
        messagebox.showinfo(title=site_data, message=f"Email: {eu_data}\nPassword: {pass_data}")


window = tk.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = tk.Canvas(width=200, height=200)
mypass_img = tk.PhotoImage(file="mypass_logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = tk.Entry()
website_input.focus()
website_input.grid(row=1, column=1, columnspan=1, sticky="ew")
wensite_button = tk.Button(text="Search", command=find_password)
wensite_button.grid(row=1, column=2, sticky="ew")

email_username_label = tk.Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
email_username_input = tk.Entry()
email_username_input.insert(0, "sample@email.com")
email_username_input.grid(row=2, column=1, columnspan=2, sticky="ew")

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = tk.Entry()
password_input.grid(row=3, column=1, sticky="ew")
password_button = tk.Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="ew")

add_button = tk.Button(text="Add", command=save_all)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
