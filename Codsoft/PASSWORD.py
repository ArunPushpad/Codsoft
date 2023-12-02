import tkinter  as tk
import tkinter.ttk as ttk
import secrets
import string

class Password:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.len_label = ttk.Label(root, text="Password length")
        self.len_label.grid(row=0,column=0,padx =10,pady =10, sticky="e")

        self.len_entry = ttk.Entry(root)
        self.len_entry.grid(row=0, column=1,padx=10,pady=10)

        self.complexity = ttk.Label(root, text="Complexity Level :")
        self.complexity.grid(row=1,column=0,padx =10,pady =10, sticky="e")

        self.complexity = ttk.Combobox(root, values=["Low", "Medium", "High"])
        self.complexity.current(1)
        self.complexity.grid(row=1, column=1, padx=10, pady=10)

        self.generate_but =  ttk.Button(root, text="Generate Passwword", command= self.generate_password)
        self.generate_but.grid(row=2, column=0, columnspan=2, pady=10)

        self.pass_label = ttk.Label(root, text="Generate Password : ")
        self.pass_label.grid(row=3,column=0,padx =10,pady =10, sticky="e")

        self.password = ttk.Entry(root, state="readonly")
        self.password.grid(row=3, column= 1, padx=10 , pady =10)

    def generate_password(self):
        try:
            length = int(self.len_entry.get())
            complexity = self.complexity.get().lower()
            if length <=0:
                self.password.configure(state="normal")
                self.password.delete(0, tk.END)
                self.password.insert(0 , "Invalid Length")
                self.password.configure(state="readonly")
                return
            characters= {
                "low": string.ascii_lowercase,
                "medium": string.ascii_letters + string.digits,
                "high" : string.ascii_letters + string.digits + string.punctuation
            }
            if complexity not in characters:
                complexity = "medium"

            password_characters = characters[complexity]
            password = ''.join(secrets.choice(password_characters) for _ in range(length))

            self.password.configure(state="normal")
            self.password.delete(0, tk.END)
            self.password.insert(0, password)
            self.password.configure(state="readonly")

        except ValueError:
            self.password.configure(state="normal")
            self.password.delete(0, tk.END)
            self.password.insert(0, "Invalid input")
            self.password.configure(state="readonly")



if __name__ == "__main__":
    root = tk.Tk()
    app = Password(root)
    root.mainloop()