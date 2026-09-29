print("===== BANK ACCOUNT MANAGEMENT SYSTEM =====")

name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

while True:
    print("\n===== MENU =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Amount deposited successfully.")
            print("Updated Balance:", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Amount withdrawn successfully.")
            print("Remaining Balance:", balance)

    elif choice == 3:
        print("\nCurrent Balance:", balance)

    elif choice == 4:
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Holder:", name)
        print("Account Number:", account_number)
        print("Current Balance:", balance)

    elif choice == 5:
        print("\nThank you for using the Bank Account Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
