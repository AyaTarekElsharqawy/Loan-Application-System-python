class Loan:
    def __init__(self, conn, username):
        self.conn = conn
        self.username = username

    def apply_for_loan(self):
        amount = float(input("Enter loan amount: "))
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE users SET loan_amount = loan_amount + %s, balance = balance + %s WHERE username = %s",
            (amount, amount, self.username)
        )
        self.conn.commit()
        print("Loan applied successfully.")
