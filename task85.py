# Write a dummy program that can perform login and registration using a menu driven program
# Dummy database to store user credentials
user_database = {}

def register_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    if username in user_database:
        print("Username already exists. Please choose a different username.")
    else:
        user_database[username] = password
        print("Registration successful!")

def login_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    if username in user_database and user_database[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()