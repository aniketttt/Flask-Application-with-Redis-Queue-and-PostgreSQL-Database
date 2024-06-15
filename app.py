from flask import Flask, request, redirect, url_for, render_template
import redis
import json
import psycopg2
import time

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

def init_db():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname='mydb',
                user='admin',
                password='admin',
                host='postgres'
            )
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS your_table_name (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100),
                    age INT,
                    city VARCHAR(100)
                )
            ''')
            conn.commit()
            cursor.close()
            conn.close()
            break
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'age': request.form['age'],
        'city': request.form['city']
    }
    redis_client.rpush('form_queue', json.dumps(data))
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/view_data')
def view_data():
    conn = psycopg2.connect(
        dbname='mydb',
        user='admin',
        password='admin',
        host='postgres'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT name, email, age, city FROM your_table_name')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_data.html', rows=rows)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
