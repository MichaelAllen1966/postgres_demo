import psycopg2

# Define dictionary of field names and data types
fields = {
    'id': 'SERIAL PRIMARY KEY',
    'name': 'VARCHAR(255)',
    'age': 'INTEGER',
    'email': 'VARCHAR(255)'
}

# Connect to local Postgres instance
conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="test",
    password="test123"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Construct the CREATE TABLE statement using the field dictionary
field_strings = [f"{field} {data_type}" for field, data_type in fields.items()]
create_table_statement = f"CREATE TABLE names ({', '.join(field_strings)})"

# Execute the CREATE TABLE statement
cur.execute(create_table_statement)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

