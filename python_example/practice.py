print("****************************************************")
print("number, float, double")
print("****************************************************")
print(5)
print(-10)
print(3.14)
print(193847191827)
print(5+3)
print(5*108)
print(3*(3+1))

#String
print("****************************************************")
print("String")
print("****************************************************")
print('풍선')
print("나비")
print("ㅎㅎㅎ"*9)

#boolean
print("****************************************************")
print("boolean")
print("****************************************************")
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

print("****************************************************")
print("변수")
print("****************************************************")
#변수
animal ="강아지"
age = 4
name = "연탄이"
hobby = "산책"
is_adult = age >= 3

print("울집 "+ animal +"의 이름은 "+ name +", "+str(age)+"살")
print(name +" " + hobby + " 을 좋아함")
print(name +" 어른일까요? " + str(is_adult))
print()
# + 말고 , 를 사용할수도있으나, , 사용시 빈칸(공백)이 하나씩꼭 들어간다.
print("울집 ", animal ,"의 이름은 ", name ,", ",age,"살")
print(name ," " + hobby , " 을 좋아함")
print(name ," 어른일까요? " , is_adult)


#주석
'''
주석은 싱글따옴표를 세개쓰면 
여러줄 주석이 된다.
'''

#quiz_1
print("****************************************************")
print("quiz_1")
print("****************************************************")
station = "사당"
print(station + " 행 열차가 들어오고있습니다")


print("****************************************************")
print("연산자")
print("****************************************************")
print(1+1)
print(3-2)
print(5*2)
print(6/2)

print(2**3)     #2^3승 계산
print(5%3)      #나머지 계산
print(5//3)     # 나머지 연산에서 몫 추출 
print(5/3)     

print(1 == 1)
print(1 != 3)
print(not(1 != 3))

print(( 3 > 0 ) and (3 < 5))
print((3 > 0 ) & (3 < 5))

print(( 3 > 0 ) or (3 > 5))
print((3 > 0 ) | (3 > 5))
print(5 > 4 > 3)
print(5 > 4 > 7)


print("****************************************************")
print("간단한 수식")
print("****************************************************")
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %=2
print(number)

print("****************************************************")
print("숫자처리 함수")
print("****************************************************")
print(abs(-5))
print(pow(4,2)) # 4^2
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4.98))

from math import *
print(floor(4.99))  # 내림
print(ceil(3.14))   # 올림
print(sqrt(16))     # 제곱근

print("****************************************************")
print("랜덤함수")
print("****************************************************")

from random import *
print(random()) #ㅁ0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10)
print(int( random() * 10 ))
print(int( random() * 10 )+1)

#lotto
print(int(random() * 45) + 1) # 1 ~ 46 미만의 임의의값 생성
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print()
print(randrange(1,46)) # 1 ~ 46 미만의 임의의값 생성
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print()
print(randint(1, 45)) # 1 ~ 45 이하의 임의의값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의값 생성

print("****************************************************")
print("quiz_2")
print("****************************************************")

study_date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+ str(study_date) +" 일로 선정되었습니다.")


