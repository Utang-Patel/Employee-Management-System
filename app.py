from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1008", 
    database="employee_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone = request.form['phone']
    salary = request.form['salary']
    cursor.execute("INSERT INTO employees (name, phone, salary) VALUES (%s, %s, %s)", (name, phone, salary))
    db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
    employee = cursor.fetchone()
    return render_template('edit.html', employee=employee)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    phone = request.form['phone']
    salary = request.form['salary']
    cursor.execute("UPDATE employees SET name = %s, phone = %s, salary = %s WHERE id = %s", (name, phone, salary, id))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
