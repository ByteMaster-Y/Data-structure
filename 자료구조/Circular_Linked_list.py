# 클래스와 함수 선언 부분 
class Node:
    def __init__(self):
        self.data = None
        self.link = None

# 원형 연결리스트 생성 -> ["다현", "정연", "쯔위", "사나", "지효"]
def print_nodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

# 노드 삽입 함수
def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        last = head  # 마지막 노드를 첫 번째 노드로 우선 지정
        while last.link != head:  # 마지막 노드를 찾으면 반복 종료
            last = last.link  # last를 다음 노드로 변경
        last.link = node  # 마지막 노드의 링크에 새 노드 지정
        head = node
        return

    current = head
    while current.link != head:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()  # 마지막 노드 삽입
    node.data = insert_data
    current.link = node
    node.link = head

# 노드 삭제 함수
def delete_node(delete_data):
    global head, current, pre

    if head.data == delete_data:  # 첫 번째 노드 삭제
        current = head
        head = head.link
        last = head
        while last.link != current:  # 마지막 노드를 찾으면 반복 종료
            last = last.link  # last를 다음 노드로 변경
        last.link = head  # 마지막 노드의 링크에 head가 가리키는 노드 지정
        del(current)
        return

    current = head  # 첫 번째 외 노드 삭제
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_data:  # 중간 노드를 찾았을 때
            pre.link = current.link
            del(current)
            return

# 노드 검색 함수
def find_node(find_data):
    global head, current, pre

    current = head
    if current.data == find_data:
        return current
    while current.link != head:
        current = current.link
        if current.data == find_data:
            return current
    return Node()  # 빈 노드 반환

# 전역 변수 선언 부분
head, current, pre = None, None, None
delete_array = ["다현", "정연", "쯔위", "사나", "지효"]

# 메인 코드 부분 
if __name__ == "__main__":

    node = Node()
    node.data = delete_array[0]  # 첫 번째 노드
    head = node
    node.link = head

    for data in delete_array[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    print_nodes(head)

    insert_node("다현", "화사")
    print_nodes(head)

    insert_node("사나", "솔라")
    print_nodes(head)

    insert_node("재남", "문별")
    print_nodes(head)

    delete_node("다현")
    print_nodes(head)

    delete_node("쯔위")
    print_nodes(head)

    delete_node("지효")
    print_nodes(head)

    delete_node("재남")
    print_nodes(head)

    f_node = find_node("솔라")
    print(f_node.data)

    f_node = find_node("문별")
    print(f_node.data)
