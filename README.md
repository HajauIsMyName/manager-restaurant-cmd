## 📄 `README.md`

```markdown
A **command-line application** written in Python for managing restaurant operations such as seating customers, taking orders, managing tables, and generating bills — all backed by a **SQLite** database.
```

---

## 📦 Project Structure

```
restaurant/
├── main.py               # Entry point
├── db\_handler.py         # SQLite database wrapper
├── table\_manager.py      # Manages table status and bills
├── order\_manager.py      # Order-taking & billing logic
├── utils.py              # Helper functions (e.g., clear screen)
├── data.db               # SQLite database file
└── README.md             # Project documentation

````

---

## ⚙️ How to Run

> 💡 Requires Python 3.8+ installed.

### 1. Clone the repository
```bash
git clone https://github.com/HajauIsMyName/manager-restaurant-cmd.git
cd manager-restaurant-cmd
````

### 2. Run the app

```bash
python main.py
```

---

## 🗃️ Database Schema

### Table: `tables`

| Column   | Type    | Description                |
| -------- | ------- | -------------------------- |
| area     | TEXT    | Table area (e.g. C, B)     |
| number   | TEXT    | Table number (e.g. 1, 2.1) |
| status   | TEXT    | Current table status (or default is empty)      |
| capacity | INTEGER | Number of seats            |

### Table: `menu`

| Column      | Type    | Description          |
| ----------- | ------- | -------------------- |
| name        | TEXT    | Food name            |
| price       | INTEGER | Price (e.g. 10k VND, 200k VND)          |
| type        | TEXT    | Food category        |
| description | TEXT    | Optional description |

> When a table is occupied, a new table (e.g., `B2`) is created to store its bill.

---


## 🤝 Contributing

Pull requests and suggestions are welcome! If you'd like to contribute, fork the repository and submit a PR.

---

## 📝 License

This project is licensed under the MIT License.

---

## ✉️ Contact

* **Author:** Lâm Hậu
* **Facebook:** [Lâm Hậu](https://www.facebook.com/hajauismyname/)
* **GitHub:** [github.com/HajauIsMyName](https://github.com/HajauIsMyName)