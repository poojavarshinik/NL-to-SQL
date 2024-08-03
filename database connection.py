import mysql.connector
# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="host",
    user="user",
    password="password",  # Replace with your actual password
    database="database name"
)

# Function to retrieve the database schema
def get_db_schema(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    schema_details = ""
    for table in tables:
        table_name = table[0]
        schema_details += f"Table: {table_name}\n"
        cursor.execute(f"DESCRIBE `{table_name}`")  # Use backticks to escape table names
        columns = cursor.fetchall()
        for column in columns:
            schema_details += f"  {column[0]} ({column[1]})\n"
    return schema_details

# Retrieve the schema details
schema_details = get_db_schema(db_connection)