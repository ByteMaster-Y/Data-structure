# 스택을 활용한 괄호 매칭 검사 구현
# 전역 변수 선언 부분 
size = 100
stack = [ None for _ in range(size) ]
top = -1

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

def check_bracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    if is_stack_empty():
        return True
    else:
        return False

# 메인 코드 부분 
if __name__ == "__main__" :
    expr_ary = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']
    for expr in expr_ary:
        top = -1
        print(expr, '=>', check_bracket(expr))
	