print("****************************************************")
print("문자열")
print("****************************************************")
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3="""
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


print("****************************************************")
print("슬라이싱")
print("****************************************************")
jumin = "991201-1231323"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])

print("****************************************************")
print("문자열 처리함수")
print("****************************************************")
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))
print(python.split(" ")[0])

index = python.index("n")
print(index)
index = python.index("n",index + 1)
print(index)

print(python.find("n"))
print(python.find("java"))
print(python.count("n"))


print("****************************************************")
print("문자열 포맷")
print("****************************************************")
print("a" + "b")
print("a" , "b")

#방법 1
print("나는 %d 살 입니다." % 20)
print("나는 %s 를 좋아합니다." % "파이썬")
print("Apple 은 %c 로 시작해요." % "A")

print("나는 %s 살 입니다." % 20)
print("나는 %s 색과 %s 색을 좋아해요" % ("파란" , "빨간"))

#방법 2
print("나는 {} 살입니다.".format(20))
print("나는 {} 색과 {} 색을 좋아해요".format("파란","빨간"))
print("나는 {0} 색과 {1} 색을 좋아해요".format("파란","빨간"))
print("나는 {1} 색과 {0} 색을 좋아해요".format("파란","빨간"))

#방법 3
print("나는 {age} 살이며, {color} 색을 좋아해요.".format(age=20, color="빨간"))

#방법 4(v3.6~)
age = 20
color = "보라"
print(f"나는 {age} 살이며, {color} 색을 좋아해요.")



print("****************************************************")
print("탈출 문자")
print("****************************************************")
print("백문이 불여일견, 백견이 불여일타")
#\n 줄바꿈
print("백문이 불여일견, \n백견이 불여일타")

#저는 "나도 코딩" 입니다
#\" \' 문장내 따옴표
print("저는 \"나도코딩\" 입니다")

# \\ : 문장내에서 \ 하나로 표출됨
print("D:\\python_workspace")

# \r : 커서를 맨앞으로 이동
print("Red Apply \rPine")

#\b : 백스페이스
print("Redd\bApple")

#\t : tab
print("Red\tApple")


print("****************************************************")
print("quiz_3")
print("****************************************************")
# 예시 url : http://naver.com
# 규칙1 : 에서 http:// 제외 => naver.com
# 규칙2 : 처음만나는 점 (.) 이후부분은 제외
# 규칙3 : 남은 글자중 처음세자리 + 글자갯수 + 글자내'e' 갯수 + "!" 로구성
# 예) nav51!

tmp_url = "http://naver.com"
ex1 = tmp_url[7:]
print(ex1)
print(ex1[:ex1.find(".")])
print(ex1[:3] + str(len(ex1[:ex1.find(".")])) + str(ex1.count('e')) + "!")
password = ex1[:3] + str(len(ex1[:ex1.find(".")])) + str(ex1.count('e')) + "!"
print("{0} 사이트의 비밀번호는 {1} 입니다.".format(tmp_url,password))

print("****************************************************")
print("list")
print("****************************************************")
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)
subway = ["유재석","조세호","박명수"]
print(subway)
print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1,"정형돈")
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [2,4,5,1,6]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#num_list.clear()
#print(num_list)

mix_list=["조세호",20,True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)


print("****************************************************")
print("사전")
print("****************************************************")

cabinet={3:"유재석",100:"김태호"}
print(cabinet)
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print(cabinet.get(5))
print(cabinet.get(5,"사용가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet2={"A-3":"유재석","B-100":"하하"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

del cabinet2["A-3"]
print(cabinet2)
print(cabinet2.keys())
print(cabinet2.values())
print(cabinet2.items())

cabinet2.clear();
print(cabinet2)

print("****************************************************")
print("튜플")
print("****************************************************")
# 값의 추가나 삭제가 불가능함.
menu = ("돈까스","치즈돈까스")
print(menu[0])
print(menu[1])

(name, age, hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)

print("****************************************************")
print("세트(set)")
print("****************************************************")
#중복이 안되며, 순서가 없다.
my_set = {1,2,3,3,3,3}
print(my_set)

java_user = {"유재석","김태호","양세형"}
python_user = set(["유재석","박명수"])

#교집합
print(java_user & python_user)
print(java_user.intersection(python_user))

#합칩합
print(java_user | python_user)
print(java_user.union(python_user))

#차집합
print(java_user - python_user)
print(java_user.difference(python_user))
python_user.add("김태호")

print(python_user - java_user)
print(python_user.difference(java_user))
java_user.remove("김태호")

print("****************************************************")
print("자료구조")
print("****************************************************")

menu_tea = {"커피","주스","우유"}
print(menu_tea , type(menu_tea))

menu_tea = list(menu_tea)
print(menu_tea, type(menu_tea))

menu_tea = tuple(menu_tea)
print(menu_tea, type(menu_tea))

menu_tea = set(menu_tea)
print(menu_tea, type(menu_tea))


print("****************************************************")
print("quiz_4")
print("****************************************************")
#조건1 : 20명이 작성 아이디는 20개
# 무작위추첨 및 중복불가
# 1위 치킨, 3명은 커피쿠폰
# random 의 shuffle 과 sample 활용

from random import * 
user_list = range(1,21)
user_list = list(user_list) # 형변환
print(f"현재 아이디는 다음 {user_list} 과 같습니다.")
print("shuffle")
shuffle(user_list)
print(user_list)
winners = sample(user_list,4)
print("치킨당첨자는 {0} 입니다.".format(winners[0]))
print("커피당첨자는 {0} 입니다.".format(winners[1:]))

print("****************************************************")
print("if")
print("****************************************************")
#if 조건 : 
#    실행 명령문
#elif 조건 :
#   실행 명령문
#else:
#   실행명령문
'''
weather = input("오늘날씨는 어때요?")
if weather == "비" or weather=="눈":
    print("우산을 챙기세요")
    print("짜증나111")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
    print("짜증나")
else:
    print("날씨 맑음")


temp_ondo = int(input("기온이 몇도인가요?"))
if 30 < temp_ondo:
    print("너무 더워요")
elif 10 <= temp_ondo <= 30 :
    print("날씨가 좋아요")
elif 0 <= temp_ondo < 10:
    print("외투를 챙겨요")
else:
    print("너무추워요")
'''

print("****************************************************")
print("for")
print("****************************************************")
waiting_list = [1,2,3,4,5,6,7]
for waiting_num in waiting_list:
    #print("대기번호 : {0}".format(waiting_num))
    print(f"대기번호 : {waiting_num}")


startbucks=["아이언맨","토르","아이엠그루트"]
for customer in startbucks:
    print(f"{customer} 님 커피가 준비되었습니다.")

print("****************************************************")
print("while")
print("****************************************************")
customer_1 = "토르"
index = 5
while index >=1 :
    print(f"{customer_1} 님 커피가 준비되었습니다. {index} 번 남았습니다.")
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")


print("****************************************************")
print("continue, break")
print("****************************************************")

absent = [2, 5]
no_book = [7]
for student_cb in  range(1,11):
    if student_cb in absent:
        continue
    elif student_cb in no_book:
        print(f"오늘수업 끝. {student_cb} 는 교무실로 따라와")
        break
    print(f"{student_cb} , 책을 읽어봐")


print("****************************************************")
print("한줄포문")
print("****************************************************")

student_o_f_num = range(1,6)
print(student_o_f_num)
student_o_f_num = [i+100 for i in student_o_f_num]
print(student_o_f_num)

student_o_f_name = ["Iron Man","Thor","I am Groot"]
print(student_o_f_name)
#student_o_f_name = [len(i) for i in student_o_f_name]
#print(student_o_f_name)
student_o_f_name = [i.upper() for i in student_o_f_name]
print(student_o_f_name)
student_o_f_name = [i.lower() for i in student_o_f_name]
print(student_o_f_name)

print("****************************************************")
print("quiz_5")
print("****************************************************")
# 50명의 승객과 매칭기회가 있을때, 총 탑승 승객의 수를 구하는 프로그램
# 조건 1 : 승객별 운행 소요시간은 5~50 분 사이의 난수로 정해짐
# 조건 2 : 소요시간 5~15분 사이의 승객만 매칭해야한다.
# 출력문 예제  [성공여부] i 번째 손님 ( 소요시간 : ~~분)

count = 0
for taxi_num in range(1,51) : 
    drive_time  = randint(5, 50)
    if  5 <= drive_time <= 15:
        print(f"[O] {taxi_num} 번째 손님 (소요시간 : {drive_time} )") 
        count += 1
    else:     
        print(f"[ ] {taxi_num} 번째 손님 (소요시간 : {drive_time} )")
    
print(f"오늘 손님은 {count} 명입니다.")  


print("****************************************************")
print("함수")
print("****************************************************")

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance + money} 입니다.")
    return balance+money

def withdraw(balance,money):
    if balance >= money:
        print(f"출금이 완료 되었습니다. 잔액은 {balance-money} 원입니다.")
        return balance - money
    else:
        print(f"출금이 완료되지않았습니다. 잔액은 {balance} 입니다.")
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance  - money - commission

balance = 0
balance = deposit(balance,2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print(f"수수료는 {commission} 이며, 잔액은 {balance} 입니다.")
print(balance)

print("****************************************************")
print("기본값")
print("****************************************************")

def profile(name, age=17, main_lang="python"):
    print(f"이름 : {name} \t 나이 : {age} \t 주 사용언어 : {main_lang} ")

profile("유재석")
profile("김태호")

print("****************************************************")
print("키워드값")
print("****************************************************")

def profile_1(name, age, main_lang):
    print(f"이름 : {name} \t 나이 : {age} \t 주 사용언어 : {main_lang} ")

profile_1(name="유재석",main_lang="python",age=20)
profile_1(name="김태호",age=25, main_lang="java")

print("****************************************************")
print("가변인자")
print("****************************************************")

def profile_2(name, age, *language):
    print(f"이름 : {name} \t 나이 : {age} \t".format(),end=" ")
    for lang in language :
        print(lang, end=" ")
    print()

profile_2("유재석",20,"python","java","c","rdb")
profile_2("김태호",20,"swift","kotlin")


print("****************************************************")
print("지역/전역변수")
print("****************************************************")

gun=10

def checkpoint(soldiers):
    #전역변수 쓰는법
    global gun
    gun = gun - soldiers
    print(f"함수내 남은총 : {gun}")

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print(f"check point 내 총의수 : {gun}")
    return gun

print(f"전체 총수 : {gun}")
#checkpoint(2)
gun = checkpoint_ret(gun,2)
print(f"이후 남은총 : {gun}")

print("****************************************************")
print("quiz_6")
print("****************************************************")
# 표준체중을 구하는 프로그램 작성
# * 표준체중 : 개인의 키에 적당한 체중
# 성별에 따른 공식(m : 미터단위)
#  남자 : 키(m) * 키(m) * 22
#  여자 : 키(m) * 키(m) * 21

# 조건 1 : 표준체중은 별도의 함수 내에서 계산
#       - 함수명 : std_weight
#       - 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준체중은 소수점 둘째자리까지 표시
# 출력예제 : 키 175 cm 남자의 표준체중은 67.38 Kg 입니다.


def std_weight(height, gender):
    gender_val = 0
    if gender == "남자":
        gender_val = 22
    else :
        gender_val = 21

    std_weight = (height*0.01) * (height*0.01) * gender_val

    print(f"키 {height} cm {gender}의 표준 체중은 {round(std_weight,2)} Kg 입니다.")

man_height = 175
girl_height = 160

std_weight(man_height,"남자")
std_weight(girl_height,"여자")

    
print("****************************************************")
print("표준 입출력")
print("****************************************************")
print("python", "java")
print("python", "java", sep=",")
print("python", "java","javascript", sep=",")
print("python", "java", sep=" vs ")

print("python", "java", sep="," , end="?")
print("무엇이 더 잼있을까요?")

import sys
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)

scores={"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():
    print(subject, score)
    
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기 순번표
# 001, 002, 003, ...

for num in range(1,21):
    print(f"대기번호 : {str(num).zfill(3)}")

#test_answer = input("아무값이나 입력하세요 :")
#print(type(test_answer))
#print(f"입력하신 값은 {str(test_answer)} 입니다")

print("****************************************************")
print("다양한 출력 포맷")
print("****************************************************")
# 빈자리는 공란, 오른쪽 정렬, 10자리 공간
print(f"{0: >10}500")
print("{0: >10}".format(500))

# 양수일땐 +, 음수일땐 - 표기
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽정렬, 빈칸을 _ 채움
print("{0:_<+10}".format(500))

# 3자리 ,
print(f"{0:,}10000000000")
print("{0:,}".format(100000000000))
# 3자리 , +,- 부호입력
print(f"{0:+,}10000000000")
print("{0:+,}".format(100000000000))

# 3자리 , 부호, 자릿수 확보 빈자리는 ^ 채우기
print("{0:^<+30,}".format(10000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 2자리 출력
print("{0:.2f}".format(5/3))

print("****************************************************")
print("파일 입출력")
print("****************************************************")
#score_file = open("score.txt","w",encoding="utf-8")
#print("수학 : 0",file=score_file)
#print("영어 : 50",file=score_file)
#score_file.close()

#score_file = open("score.txt","a",encoding="utf-8")
#score_file.write("과학 : 80")
#score_file.write("\n코딩 : 100")
#score_file.close()

score_file = open("./python_example/score.txt","r",encoding="utf-8")
print(score_file.read())
score_file.close()

score_file = open("./python_example/score.txt","r",encoding="utf-8")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline())
score_file.close()

score_file = open("./python_example/score.txt","r",encoding="utf-8")

while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

score_file = open("./python_example/score.txt","r",encoding="utf-8")
for_lines = score_file.readlines()
for line in for_lines:
    print(line,end="")
score_file.close()

print("****************************************************")
print("pickle")
print("****************************************************")
import pickle
#profile_file = open("profile.pickle","wb")
#profile_data = {"이름":"박명수","나이":30 , "취미":["축구","골프","코딩"]}
#print(profile_data)
#pickle.dump(profile_data,profile_file)
#profile_file.close()

profile_file = open("./python_example/profile.pickle","rb")
profile_get_data = pickle.load(profile_file)
print(profile_get_data)
profile_file.close()

print("****************************************************")
print("with")
print("****************************************************")
with open("./python_example/profile.pickle","rb") as profile_with_file:
    print(pickle.load(profile_with_file))

#with open("study.txt","w", encoding="utf8") as study_file:
#    study_file.write("파이썬을 열심히 공부하고 있습니다.")

with open("./python_example/study.txt","r", encoding="utf8") as study_file:
    print(study_file.read())

print("****************************************************")
print("quiz_7")
print("****************************************************")
# 조건 1 : 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
#         보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고
# 부서 :
# 이름 : 
# 업무요약 :

# 1주차 부터 50주차 까지의 보고서 파일을 만드는 프로그램
max_val = 51

for i in range(1,max_val):
    with open(f"./python_example/quiz7/{i}_주차.txt","w",encoding="utf8") as bogoser_file:
        bogoser_file.write(f"""
        # - {i} 주차 주간보고 -
        #   부서 : 개발부서
        #   이름 : 김대훈
        #   업무요약 : 개발중
        """)
    
print("****************************************************")
print("class")
print("****************************************************")

#t_name = "마린"
#t_hp = 40
#t_damage = 5

#print(f"{t_name} 유닛이 생성되었습니다.")
#print(f"체력은 {t_hp} , 공격력은 {t_damage}")

#t_tank_name = "탱크"
#t_tank_hp = 150
#t_tank_damage = 35

#print(f"{t_tank_name} 유닛이 생성되었습니다.")
#print(f"체력은 {t_tank_hp} , 공격력은 {t_tank_damage}")

#def attack(name, location, damage):
#    print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage} ]")

#attack(t_name,"1시",t_damage)
# attack(t_tank_name,"1시",t_tank_damage)

class Unit:
    def __init__(self, name, hp , speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 유닛이 생성되었습니다.")

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")
       
class AttackUnit(Unit): #()안에 있는 class 호출

    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속된 class 생성자 호출
        self.damage = damage
        print(f"체력 {self.hp}, 공격력 {self.damage}")

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}] ")

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린", 40, 1, 5)

    def stimpack (self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")


class Tank(AttackUnit):
    seize_developed = False
    
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 10, 30)
        self.seize_mode = False;

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환 합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f"{self.name} : 시즈모드를 해제 합니다.")
            self.damage /= 2
            self.seize_mode = False

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print(f"{self.name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}] ")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage,)
        Flyable.__init__(self,flying_speed)
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

    def move(self, location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드를 해제 합니다..")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드를 설정 합니다.")
            self.seize_mode = True

# marine1 = AttackUnit("마린",40,5)
# marine2 = AttackUnit("마린",40,5)

# tank1 = AttackUnit("탱크",150,35)


print("****************************************************")
print("__init__")
print("****************************************************")
# 파이썬에서 쓰이는 생성자


print("****************************************************")
print("멤버변수")
print("클래스 내에 정의된 함수, self 를 통해서 접근")
print("****************************************************")
# wraith1 = AttackUnit("레이스",80,5)
# print(f"유닛이름 : {wraith1.name} , 공격력 : {wraith1.damage}")

# wraith2 = AttackUnit("레이스", 80 , 5)
# #클래스 외부에서 확장이 가능하다.
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print(f"{wraith2.name} 은 현재 클로킹 상태입니다.")

print("****************************************************")
print("메소드")
# AttackUnit 클래스 생성  attack, dameged 메소드 추가
print("****************************************************")

# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")
# firebat1.demaged(25)
# firebat1.demaged(25)


print("****************************************************")
print("상속")
print("****************************************************")

# 아래와 같은 형태로 사용      
# class AttackUnit(Unit): #()안에 있는 class 호출

#   def __init__(self, name, hp, damage):
#        Unit.__init__(self, name, hp) # 상속된 class 생성자 호출
#        self.damage = damage
#        print(f"{self.name} 유닛이 생성되었습니다.")
#        print(f"체력 {self.hp}, 공격력 {self.damage}")


print("****************************************************")
print("다중상속")
print("****************************************************")
# FlyableAttackUnit, Flyable 클래스 참조
valkyrie1 = FlyableAttackUnit("발키리",200,6,5)
valkyrie1.fly(valkyrie1.name,"3시")



print("****************************************************")
print("메소드 오버라이딩")
print("****************************************************")
vulture = AttackUnit("벌쳐", 80, 10, 20)

battleCruiser = FlyableAttackUnit("배틀크루저" , 500, 25, 3)

vulture.move("11시")
battleCruiser.move("9시")



print("****************************************************")
print("pass")
print("****************************************************")
class buildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self,name, hp, 0)
        super().__init__(name, hp, 0)
        self.locaion = locaion

print("****************************************************")
print("super")
print("****************************************************")




print("****************************************************")
print("starcraft example")
print("****************************************************")
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()

#Unit 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

#공격모드 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군공격
for unit in attack_units:
    unit.attack("1시")

# 전군피해
for unit in attack_units:
    unit.damaged(randint(5,20))


game_over()



print("****************************************************")
print("quiz_8")
print("****************************************************")
# 부동산 프로그램 작성
# 출력예제
# 총 3대의 매물이 있습니다.
# 1) 강남 아파트 매매 10억 2010년
# 2) 마포 오피스텔 전세 5억 2007년
# 3) 송파 빌라 월세 500/50 2000년

# 코드
class House:
    #매물초기화
    def __init__(self, locaion, house_type, deal_type, price, completion_year):
        self.locaion = locaion
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(f"{self.locaion} {self.house_type} {self.deal_type} {self.price} {self.completion_year} 년")


house1 = House("강남", "아파트",  "매매",  "10억", 2010)
house2 = House("마포", "오피스텔",  "전세",  "5억", 2007)
house3 = House("송파", "빌라",  "월세",  "500/50", 2000)

house_list =[]
house_list.append(house1)
house_list.append(house2)
house_list.append(house3)

print(f"총 {len(house_list)} 대의 매물이 있습니다.")
for house_unit in house_list:
    
    
    house_unit.show_detail()

print("****************************************************")
print("예외처리")
print("****************************************************")
# try:
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError as err:
#     print("숫자만 입력 가능합니다.")
#     print(err)
# except ZeroDivisionError as err :
#     print(err)
# except Exception as err:
#     print("알수없는 에러가 발생하였습니다.")
#     print(err)


print("****************************************************")
print("에러 발생시키기")
print("****************************************************")

#사용자 정의 에러
# class BigNumberError(Exception):
#     def __init__(self , msg):
#         self.msg = msg
        
#     def __str__(self):
#         return self.msg

# try:
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num >= 10 or num2 >= 10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError as err:
#     print("한자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("사용자 정의 에러 : 한자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해주셔서 감사합니다.")



print("****************************************************")
print("quiz_9")
print("****************************************************")
# 치킨집 자동주문시스템 제작
# 1 보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError 로 처리
#   출력 메세지 : "잘못된 값을 입력 하였습니다."
# 2 대기손님이 주문할수 있는 총 치킨량은 10마리로 한정
#   치킨 소진시 사용자 정의 에러(SoldOutError) 를 발생시키고, 프로그램 종료
#   출력 메시지 : "재고가 소진되어 더이상 주문을 받지 않습니다."

#chicken = 10
chicken = 0
waiting = 1

class SoldOutError(Exception):
    def __init__(self , msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg


while(True):
    try:
        print(f"[남은치킨 : {chicken}]")
        if chicken > 0 :
            order = int(input("치킨 몇마리 주문 하시겠습니까?"))
            if order < 1 :
                raise ValueError

            if order > chicken:
                print("재료가 부족합니다.")
            else:
                print(f"[대기번호 {waiting}] {order} 마리 주문이 완료되었습니다.")
                waiting += 1
                chicken -= order
        else:
            raise SoldOutError(f"[현재 주문가능 치킨 재고량 : {chicken}]")
            
    except ValueError as err:
        print("잘못된 값을 입력 하였습니다.")
        print(err)
    except SoldOutError as err:
        print("재고가 소진되어 더이상 주문을 받지 않습니다.")
        print(err)
        break

print("****************************************************")
print("모듈")
print("****************************************************")
# import 구문
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(10)

# import alias
# import theater_module as tm
# tm.price_soldier(3)

# from import 구문
#from theater_module import *
#price_morning(30)

# from import 구문 이후, 특정 함수만 가져오기
#from theater_module import price,price_morning
#price_morning(3)

# from import 구문 이후, 특정 함수 alias
from theater_module import price_soldier as ps
ps(4)

print("****************************************************")
print("패키지")
print("****************************************************")
# import 구문사용시 클래스나 함수는 import 가 불가하다.
# 패키지명.py 파일명으로 작성
# import travle.thailand 
# trip_to = travle.thailand.ThailandPackage()
# trip_to.detail()

from travle.thailand import ThailandPackage
trip_to1 = ThailandPackage()
trip_to1.detail()

from travle import vietnam
trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()

print("****************************************************")
print("__all__")
print("****************************************************")
# tavle > __init__ 에서  py 접근권한 신청
from travle import *
trip_to3 = thailand.ThailandPackage()
trip_to3.detail()
trip_to4 = vietnam.VietnamPackage()
trip_to4.detail()


print("****************************************************")
print("패키지 , 모듈위치")
print("****************************************************")
import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))

print("****************************************************")
print("내장함수")
print("****************************************************")
# language = input("무슨언어를 좋아하세요?")
# print(f"{language} 는 아주 좋은 함수입니다.")

# dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고있는지 표시
#print(dir())
print(dir(random))

lst = [1,2,3]
print(dir(lst))

print("****************************************************")
print("외장함수")
print("****************************************************")
#glob : 경로내 파일/ 폴더 조회
#import glob
#print(glob.glob("*.py"))

#os : 운영체제에서 제공하는 기본기능
# import os
# print(os.getcwd()) # 현재경로 표시
# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더")
#     os.rmdir(folder)
#     print(f"{folder} 를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(("폴더를 생성 하였습니다."))

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날자는 : ", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은 : ", today+td)

print("****************************************************")
print("퀴즈10")
print("****************************************************")
# 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건1 : 모듈파일명은 byme.py 로 작성

#(모듈사용예제)
# 이 프로그램은 나도코딩에 의해 만들어 졌습니다.
# 유튜브 : http://www.youtube.com
# email : hoonpig@nate.com

import byme as byme

byme_tmp = byme.Byme()
byme_tmp.sign()
