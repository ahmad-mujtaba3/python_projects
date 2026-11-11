class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

balance = 0

def save(record):
    try:
        with open("transactions.txt", "a") as f:
            f.write(record + "\n")
    except OSError:
        print("File error!")

def amount():
    value = float(input("Enter amount: "))
    if value <= 0:
        raise InvalidAmountError("Amount must be positive!")
    return value

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose: ")

    try:
        if choice == "1":
            balance = 0
            print("Account created!")

        elif choice == "2":
            a = amount()
            balance += a
            save(f"Deposited: {a}")
            print("Deposit successful!")

        elif choice == "3":
            a = amount()
            if a > balance:
                raise InsufficientFundsError("Insufficient balance!")
            balance -= a
            save(f"Withdrawn: {a}")
            print("Withdrawal successful!")

        elif choice == "4":
            print("Balance:", balance)

        elif choice == "5":
            break

        else:
            print("Invalid menu option!")

    except ValueError:
        print("Enter a valid number!")

    except InvalidAmountError as e:
        print(e)

    except InsufficientFundsError as e:
        print(e)