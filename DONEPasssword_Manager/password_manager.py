from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key

def enter():
    mode = input("Would you like to view or add passwords. (press q to quit) ")
    if mode.lower() == "add":
        add()
    elif mode.lower() == "view":
        view()
    elif mode.lower() == "q":
        quit()
    else: 
        print("Please enter view, add, or q")
        quit()

def add():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{username}|{fer.encrypt(password.encode()).decode()}\n")
    enter()

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            loginID = line.rstrip()
            username, password = loginID.split("|")
            print(f"Username: {username}\nPassword: {fer.decrypt(password.encode()).decode()}\n")
    enter()

#driver code
masterPassword = input("Enter master password: ")
key = load_key() + masterPassword.encode()
fer = Fernet(key)
enter()