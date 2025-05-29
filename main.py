from db import get_connection
from user import User
from loan import Loan
from payment import Payment

def main():
    conn = get_connection()

    user = User(conn)
    if not user.login():
        conn.close()
        return

    loan = Loan(conn, user.username)
    payment = Payment(conn, user.username)

    while True:
        print("\n1. Apply for a loan\n2. Make a payment\n3. Check balance\n4. View payment history\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            loan.apply_for_loan()
        elif choice == "2":
            payment.make_payment()
        elif choice == "3":
            payment.check_balance()
        elif choice == "4":
            payment.view_payment_history()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

    conn.close()

if __name__ == "__main__":
    main()
