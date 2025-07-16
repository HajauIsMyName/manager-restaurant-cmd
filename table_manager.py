from utils import clear_screen
from db_handler import DBHandler
import time


class TableManager:
    def __init__(self, db: DBHandler):
        self.db = db

    def view_table_status(self):
        clear_screen()
        user_input = input("Enter area or table (e.g. T or T1): ").strip().upper()

        if not user_input:
            print("⚠️ No input provided.")
            return

        if len(user_input) == 1:  # Khu vực
            self.db.cursor.execute(
                "SELECT number, status, capacity FROM tables WHERE area = ?",
                (user_input,),
            )
            tables = self.db.cursor.fetchall()

            if not tables:
                print("❌ Area not found.")
                return

            print(f"\nTables in Area {user_input}:\n")
            tables.sort(
                key=lambda x: (
                    float(x[0]) if x[0].replace(".", "", 1).isdigit() else x[0]
                )
            )

            for i, (num, status, cap) in enumerate(tables, 1):
                print(
                    f"{user_input}{num:<4}: {status:<10} | Seats: {cap:<2}", end="   "
                )
                if i % 3 == 0:
                    print()
            print()
        else:  # Cụ thể bàn
            area, number = user_input[0], user_input[1:]
            self.db.cursor.execute(
                "SELECT status, capacity FROM tables WHERE area=? AND number=?",
                (area, number),
            )
            result = self.db.cursor.fetchone()
            if result:
                status, capacity = result
                print(
                    f"\nTable {user_input}: {status.capitalize()}, Capacity: {capacity}"
                )
            else:
                print("❌ Table not found.")

    def create_bill_table(self, table_name):
        try:
            self.db.execute(
                f"""CREATE TABLE {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    food_name TEXT NOT NULL,
                    amount INTEGER NOT NULL,
                    price INTEGER NOT NULL
                )"""
            )
            print(f"✅ Bill table for {table_name} created.")
        except Exception as e:
            print(f"⚠️ Table already exists or error: {e}")

    def drop_bill_table(self, table_name):
        try:
            self.db.execute(f"DROP TABLE IF EXISTS {table_name}")
            print(f"🧹 Bill table {table_name} cleared.")
        except Exception as e:
            print(f"⚠️ Failed to clear bill: {e}")

    def update_table_status(self, new_status="using"):
        clear_screen()
        table_input = input("Enter table (e.g., T1): ").strip().upper()

        if len(table_input) < 2:
            print("⚠️ Invalid input.")
            return

        area, number = table_input[0], table_input[1:]
        self.db.cursor.execute(
            "SELECT status FROM tables WHERE area=? AND number=?", (area, number)
        )
        result = self.db.cursor.fetchone()
        if not result:
            print("❌ Table not found.")
            return

        current_status = result[0]
        if current_status == new_status:
            print(f"⚠️ Table already in '{new_status}' state.")
            return

        if new_status == "using":
            self.create_bill_table(table_input)
        elif new_status == "empty":
            self.drop_bill_table(table_input)

        self.db.execute(
            "UPDATE tables SET status=? WHERE area=? AND number=?",
            (new_status, area, number),
        )
        print(f"✅ Updated table {table_input} to '{new_status}'")
