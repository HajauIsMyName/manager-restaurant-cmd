from db_handler import DBHandler
from table_manager import TableManager
from order_manager import OrderManager
from utils import clear_screen


def main():
    db = DBHandler()
    table_mgr = TableManager(db)
    order_mgr = OrderManager(db)

    while True:
        clear_screen()
        print("🍽️ Restaurant Management System\n")
        print("1. View table status")
        print("2. Seat customer")
        print("3. Take order")
        print("4. Get bill")
        print("5. Clear table")
        print("6. View menu")
        print("0. Exit\n")

        choice = input("Enter choice: ").strip()
        match choice:
            case "1":
                table_mgr.view_table_status()
                input("\nPress Enter to continue...")

            case "2":
                table_mgr.update_table_status("using")
                input()

            case "3":
                order_mgr.take_order()
                input()

            case "4":
                order_mgr.get_bill()
                input()

            case "5":
                table_mgr.update_table_status("empty")
                input()

            case "6":
                view_menu(db)
                input()

            case "0":
                break

            case _:
                input("Invalid choice. Press Enter...")

    db.close()


def view_menu(db):
    clear_screen()
    db.cursor.execute("SELECT name, price, type FROM menu ORDER BY type, name")
    rows = db.cursor.fetchall()

    if not rows:
        print("⚠️ Menu is empty.")
        return

    current_type = None
    for name, price, food_type in rows:
        if food_type != current_type:
            current_type = food_type
            print(f"\n🍴 {food_type.upper()}")
            print("-" * 30)
        print(f"{name.capitalize():<20} {price}k VND")


if __name__ == "__main__":
    main()
