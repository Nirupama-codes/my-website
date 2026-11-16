# ATM Simulation Program

# Initial balance and PIN
balance = 10000
correct_pin = "1234"
logged_in = False

# PIN validation with three attempts
for attempt in range(3):
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        print("\nLogin Successful!")
        logged_in = True
        break
    else:
        print("Incorrect PIN!")

# Lock message after three failed attempts
if not logged_in:
    print("\nATM Locked! Too many incorrect attempts.")

else:
    # ATM menu
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print(f"Your Current Balance: Rs. {balance:.2f}")

        # Deposit
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount < 0:
                print("Negative amount is not allowed.")
            else:
                balance += amount
                print("Amount deposited successfully.")
                print(f"Updated Balance: Rs. {balance:.2f}")

        # Withdraw
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount < 0:
                print("Negative amount is not allowed.")
            elif amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print("Withdrawal successful.")
                print(f"Updated Balance: Rs. {balance:.2f}")

        # Change PIN placeholder
        elif choice == "4":
            pass

        # Exit
        elif choice == "5":
            print("\nThank you for using ATM!")
            print(f"Final Balance: Rs. {balance:.2f}")
            break

        # Invalid choice
        else:
            print("Invalid choice! Please try again.")