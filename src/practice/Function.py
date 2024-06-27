# 함수에 대한 설명
# 함수의 정의와 호출
# - 어떤 일을 실행하기 위한 코드의 집합
# - 함께 사용하는 여러 개의 문장 혹은 명령어를 하나로 묶어놓은 것
# - 주어진 입력에 대해 어떤 과정을 거쳐서 출력으로 내보내는 박스
# - 동일한 함수를 여러 차례 호출 -> 코드의 재사용 가능
# - 함수의 필요성
#   - 동일한 처리 코드의 재활용
#   - 자원의 효율적인 관리
#   - 가독성 향상
#   - 프로그램 흐름 파악 & 디버깅 용이
#   - 유지보수 용이

# def (함수 생성을 의미) 예약어 사용
# 반드시 함수명 다음에 괄호()와 콜론(:) 필요 괄호() 안에는 인자값(매개변수) 부여
# 매개변수: 0개 혹은 1개 이상의 인자(입력)을 입력 받아 필요한 데이터를 전달(선언: argument, 호출: parameter)
# return: 작업의 결과를 호출한 곳으로 반환

def f(x):
    y = x + 2
    return y

i = f(5)
print(i)

### 사용자 정의 함수
# 사용자가 필요한 기능을 직접 정의하는 함수

# 매개변수 없음, 리턴 값 없음
def f():
    x = 5
    y = x + 2

print(f())

# 매개변수 없음, 리턴 값 있음
def f():
    x = 5
    y = x + 2
    return y

print(f())

# 매개변수 없음, 리턴 값 여러 개 있음
def f():
    x = 5
    y = 7
    a = x + y
    b = x - y
    return a, b

ra, rb = f()
print(ra, rb)

# 매개변수 있음, 리턴 값 없음
def f(x):
    x = 5
    y = x + 2

print(f(5))

# 매개변수 있음, 리턴 값 있음
def f(x):
    y = x + 2
    return y

print(f(5))

# 매개변수 있음, 리턴 값 여러 개 있음
def f(x, y):
    a = x + y
    b = x - y
    return a, b

rt = f(5, 7)
print(rt)

# 변수로 할당되거나 함수의 인자로 전달되는 경우
def double(x):
    return x * 2

def triple(x):
    return x * 3

y = 5
print(double(y))

def func(f):
    return f(2)

print(func(double))  # double(2)와 같은 의미

def func(f, x):
    return f(x)

ret2 = func(double, 5)
ret3 = func(triple, 2)
print(ret2, ret3)

### 매개변수의 유형
# 매개변수가 여러 개일 때 (정해놓은 인자 값, 불특정 인자 값)

# default 인자 값
# 인자값을 기본 값으로 정할 때 사용
def my_print(message='my print'):
    print(message)

my_print('hello')
my_print()  # 인자값이 없을 때 기본적으로 default message를 출력

# keyword 인자 값
# 인자에 이름을 명시해주는 방법
def full_name(first='first name을 쓰세요', last='last name이 비어있어요'):
    return first + ' ' + last

print(full_name('Lucy', 'Chun'))
print(full_name('Lucy'))  # 뒤의 인자가 없을 때 default값이 출력됨
print(full_name(last='Chun'))  # 인자 이름을 쓰지 않은 경우 default값이 출력됨

# 변수의 영역 (scope)
# - 전역변수: 함수 외부에서 선언한 변수, global variable
# - 지역변수: 함수 안에서 선언한 변수, local variable

### 지역변수와 전역변수
# 지역변수: 선언된 함수 안에서만 유효, 함수 호출이 종료되면 소멸
# 전역변수: 함수 외부에서 유효

# 지역변수 예제
def sub():
    loc = '바나나가 좋아'
    print(loc)

sub()
# print(loc)  # NameError 발생

# locals(): 함수 내에 있는 변수들의 값을 알 수 있음
def sub():
    loc = '바나나가 좋아'
    print(loc)
    print(locals())

sub()

# 전역변수 예제
glb = '사과가 좋아'

def sub():
    glb = '바나나가 좋아'
    print(glb)

sub()
print(glb)

# global 키워드: 함수 내부에서 전역 변수 값을 저장
glb = '사과가 좋아'

def sub():
    global glb
    glb = '바나나가 좋아'
    print(glb)

sub()
print(glb)
