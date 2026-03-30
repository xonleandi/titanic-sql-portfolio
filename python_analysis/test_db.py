import psycopg2
try:
    conn = psycopg2.connect(host="127.0.0.1", port="5432", database="titanic_db", user="postgres", password="postgres")
    print("SUCCESS! Connection to PostgreSQL works!")
    conn.close()
except Exception as e:
    print(f"ERROR: {e}")
