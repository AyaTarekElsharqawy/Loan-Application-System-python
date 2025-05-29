class User:
    def __init__(self, conn):
        self.conn = conn
        self.username = None

    def login(self):
        cur = self.conn.cursor()
        username = input("Username: ")
        password = input("Password: ")

        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        if user:
            print(f"Welcome back, {username}!")
            self.username = username
            return True
        else:
            print("User not found.")
            choice = input("Do you want to register? (yes/no): ")
            if choice.lower() == "yes":
                return self.register(username, password)
            return False

    def register(self, username, password):
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.conn.commit()
            print("Registration successful.")
            self.username = username
            return True
        except Exception as e:
            print("Error during registration:", e)
            return False
