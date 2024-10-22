class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


MINIMAL_AGE = 18

user_input = input().split(', ')
user_pin = user_input[0]
user_balance = int(user_input[1])
user_age = int(user_input[2])

while True:
    command = input().split('#')
    cmd = command[0]

    if cmd == 'End':
        break

    if cmd == 'Send Money':
        money = int(command[1])
        pin_code = command[2]

        if money > user_balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin_code != user_pin:
            raise PINCodeError("Invalid PIN code")

        if user_age < MINIMAL_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        user_balance -= money

        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {user_balance:.2f} money left in the bank account")

    if cmd == 'Receive Money':
        money = int(command[1])

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        amount_received = money / 2

        print(f"{amount_received:.2f} money went straight into the bank account")