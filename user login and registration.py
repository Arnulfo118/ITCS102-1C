import tkinter as tk 

window = tk.Tk()
window.geometry("500x300")
window.title("Profile Maker")

mainLabel = tk.Label(window, text="Profile Maker", font=("Arial", 15, "bold"))
mainLabel.pack(fill="x", anchor="center")

userNames = []
passwords = []

def open_login():
    
    login = tk.Toplevel()
    login.title("Login")
    login.resizable(False, False)
    login.geometry("400x300")
    
    loginFrame = tk.Frame(login, width=300, height=160, bg="light blue", borderwidth=2, relief="ridge")
    loginFrame.grid_propagate(False)
    
    loginLabel = tk.Label(loginFrame, text="Login your credentials here", bg="light blue", font=("Arial", 12, "bold"))
    loginLabel.grid(column=0, row=0, columnspan=2)
    
    loginFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    usernameLabel = tk.Label(loginFrame, text="Username:", bg="light blue")
    usernameLabel.grid(column=0, row=1, padx=10, pady=15)
    
    usernameEntry = tk.Entry(loginFrame, width=30, relief="ridge")
    usernameEntry.grid(column=1, row=1)
    
    passwordLabel = tk.Label(loginFrame, text="Password:", bg="light blue")
    passwordLabel.grid(column=0, row=2, padx=10, pady=15)
    
    passwordEntry = tk.Entry(loginFrame, width=30, relief="ridge")
    passwordEntry.grid(column=1, row=2)
    
    loginButton = tk.Button(loginFrame, text="Login", bg="light green", command=login)
    loginButton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    
    def login():
        userInput = usernameEntry.get()
        passInput = passwordEntry.get()
        user = user[0]
        passw = passw[0]
        
        if userInput != user:
            loginLabel.config(text="Wrong username")
        elif passInput != passw:
            loginLabel.config(text="Wrong password")
        elif userInput == "" or passInput == "":
            loginLabel.config(text="Invalid credentials")
        else:
            loginLabel.config(text="User logged in")

def open_register():
    register = tk.Toplevel()
    register.title("Register")
    register.geometry("400x200")
    register.resizable(False, False)
    
    def check():
        username = usernameEntry.get()
        password = passwordEntry.get()
        
        if len(username) <= 8:
            registerLabel.config(text=f"The username is less than 8.")
        elif len(password) <= 8:
            registerLabel.config(text=f"The password is less than 8.")
        else:
            registerLabel.config(text=f"Registered successfully")
            
        userNames.insert[username]
        passwords.insert[password]
            

    registerFrame = tk.Frame(register, width=300, height=160, bg="light blue", relief="ridge", borderwidth=2)
    registerFrame.grid_propagate(False)
    
    registerLabel = tk.Label(registerFrame, text="Register your credentials here", bg="light blue", font=("Arial", 12, "bold"))
    registerLabel.grid(column=0, row=0, columnspan=2)
    
    registerFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    usernameLabel = tk.Label(registerFrame, text="Username:", bg="light blue")
    usernameLabel.grid(column=0, row=1, padx=10, pady=15)
    
    usernameEntry = tk.Entry(registerFrame, width=30, relief="ridge")
    usernameEntry.grid(column=1, row=1)
    
    passwordLabel = tk.Label(registerFrame, text="Password:", bg="light blue")
    passwordLabel.grid(column=0, row=2, padx=10, pady=15)
    
    passwordEntry = tk.Entry(registerFrame, width=30, relief="ridge")
    passwordEntry.grid(column=1, row=2)
    
    submitButton = tk.Button(registerFrame, text="Register", bg="light green", command=check)
    submitButton.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


loginButton = tk.Button(window, text="Log In", font=("Arial", 15, "bold"), bg="sky blue", command=open_login)
loginButton.pack(anchor="center", fill="x", pady=30)
registerButton = tk.Button(window, text="Register", font=("Arial", 15, "bold"), bg="red", command=open_register)
registerButton.pack(anchor="center", fill="x", pady=10)






window.mainloop()