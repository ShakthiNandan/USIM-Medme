
from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# Initialize the database
database.init_db()

@app.route('/')
def index():
    patients = database.get_patients()
    return render_template("index.html", patients=patients)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    ic_passport = request.form['ic_passport']
    admitted_date = request.form['admitted_date']
    remarks = request.form.get('remarks', '')
    database.add_patient(name, ic_passport, admitted_date, remarks)
    return redirect(url_for('index'))

@app.route('/edit/<int:patient_id>', methods=['POST'])
def edit(patient_id):
    name = request.form['name']
    ic_passport = request.form['ic_passport']
    remarks = request.form.get('remarks', '')
    database.edit_patient(patient_id, name, ic_passport, remarks)
    return redirect(url_for('index'))

@app.route('/discharge/<int:patient_id>', methods=['POST'])
def discharge(patient_id):
    database.discharge_patient(patient_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
