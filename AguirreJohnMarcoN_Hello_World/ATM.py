

balance = 1000
pin = "1234"

print("Welcome to Simple ATM")

while True:
    entered_pin = input("\nEnter your PIN (or type exit to quit): ")

    if entered_pin.lower() == "exit":
        print("Thank you for using the ATM.")
        break

    if entered_pin == pin:

        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Reset PIN")
            print("5. Logout")

            choice = input("Choose an option (1-5): ")

            if choice == "1":
                print("Your balance is:", balance)

            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                balance += amount
                print("Deposit successful.")

            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                if amount <= balance:
                    balance -= amount
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance.")

            elif choice == "4":
                new_pin = input("Enter new PIN: ")
                pin = new_pin
                print("PIN successfully changed.")

            elif choice == "5":
                print("Logged out.")
                break

            else:
                print("Invalid option. Try again.")

    else:
        print("Incorrect PIN. Try again.")