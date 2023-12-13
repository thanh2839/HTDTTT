import mysql.connector
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


query = "SELECT * FROM advise_clothes.bodyform"
#try: 
mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "123456a@",
    database = "advise_clothes"
)
#if mydb.is_connected():
    #print("Connected to MySQL database")
    # ------------------------------------
    # Tạo một đối tượng Cursor để thực hiện truy vấn
    #cursor = mydb.cursor()
    # Thực hiện truy vấn
    #cursor.execute(query)
    # Lấy tất cả các dòng dữ liệu từ kết quả truy vấn
    #rows = cursor.fetchall()
    # Hiển thị kết quả
    #for row in rows:
    #    # Encode and decode each string in the tuple
    #    #encoded_row = tuple(element.encode('utf-8').decode('utf-8') if isinstance(element, str) else element for element in row)
    #    print(row)
    #    # ---------------------------------------
#except mysql.connector.Error as e:
    #print(f"Error connecting to MySQL: {e}")
'''finally:
    # Close the mydb
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed")
        '''
#---------database ------------------
class ConvertData:
    def __init__(self):
        self.resultBMI = []
        self.resultBodyForm = []
        self.resultFace = []
        self.resultEvent = []
    def convertBmi(self):
        #lay du lieu BMI
        dbBmi = mydb.cursor()
        dbBmi.execute("SELECT * FROM advise_clothes.bmi;")
        BMI = dbBmi.fetchall()
        for i  in BMI:
            dictBmi = {}
            dictBmi['id'] = i[0]
            dictBmi['category'] = i[1]
            self.resultBMI.append(dictBmi)
    def convertBodyForm (self):
        #lay du liệu dang người
        dbBodyForm = mydb.cursor()
        dbBodyForm.execute('SELECT * FROM advise_clothes.bodyform;')
        bodyForm = dbBodyForm.fetchall()
        for i in bodyForm:
            dictBodyForm = {}
            dictBodyForm['gender'] = i[0]
            dictBodyForm['id'] = i[1]
            dictBodyForm['form'] = i[2]
            self.resultBodyForm.append(dictBodyForm)
    def convertFace (self):
        #lay du lieu mat nguoi
        dbFace = mydb.cursor()
        dbFace.execute("SELECT * FROM advise_clothes.face;")
        face = dbFace.fetchall()
        for i in face:
            dictFace = {}
            dictFace['id'] = i[0]
            dictFace['face_shape'] = i[1]
            self.resultFace.append(dictFace)
    def convertEvent (self):
        #lay du lieu mat nguoi
        dbevent = mydb.cursor()
        dbevent.execute("SELECT * FROM advise_clothes.event;")
        event = dbevent.fetchall()
        for i in event:
            dictEvent = {}
            dictEvent['id'] = i[0]
            dictEvent['name'] = i[1]
            self.resultEvent.append(dictEvent)

#---------class cơ bản ---------------
class Person:
    def __init__(self, name, gender, age, BMI):
        self.name = name
        self.gender = gender
        self.age = age
        self.bmi = BMI
    def __str__(self):
        return f"{self.name} \n{self.gender}\n{self.age}\n{self.bmi}"
class Validate:
    def __init__(self) -> None:
        pass
    def validate_input_number_form(self,value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            check = valueGetRidOfSpace.isnumeric()
            if (check):
                return valueGetRidOfSpace
            else:
                print("-->Chatbot: Vui lòng nhập 1 số dương")
                value = input()
    def validate_name(self, value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))

            check = valueGetRidOfSpace.isalpha()
            if (check):
                # print("Tôi đã nhận được thông tin Tên của bạn")
                return value
            else:
                print("-->Chatbot: Vui lòng nhập lại tên ! ")
                value = input()
    def validate_gender(self, value):
        while(1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            if (valueGetRidOfSpace == 'nam'):
                return 1
            elif (valueGetRidOfSpace == 'nữ' or valueGetRidOfSpace == 'nu'):
                return 0
            else :
                print("hãy nhập giới tính là nam hoặc nữ ! ")
                value = input()
    def validate_age (self, value):
        while(1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            check = valueGetRidOfSpace.isnumeric()
            if(check and int(valueGetRidOfSpace) >= 0 and int(valueGetRidOfSpace) <= 150):
                return valueGetRidOfSpace
            else:
                print("-->Chatbot: Vui lòng nhập lại tuổi ! ")
                value = input()
    def validate_number (self, value):
        while(1):
            try:
                check = float(value)
                return value
            except ValueError:
                print("-->Chatbot: Vui lòng nhập lại là số ! ")
                value = input()



#db = ConvertData()
#print(db.resultFace)