import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EMPLOYEES"
)

mycursor = mydb.cursor()  # Fixed typo: `mybd.cusrsor()` → `mydb.cursor()`

# Create table (Fixed: AUTO_INCREMENT, not AUTO-INCREASE)
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS CUSTOMERS (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        NAME VARCHAR(255) NOT NULL,
        EMAIL VARCHAR(255) NOT NULL UNIQUE
    )
""")

# Insert data into CUSTOMERS (Fixed: extra spacing in `VALUES(%s,%s)`)
sql = "INSERT INTO CUSTOMERS (NAME, EMAIL) VALUES (%s, %s)"
val = ("JOHN DOE", "john@email.com")
mycursor.execute(sql, val)
mydb.commit()  # Commit changes

# Update customer (Fixed: `UPDATE CUSTOME` → `UPDATE CUSTOMERS`)
sql = "UPDATE CUSTOMERS SET NAME = %s WHERE ID = %s"
val = ("JANE DOE", 1)
mycursor.execute(sql, val)  # Fixed: `mycursor,execute` → `mycursor.execute`
mydb.commit()

# Read all customers
mycursor.execute("SELECT * FROM CUSTOMERS")
mytable = mycursor.fetchall()
for row in mytable:
    print(row)

# Read the updated customer (Fixed: `WHER` → `WHERE`, `CUSTOMER` → `CUSTOMERS`)
mycursor.execute("SELECT * FROM CUSTOMERS WHERE ID = 1")
myupdate = mycursor.fetchall()
print("Updated Customer:", myupdate)

# Delete a customer (Fixed: `mycursor,execute` → `mycursor.execute`)
mycursor.execute("DELETE FROM CUSTOMERS WHERE ID = 2")
mydb.commit()

# Close connection
mycursor.close()
mydb.close()
