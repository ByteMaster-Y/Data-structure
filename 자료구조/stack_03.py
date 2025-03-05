# 전역 변수 선언 부분 
size = 100
stack = [ None for _ in range(size) ]
top = -1

import webbrowser
import time

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
	urls = [ 'naver.com', 'daum.net', 'nate.com']

	for url in urls :
		push(url)
		webbrowser.open('http://'+url)
		print(url, end = '-->')
		time.sleep(1)

	print("방문 종료")
	time.sleep(5)

	while True :
		url = pop()
		if url == None :
			break
		webbrowser.open('http://'+url)
		print(url, end = '-->')
		time.sleep(1)
	print("방문 종료")
