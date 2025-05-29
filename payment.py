class Payment:
    def __init__(self, conn, username):
        self.conn = conn
        self.username = username

    def make_payment(self):
        amount = float(input("Enter payment amount: "))
        cur = self.conn.cursor()
      
        cur.execute("SELECT balance FROM users WHERE username = %s", (self.username,))
        balance = cur.fetchone()[0]

        if amount > balance:
            print("Insufficient balance! Payment cannot be processed.")
            return

        cur.execute("UPDATE users SET balance = balance - %s WHERE username = %s", (amount, self.username))
        cur.execute("INSERT INTO payments (username, amount) VALUES (%s, %s)", (self.username, amount))
        self.conn.commit()
        print("Payment recorded.")

    def check_balance(self):
        cur = self.conn.cursor()
        cur.execute("SELECT balance FROM users WHERE username = %s", (self.username,))
        balance = cur.fetchone()[0]
        print(f"Current balance: {balance}")

    def view_payment_history(self):
        cur = self.conn.cursor()
        cur.execute("SELECT amount, payment_date FROM payments WHERE username = %s ORDER BY payment_date DESC", (self.username,))
        payments = cur.fetchall()
        if payments:
            print("Payment History:")
            for amount, date in payments:
                print(f"- {amount} on {date}")
        else:
            print("No payment history found.")
