

from class_database import *
#khởi tạo
person = Person(None, None, None, None)
validate = Validate()
list_clothes = []
list_hair = []
height = 0.0
weight = 0.0
BMI = 0.0
BMIid = ''
db = ConvertData()
db.convertBmi()
db.convertBodyForm()
db.convertFace()
db.convertEvent()
#print(db.resultBodyForm[0]['gender'])

#############################
# người
def welcome_question ():
    print("-->Chatbot: Xin chào, tôi là chatbot tư vấn trang phục!")
    print("-->Chatbot: Để có thể tư vấn tốt nhất, hãy để lại tên, giới tính và tuổi của bạn")

    print("-->Chatbot: Đầu tiên hãy nhập tên")
    person.name = validate.validate_name(input())
    print(f'-->Chatbot: Tên của bạn là: {person.name}')

    print("-->Chatbot: Hãy nhập giới tính của bạn")
    person.gender = validate.validate_gender(input())
    if(person.gender == 1):
        print("-->Chatbot: Tôi đã có giới tính của bạn là nam")
    if(person.gender == 0):
        print("-->Chatbot: Tôi đã có giới tính của bạn là nữ")
    print("-->Chatbot: Hãy nhập tuổi của bạn")
    person.age = validate.validate_age(input())
    print(f'-->Chatbot: Tuổi của bạn: {person.age}')
    if ( 0 <= int(person.age) < 15):
        person.age = 'A01'
    elif ( 16 <= int(person.age) < 40):
        person.age = 'A02'
    elif ( 40 <= int(person.age) < 64):
        person.age = 'A03' 
    elif ( 65 <= int(person.age) < 100):
        person.age = 'A04'
    print("-->Chatbot: Hãy nhập cân nặng của bạn của bạn (kg)")
    weight = validate.validate_number(input())
    
    print("-->Chatbot: Hãy nhập chiều cao của bạn của bạn (m)")
    height = validate.validate_number(input())

    BMI = float(weight)/(float(height)*float(height))
    if ( 0 <= BMI < 18.5):
        print("-->Chatbot: Bạn thuộc dạng người gầy")
        person.bmi = 'BMI01'
    elif ( 18.5 <= BMI < 24.9):
        print("-->Chatbot: Bạn thuộc dạng người bình thường")
        person.bmi = 'BMI02'
    elif ( 24.9 <= BMI < 29.9):
        print("-->Chatbot: Bạn thuộc dạng người hơi béo")
        person.bmi = 'BMI03' 
    elif ( 29.9 <= BMI < 100):
        print("-->Chatbot: Bạn thuộc dạng người béo phì")
        person.bmi = 'BMI04'
    list_clothes.append(person.bmi)
    list_clothes.append(person.age)
    print(person)
    return(person)
    
#########################
# câu hỏi quần áo
def first_question_clothes (list_clothes, person):
    while (1):
        #sự kiện
        print("-->Chatbot: Để có thể bắt đầu tư vấn tôi cần thông tin về sự kiện bạn đi")
        count = 1
        for i in db.resultEvent:
            print  (f"{count}. {i['name']}\n")
            count+=1
        answer = validate.validate_number(input())
        if (int(answer) < 1 or int(answer) > 3):
                print('-->Chatbot: Vui lòng nhập 1 số từ 1 tới 3')
                continue
        else:
            list_clothes.append(db.resultEvent[int(answer) - 1 ]['id'])
            print(list_clothes)
        print(f"-->Chatbot: Bạn {person.name} muốn tư vấn cho sự kiên: {db.resultEvent[int(answer) - 1 ]['name']}")
        
        #dang người
        print("-->Chatbot: Tiếp đến tôi cần dáng người của bạn hãy chọn: ")
        countBdF = 1
        if (person.gender == 0):
            for i in db.resultBodyForm:
                if ( i['gender'] == 0):
                    print  (f"{countBdF}. {i['form']}\n")
                    countBdF += 1

        else:
            for i in db.resultBodyForm:
                if ( i['gender'] == 1):
                    print  (f"{countBdF}. {i['form']}\n")
                    countBdF += 1

        answerBdF = validate.validate_number(input())
        list_clothes.append(db.resultBodyForm[int(answerBdF) - 1 ]['id'])
        print(list_clothes)

        return list_clothes
    
#########################
# câu hỏi khuôn mặt và tóc
def second_question_face (list_hair, person):
    while(1):
        print("-->Chatbot: Để có thể bắt đầu tư vấn về tóc và trang điểm tôi cần một vài thông tin")
        count = 1
        for i in db.resultFace:
            print  (f"{count}. {i['face_shape']}\n")
            count +=1
        answer = validate.validate_number(input())
        if (int(answer) < 1 or int(answer) > 6):
                print('-->Chatbot: Vui lòng nhập 1 số từ 1 tới 6')
                continue
        else:
            list_hair.append(db.resultFace[int(answer) - 1 ]['id'])
            print(list_hair)
        #print(f"-->Chatbot: Bạn {person.name} có kiểu khuôn măt: {db.resultEvent[int(answer) - 1 ]['name']}")
        print(f"-->Chatbot: Bạn {person.name} có kiểu khuôn măt: {db.resultFace[int(answer) - 1 ]['face_shape']}")
        
        return list_hair


###########################
welcome_question()
first_question_clothes (list_clothes, person)
second_question_face (list_hair, person)