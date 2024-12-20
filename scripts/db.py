import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="<database_name>",
            user="<username>",
            password="<password>",
            host="<host>",
            port="<port>"
        )
        print("Connection successful")
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None



# Example Usage
# conn = connect_to_db()
# query = "SELECT * FROM your_table LIMIT 10;"
# data = fetch_data(query, conn)
