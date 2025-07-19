from utils import clear_screen


class OrderManager:
    def __init__(self, db):
        self.db = db

    def take_order(self):
        clear_screen()
        table = input("Enter table (e.g., T1): ").strip().upper()
        area, number = table[0], table[1:]

        self.db.cursor.execute(
            "SELECT status FROM tables WHERE area = ? AND number = ?", (area, number)
        )
        result = self.db.cursor.fetchone()
        if not result:
            print("❌ Table not found.")
            return
        if result[0] != "using":
            print(f"⚠️ Table must be in 'using' state to order.")
            return

        while True:
            clear_screen()
            food_input = input("Enter food (or type 'x' to stop): ").strip()
            if food_input.lower() in ["x", "stop"]:
                break

            self.db.cursor.execute(
                "SELECT name, price FROM menu WHERE name LIKE ?", (f"{food_input}%",)
            )
            result = self.db.cursor.fetchone()
            if not result:
                print("❌ Food not found.")
                continue

            name, price = result
            try:
                amount = int(input(f"How many '{name}': "))
                note = input("Note anything: ")
                self.db.execute(
                    f"INSERT INTO {table} (food_name, amount, price, note) VALUES (?, ?, ?, ?)",
                    (name, amount, price, note),
                )
                input(f"✅ Ordered {amount} x {name}. Press Enter to continue...")
            except ValueError:
                print("❌ Invalid quantity.")

    def get_bill(self):
        clear_screen()
        table = input("Enter table name (e.g., T1): ").strip().upper()

        # Kiểm tra bảng hóa đơn có tồn tại
        try:
            self.db.cursor.execute(f"SELECT food_name, amount, price FROM {table}")
            orders = self.db.cursor.fetchall()
        except Exception as e:
            print(f"❌ Bill table '{table}' not found or error occurred.")
            return

        if not orders:
            print(f"📭 No orders found for table {table}.")
            return

        print(f"\n🧾 Bill for Table {table}")
        print("-" * 50)
        total_amount = 0
        total_price = 0

        print(f"{'No.':<4} {'Food':<20} {'Qty':<5} {'Price':<10} {'Total':<10}")
        print("-" * 50)

        for idx, (name, qty, price) in enumerate(orders, 1):
            item_total = int(qty) * int(price)
            total_amount += int(qty)
            total_price += item_total

            print(
                f"{idx:<4} {name.capitalize():<20} {qty:<5} {price:<10,} {item_total:<10,}"
            )

        print("-" * 50)
        print(f"{'TOTAL':<26} {total_amount:<5} {'':<10} {total_price:<10,}k VND")
