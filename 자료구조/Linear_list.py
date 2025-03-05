# 함수 선언 부분
def add_data(friend):
    katok.append(None)
    k_len = len(katok)
    katok[k_len - 1] = friend  # 배열 길이 - 1에 추가한다.

def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None)
    k_len = len(katok)

    for i in range(k_len - 1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend  # 지정한 위치에 친구 추가

def delete_data(position):
    if position < 0 or position >= len(katok):  # 범위 체크 수정
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    k_len = len(katok)
    katok[position] = None  # 데이터 삭제

    for i in range(position + 1, k_len):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[k_len - 1])  # 마지막 요소 제거

# 전역 변수 선언 부분
katok = []
select = -1  # 1. 추가, 2. 삽입, 3. 삭제, 4. 종료

# 메인 코드 생성
while select != 4:
    select = int(input("선택하세요 (1: 추가, 2: 삽입, 3: 삭제, 4: 종료) --> "))

    if select == 1:
        data = input("추가할 데이터 --> ")
        add_data(data)
        print(katok)
    elif select == 2:
        pos = int(input("삽입할 위치 --> "))
        data = input("추가할 데이터 --> ")
        insert_data(pos, data)
        print(katok)
    elif select == 3:
        pos = int(input("삭제할 위치 --> "))
        delete_data(pos)
        print(katok)
    elif select == 4:
        print(katok)
        exit()  # 종료 함수 호출 수정
    else:
        print("1~4 중 하나를 선택하세요.")
