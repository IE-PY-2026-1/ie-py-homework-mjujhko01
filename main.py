# 파일이름 : main.py
# 작 성 자 : 고준하
import random

members = []
count_members = 0

def load_data():
    global count_members

    members.clear()
    count_members = 0

    try:
        with open("members.csv", "r", encoding="utf-8") as f:
            for line in f:
                part = []

                for l in line.strip().split(","):
                    part.append(l.strip())

                if len(part) != 4:
                    print(f"{line.strip()}: 불러오기 실패")
                    continue

                try:
                    members.append([part[0], part[1], part[2], float(part[3])])
                    count_members += 1
                except ValueError:
                    print(f"{line.strip()}: 불러오기 실패")
            print("불러오기 완료")
    except FileNotFoundError:
        print("저장된 멤버 파일을 찾을 수 없습니다")

def save_data():
    with open("members.csv", "w", encoding="utf-8") as f:
        for mem in members:
            f.write(f"{mem[0]}, {mem[1]}, {mem[2]}, {mem[3]}\n")
    print("members.csv 저장완료")

def set_grade(score):
    if score >= 1500:
        return "gold"
    elif score >= 1000:
        return "silver"
    else:
        return "bronze"
    
def register():
    global count_members
    count_reg = 0

    while True:
        try:
            total_new = int(input("추가할 회원수를 입력하세요(취소: 0): "))
            if total_new == 0:
                print("메뉴로 돌아갑니다")
                return
            elif total_new < 0:
                print("양의 정수를 입력하세요")
                continue
            else:
                break
        except ValueError:
            print("정수를 입력하세요")

    for i in range(1,total_new+1):
        while True:
            try:
                member = input("이름, 성별, 점수를 띄어쓰기로 구분하여 입력하세요: ").split(" ")
                
                name = member[0]
                gender = member[1]
                score = float(member[2])
                grade = set_grade(score)

                new_mem = [name, gender, grade, score]
                members.append(new_mem)

                count_reg += 1
                count_members += 1

                break
            except (IndexError, ValueError):
                print("이름, 성별, 점수(숫자) 세 요소를 띄어쓰기로 구분하여 정확히 입력하세요")
    
    save_data()
    print(f"회원 {count_reg}/{total_new}명 등록 완료")

def delete():
    global count_members
    count_del = 0

    while True:
        try:
            total_del = int(input("삭제할 회원수를 입력하세요(취소: 0): "))
            if total_del == 0:
                print("메뉴로 돌아갑니다")
                return
            elif total_del < 0:
                print("양의 정수를 입력하세요")
                continue
            elif total_del > count_members:
                print("등록 회원수보다 더 많이 삭제할 수 없습니다")
                continue
            else:
                break
        except ValueError:
            print("정수를 입력하세요")
    for i in range(1, total_del+1):
        name_delete = input("삭제할 회원의 이름을 입력하세요: ")
        found = False
        for j in range(len(members)):
            if members[j][0] == name_delete:
                members.pop(j)
                count_del += 1
                count_members -= 1
                found = True
                break
        if not found:
            print(f"{name_delete}는 우리 클럽의 회원이 아닙니다")
    save_data()
    print(f"회원 {count_del}/{total_del} 삭제 완료")

def view_mem():
    if count_members > 0:
        for i in range(len(members)):
            print(f"{i+1} | 이름: {members[i][0]} |성별: {members[i][1]} | 등급: {members[i][2]} | 점수: {members[i][3]}")
    else:
        print("등록된 회원이 없습니다")

def analyze_club():
    scores = []
    
    if count_members == 0:
        print("등록된 회원이 없습니다.")
    else:
        for i in range(len(members)):
            scores.append(members[i][3])
        print(f"클럽 평균 점수: {sum(scores)/count_members:.2f} | 클럽 최고점: {max(scores)} | 클럽 최저점: {min(scores)}")

def set_match_group():
    participants = []

    match_grade = input("대진표를 작성할 등급을 입력하세요: ").lower()

    for i in range(len(members)):
        if members[i][2] == match_grade:
            participants.append(members[i][0])
    
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
    print("1.회원등록 2.회원삭제 3.회원조회 4.클럽분석 5.대진표작성 6.회원저장 7.회원불러오기 0.종료")
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
    elif menu == "6":
        save_data()
    elif menu == "7":
        load_data()
    elif menu == "0":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다.")