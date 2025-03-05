# 0번 인덱스는 데이터가 추가되거나 삭제되지 않는 공간으로 유지됩니다. 
# 이는 큐가 비어있는지 혹은 꽉 찼는지를 판단할 때 필요합니다.

# 함수 선언 부분
def is_queue_full():
    global SIZE, queue, front, rear
    # 조건이 참이면, 큐가 가득 찬 상태
    if ( (rear + 1) % SIZE == front):
        return True
    else:
        return False

def is_queue_empty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def enqueue(data):
    global SIZE, queue, front, rear
    if (is_queue_full()):
        print("큐가 꽉 찼습니다.")
        return
    # 이동 시 (rear + 1) % SIZE로 계산하여 원형으로 순환할 수 있게
    # 만약 rear가 1이면 2 % 5 는 rear 가 2이다.
    rear = (rear + 1) % SIZE 
    queue[rear] = data

def dequeue():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print("큐가 비었습니다.")
        return None
    # 비어 있지 않으면, front를 한 칸 앞으로 이동하고 해당 위치의 데이터를 추출한 후, 그 자리를 None으로 설정
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (is_queue_empty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % SIZE]

# 전역 변수 선언 부분 
SIZE = int(input("큐의 크기를 입력하세요 ==> "))
queue = [None for _ in range(SIZE)]
front = rear = 0

# 메인 코드 부분 
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            enqueue(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'E' or select == 'e':
            data = dequeue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
