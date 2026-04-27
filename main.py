# 파일이름 : main.py
# 작 성 자 : 고준하

name = []
gender = []
score = []
grade = []

count_members = 0 #변수(리스트 & 정수)
count_new = int(input("신규 등록할 인원수를 입력하세요: ")) #int 형변환

if not(count_new > 0): #논리연산자(not), 관계연산자(>) 사용
    print("오류: 양의 정수를 입력하세요")
else:
    for i in range(count_new):
        if count_new > 1: #중첩if 사용
            print(f"{i+1}번째 회원 입력")
            name_new = input("이름: ")
            gender_new = input("성별: ")
            score_new = float(input("초기 점수: ")) #변수(문자열 & 실수), float 형변환
        elif count_new == 1:
            name_new = input("이름")
            gender_new = input("성별: ")
            score_new = float(input("초기 점수: "))

        if score_new >= 1500:
            grade_new = "gold"
        elif score_new >= 1000:
            grade_new = "silver"
        else:
            grade_new = "bronze" #for문 내의 다중if 이용한 필터링

        name.append(name_new)
        gender.append(gender_new)
        grade.append(grade_new)
        score.append(score_new) #3개 이상 input 후 list 추가(append)

        count_members += 1 #복합대입연산자 사용

name_delete = input("삭제할 회원의 이름을 입력하세요: ")
if name_delete not in name: #논리연산자 not 사용, 독립 if 사용
    print(f"{name_delete}는 우리 클럽의 회원이 아닙니다.")

for i in range(len(name)): #len()사용
    if name[i] == name_delete:
        name.pop(i)
        gender.pop(i)
        grade.pop(i)
        score.pop(i)
        count_members -= 1
        break #break 사용

if count_members > 0:
    print(f"클럽 평균 점수: {sum(score)/count_members} | 클럽 최고점: {max(score)} | 클럽 최저점: {min(score)}")
    #sum(), max(), min() 사용
for i in range(len(name)):
    print(f"{i+1} | 이름: {name[i]} | 성별: {gender[i]} | 등금: {grade[i]}")