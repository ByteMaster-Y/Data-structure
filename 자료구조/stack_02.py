# 전역 변수 선언 부분 
size = int(input("스택의 크기를 입력하세요 ==> "))
stack = [ None for _ in range(size) ]
top = -1 # 처음 초기값

def is_stack_full():
	global size, stack, top
	if (top >= size-1) :
		return True
	else :
		return False

def is_stack_empty():
	global size, stack, top
	if (top == -1) :
		return True
	else :
		return False

def push(data):
	global size, stack, top
	if (is_stack_full()) :
		print("스택이 꽉 찼습니다.")
		return
	top += 1
	stack[top] = data

def pop():
	global size, stack, top
	if (is_stack_empty()) :
		print("스택이 비었습니다.")
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

# 스택에서 top 위치의 데이터를 확인하는 함수
def peek():
	global size, stack, top
	if (is_stack_empty()) :
		print("스택이 비었습니다.")
		return None
	return stack[top]

# 메인 코드 부분 
if __name__ == "__main__" :
	select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	while (select != 'X' and select != 'x') :
		if select=='I' or select =='i' :
			data = input("입력할 데이터 ==> ")
			push(data)
			print("스택 상태 : ", stack)
		elif select=='E' or select =='e' :
			data = pop()
			print("추출된 데이터 ==> ", data)
			print("스택 상태 : ", stack)
		elif select=='V' or select =='v' :
			data = peek()
			print("확인된 데이터 ==> ", data)
			print("스택 상태 : ", stack)
		else :
			print("입력이 잘못됨")

		select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	print("프로그램 종료!")
