# Extract username from a given email.
# Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh
def extract_username(email):
    # Split the email at '@'
    parts = email.split('@')
    
    # Check if there is a valid email structure
    if len(parts) != 2:
        return "Invalid email address"
    
    # The username is the part before '@'
    username = parts[0]
    return username

def main():
    # Input email from the user
    email = input("Enter the email address: ")
    
    # Extract and print the username
    username = extract_username(email)
    print(f"The username is: {username}")

if __name__ == "__main__":
    main()
