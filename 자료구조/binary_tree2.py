import random

# 함수 선언 부분 
class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 전역 변수 선언 부분 
memory = []
root_book, root_auth = None, None
book_ary = [
    ['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'],
    ['신곡', '단테'], ['돈키호테', '세브반테스'], ['동물농장', '조지오웰'],
    ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']
]
random.shuffle(book_ary)


# 책 이름 트리 
node = TreeNode()
node.data = book_ary[0][0]
root_book = node
memory.append(node)

for book in book_ary[1:]:
    name = book[0]
    node = TreeNode()
    node.data = name

    current = root_book
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print("책 이름 트리 구성 완료!")

# 작가 이름 트리 
node = TreeNode()
node.data = book_ary[0][1]
root_auth = node
memory.append(node)

for book in book_ary[1:]:
    name = book[1]
    node = TreeNode()
    node.data = name

    current = root_auth
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print("작가 이름 트리 구성 완료!")

# 책 이름 및 작가 이름 검색 
book_or_auth = int(input('책검색(1), 작가검색(2)-->'))
find_name = input('검색할 책 또는 작가-->')

if book_or_auth == 1:
    root = root_book
else:
    root = root_auth

current = root
while True:
    if find_name == current.data:
        print(find_name, '을(를) 찾음.')
        find_yn = True
        break
    elif find_name < current.data:
        if current.left is None:
            print(find_name, '이(가) 목록에 없음')
            break
        current = current.left
    else:
        if current.right is None:
            print(find_name, '이(가) 목록에 없음')
            break
        current = current.right
