from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

FILE_NAME = 'attendance.csv'

# Create file if not exists
def create_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Date', 'Status'])
    except FileExistsError:
        pass

create_file()

# Home page - show data
@app.route('/')
def index():
    data = []
    
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)   # ✅ avoids error
            
            for row in reader:
                data.append(row)
    except:
        data = []

    return render_template('index.html', data=data)


# Add attendance
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    status = request.form['status']
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date, status])

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)