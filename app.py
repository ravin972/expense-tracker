from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = "expenses.json"

# Initialize file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def load_expenses():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

@app.route('/')
def index():
    expenses = load_expenses()
    total = sum(e["amount"] for e in expenses)
    avg = total / len(expenses) if expenses else 0
    return render_template('index.html', expenses=expenses, total=total, average=avg)

@app.route('/add', methods=['POST'])
def add():
    category = request.form['category']
    amount = float(request.form['amount'])
    
    # Get current date in the format DD/MM/YYYY
    from datetime import datetime
    current_date = datetime.now().strftime('%d/%m/%Y')

    expenses = load_expenses()
    expenses.append({
        "category": category,
        "amount": amount,
        "date": current_date
    })
    save_expenses(expenses)

    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
