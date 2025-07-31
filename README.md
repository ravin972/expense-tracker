# 🧾 Expense Tracker

A simple and interactive **Command Line Expense Tracker** built in Python to help you record, view, and manage your expenses. Data is stored in a JSON file for persistence.

---

## 📌 Features

- ✅ Add expenses with name and amount
- 📋 List all expenses with total and average
- ❌ Delete expenses by index
- 💾 Data saved in JSON file (persistent)
- 💡 Easy to extend into a GUI or web version

---

## 📂 Project Structure

```

expense\_tracker/
├── app.py          # Main application file
├── expenses.json       # Data storage (auto-created)
└── README.md           # Project documentation

````

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone https://github.com/your-username/cli-expense-tracker.git
cd cli-expense-tracker
````

2. Run the app:

```bash
python tracker.py
```

---

## 🖥️ Demo

```
🧾 Expense Tracker Menu
1. Add Expense
2. List Expenses
3. Delete Expense
4. Exit

Choose (1-4):
```

---

## 🔧 Sample Expense Record (JSON)

```json
[
  {
    "name": "Groceries",
    "amount": 500
  },
  {
    "name": "Internet Bill",
    "amount": 999
  }
]
```

---

## 🛠️ Technologies Used

* Python 3.x
* JSON for data persistence
* Standard Python modules (`os`, `json`)

---

## 🌱 Future Improvements

* Add search and filter options
* Export data to CSV
* GUI version using Tkinter
* Web version using Flask or Django

---

## 📬 Contribute

Pull requests are welcome! Feel free to fork and enhance.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

