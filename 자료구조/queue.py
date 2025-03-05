# 전역 변수 선언 부분
SIZE = int(input("큐의 크기를 입력하세요 ==> "))
queue = [None for _ in range(SIZE)]
front = rear = -1

# 개선된 함수
# 큐가 꽉 찼을 때 데이터를 앞으로 이동시키는 기능을 포함
def is_queue_full():
    global SIZE, queue, front, rear
    if rear != SIZE - 1:
        return False
    elif (rear == SIZE - 1) and (front == -1):
        return True
    else:
        # rear가 끝에 도달했지만 front가 -1이 아니면: 데이터 앞으로 이동, False 반환 (공간 재활용)
        for i in range(front + 1, SIZE):
            queue[i - 1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enqueue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def dequeue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[front + 1]
    # 큐 상태 :  ['1', '2', '3']
    # 확인된 데이터 ==>  1 
    # 즉 다음번에 빠져야할 친구는 1이다.


# 메인 코드 부분
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while select != 'X' and select != 'x':
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            enqueue(data)
            print("큐 상태 : ", queue)
        elif select == 'E' or select == 'e':
            data = dequeue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
