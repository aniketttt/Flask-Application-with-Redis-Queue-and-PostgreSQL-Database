import redis
import psycopg2
import json
import time

redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

def connect_to_db(retries=5):
    conn = None
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname='mydb',
                user='admin',
                password='admin',
                host='postgres'
            )
            break
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    return conn

def process_queue():
    conn = connect_to_db()
    if not conn:
        print("Failed to connect to the database after several retries.")
        return
    
    cursor = conn.cursor()
    
    while True:
        _, data = redis_client.blpop('form_queue')
        data = json.loads(data)

        cursor.execute(
            "INSERT INTO your_table_name (name, email) VALUES (%s, %s)",
            (data['name'], data['email'])
        )
        conn.commit()

if __name__ == '__main__':
    process_queue()
