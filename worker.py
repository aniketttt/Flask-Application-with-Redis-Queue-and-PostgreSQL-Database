import redis
import psycopg2
import json
import time

redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

def process_queue():
    conn = psycopg2.connect(
        dbname='yourdbname',
        user='yourdbuser',
        password='yourdbpassword',
        host='postgres'
    )
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
