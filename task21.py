# Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit
def cm_to_feet(cm):
    return cm / 30.48

def km_to_miles(km):
    return km * 0.621371

def usd_to_inr(usd, conversion_rate=83.0):
    return usd * conversion_rate

def display_menu():
    print("\nMenu:")
    print("1. Convert cm to feet")
    print("2. Convert km to miles")
    print("3. Convert USD to INR")
    print("4. Exit")

while True:
    display_menu()
    
    try:
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            cm = float(input("Enter the length in centimeters: "))
            feet = cm_to_feet(cm)
            print(f"{cm} cm is equal to {feet:.2f} feet.")
        
        elif choice == 2:
            km = float(input("Enter the distance in kilometers: "))
            miles = km_to_miles(km)
            print(f"{km} km is equal to {miles:.2f} miles.")
        
        elif choice == 3:
            usd = float(input("Enter the amount in USD: "))
            conversion_rate = float(input("Enter the conversion rate (USD to INR): "))
            inr = usd_to_inr(usd, conversion_rate)
            print(f"${usd} USD is equal to ₹{inr:.2f} INR.")
        
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Please enter a valid number.")
