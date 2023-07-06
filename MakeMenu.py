def menu():
    print("Chose option you want: ")
    print("Option 1: Sum of digits")
    print("Option 2: Product of even digits")
    print("Option 3: Count odd numbers")
    print("Option 4: Find max number")
    print("Option 5: Find min number")
    print("Option 6: Sum of digits")
    print("Option 7: Exit")

def get_user_choice():
    choice = input("Enter your choice (1-7): ")
    return choice

def execute_option(choice):
    if choice == "1":
        print("Option 1: Sum of digits")
        # Add your code for Option 1 here
    elif choice == "2":
        print("Option 2: Product of digits")
        # Add your code for Option 2 here
    elif choice == "Option 3: Count odd numbers":
        print("You selected Option 3.")
        # Add your code for Option 3 here
    elif choice == "Option 4: Find max number":
        print("You selected Option 4.")
        # Add your code for Option 4 here
    elif choice == "Option 5: Find min number":
        print("You selected Option 5.")
        # Add your code for Option 5 here
    elif choice == "Option 6: Sum of digits":
        print("You selected Option 5.")
        # Add your code for Option 5 here
    elif choice == "Option 7: Exit":
        print("Exiting the program...")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True