# main-0.py
import sys
from bank_account import BankAccount

def _fmt_amount(amount):
    """Format amount: show as int if whole number, otherwise show float."""
    try:
        a = float(amount)
    except (TypeError, ValueError):
        return str(amount)
    if a.is_integer():
        return str(int(a))
    return str(a)

def main():
    # Example starting balance as requested in the spec
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = None
    if params and params[0] != "":
        try:
            amount = float(params[0])
        except ValueError:
            # if amount is not numeric, mirror expected simple behavior: invalid command
            print("Invalid command.")
            return

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${_fmt_amount(amount)}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${_fmt_amount(amount)}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
