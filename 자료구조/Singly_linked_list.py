# 클래스와 함수 선언 부분 
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def insertNode(find_data, insert_data) :
	global memory, head, current, pre

	if head.data == find_data :      # 첫 번째 노드 삽입
		node = Node()
		node.data = insert_data
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == find_data :
			node = Node()
			node.data = insert_data
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insert_data
	current.link = node

def deleteNode(delete_data) :
	global memory, head, current, pre

	if head.data == delete_data :         # 첫 번째 노드 삭제
		current = head
		head = head.link
		del(current)
		return

	current = head                          # 첫 번째  외 노드 삭제
	while current.link != None :
		pre = current
		current = current.link
		if current.data == delete_data :
			pre.link = current.link
			del(current)
			return

def find_node(find_data) :
	global memory, head, current, pre

	current = head
	if current.data == find_data :
		return current
	while current.link != None :
		current = current.link
		if current.data == find_data :
			return current
	return Node()	# 빈 노드 반환

# 전역 변수 선언 부분 
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

# 메인 코드 부분 
if __name__ == "__main__" :

	node = Node()			# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :		# 두 번째 노드부터
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	print_nodes(head)

	f_node = find_node("다현")
	print(f_node.data)

	f_node = find_node("쯔위")
	print(f_node.data)

	f_node = find_node("재남")
	print(f_node.data)
