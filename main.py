# 파일이름 : main.py
# 작 성 자 : 고준하
import random

names = []
genders = []
scores = []
grades = []

count_members = 0

#기존에 구현되었던 기능들 함수(7개)로 분리, 매개변수 사용(set_grade, set_match_table)
#return 이용(set_grade, set_match_group), global 키워드 사용(register, delete)
def set_grade(score):
    if score >= 1500:
        return "gold"
    elif score >= 1000:
        return "silver"
    else:
        return "bronze"
    
def register():
    global count_members

    total_new = int(input("추가할 인원수를 입력하세요: "))
    for i in range(1, total_new+1):
        members = input("이름, 성별, 점수를 띄어쓰기로 구분하여 입력하세요: ").split(" ")

        name = members[0]
        gender = members[1]
        score = float(members[2])

        names.append(name)
        genders.append(gender)
        scores.append(score)
        grades.append(set_grade(score))

        count_members += 1
    print(f"회원 {total_new}명 등록 완료")

def delete():
    global count_members

    total_del = int(input("삭제할 인원수를 입력하세요: "))

    for i in range(1, total_del+1):
        name_delete = input("삭제할 회원의 이름을 입력하세요: ")
        
        if name_delete not in names:
            print(f"{name_delete}는 우리 클럽의 회원이 아닙니다")

        for i in range(len(names)):
            if names[i] == name_delete:
                names.pop(i)
                genders.pop(i)
                grades.pop(i)
                scores.pop(i)
                count_members -= 1
                break
    print(f"회원 {total_del}명 삭제 완료")

def view_mem():
    for i in range(len(names)):
        print(f"{i+1} | 이름: {names[i]} |성별: {genders[i]} | 등급: {grades[i]}")

def analyze_club():
    if count_members == 0:
        print("등록된 회원이 없습니다.")
    else:
        print(f"클럽 평균 점수: {sum(scores)/count_members:.2f} | 클럽 최고점: {max(scores)} | 클럽 최저점: {min(scores)}")

def set_match_group():
    participants = []

    match_grade = input("대진표를 작성할 등급을 입력하세요: ").lower()

    for i in range(len(names)):
        if grades[i] == match_grade:
            participants.append(names[i])
    
    random.shuffle(participants)
    return participants

def set_match_table(p):
    print("-"*30)

    if len(p) < 2:
        print("인원이 부족하여 대진표를 작성할 수 없습니다.")
    else:
        for i in range(0, len(p)-1, 2):
            print(f"{p[i]} vs {p[i+1]}: 경기{i//2 + 1}")
            print()
        
        if len(p) % 2 != 0:
            print(f"{p[-1]}:부전승")
            
    print("-"*30)

while True:
    print("1.회원등록 2.회원삭제 3.회원조회 4.클럽분석 5.대진표작성 0.종료")
    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        register()
    elif menu == "2":
        delete()
    elif menu == "3":
        view_mem()
    elif menu == "4":
        analyze_club()
    elif menu == "5":
        set_match_table(set_match_group())
    elif menu == "0":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다.")