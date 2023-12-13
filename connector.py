import mysql.connector
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

query = "SELECT * FROM advise_clothes.bodyform"
try: 
    mydb = mysql.connector.connect (
        host="localhost",
        user="root",
        password="123456a@",
        database="advise_clothes"
    )
    if mydb.is_connected():
        print("Connected to MySQL database")
        # ------------------------------------
        # Tạo một đối tượng Cursor để thực hiện truy vấn
        cursor = mydb.cursor()

        # Thực hiện truy vấn
        cursor.execute(query)

        # Lấy tất cả các dòng dữ liệu từ kết quả truy vấn
        rows = cursor.fetchall()

        # Hiển thị kết quả
        for row in rows:
            # Encode and decode each string in the tuple
            encoded_row = tuple(element.encode('utf-8').decode('utf-8') if isinstance(element, str) else element for element in row)
            print(encoded_row)

        # ---------------------------------------
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    # Close the mydb
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed")
