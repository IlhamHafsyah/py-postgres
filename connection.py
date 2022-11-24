import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="airflowdb", user='ngunajmi', password='P@ssw0rd123', host='10.239.2.12', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing a function using the execute() method
# insert query below
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()
# Connection established to: (
#    'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
# )