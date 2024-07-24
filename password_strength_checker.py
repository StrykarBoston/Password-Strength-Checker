import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PasswordEvaluator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Evaluator")
        self.root.geometry("420x650")
        self.root.configure(background='#faf0e6')

        self.password_label = tk.Label(root, text="Enter Password:", font=('Segoe UI', 20), fg='#3498db', bg='#f7f7f7')
        self.password_label.pack(pady=25)
        self.password_entry = tk.Entry(root, show="•", width=25, font=('Segoe UI', 20), fg='#333', bg='#fff')
        self.password_entry.pack(pady=15)

        self.evaluate_button = tk.Button(root, text="Evaluate Password", command=self.evaluate_password, 
                                         font=('Segoe UI', 20), fg='#fff', bg='#3498db', activebackground='#4caf50', bd=2)
        self.evaluate_button.pack(pady=25)

        self.show_password_button = tk.Button(root, text="Toggle Password", command=self.toggle_password, 
                                             font=('Segoe UI', 20), fg='#fff', bg='#3498db', activebackground='#4caf50', bd=2)
        self.show_password_button.pack(pady=15)

        self.result_label = tk.Label(root, text="", font=('Segoe UI', 20), fg='#333', bg='#f7f7f7')
        self.result_label.pack(pady=25)

        self.progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
        self.progress_bar.pack(pady=15)

        self.progress_label = tk.Label(root, text="", font=('Segoe UI', 20), fg='#333', bg='#f7f7f7')
        self.progress_label.pack(pady=15)

        self.show_password = False

    def evaluate_password(self):
        password = self.password_entry.get()
        strength = self.evaluate_password_logic(password)
        self.result_label.config(text=strength)
        self.update_progress_bar(strength)

    def evaluate_password_logic(self, password):
        if len(password) < 10:
            return "Weak Password"
        elif len(password) >= 10 and len(password) < 14:
            return "Medium Password"
        else:
            return "Strong Password"

    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show="•")
            self.show_password_button.config(text="Toggle Password")
            self.show_password = False
        else:
            self.password_entry.config(show="")
            self.show_password_button.config(text="Hide Password")
            self.show_password = True

    def update_progress_bar(self, strength):
        if strength == "Weak Password":
            self.progress_bar['value'] = 20
            self.progress_label.config(text="20%")
        elif strength == "Medium Password":
            self.progress_bar['value'] = 50
            self.progress_label.config(text="50%")
        else:
            self.progress_bar['value'] = 100
            self.progress_label.config(text="100%")

    def show_message(self, message):
        messagebox.showinfo("Password Evaluation", message, parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordEvaluator(root)
    root.mainloop()