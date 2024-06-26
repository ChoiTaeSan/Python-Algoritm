# 튜플(Tuple)에 대한 특징과 설명
# - 리스트는 대괄호[]로 생성, 튜플은 소괄호()로 생성
# - 튜플은 소괄호() 생략 가능
# - 튜플은 함수의 리턴 값에 많이 사용(여러 개의 값을 리턴 가능)
# - 튜플을 만들기 위해 각 요소사이에 ,를 넣는다.
# - 한 개의 요소인 경우 요소의 값, ( ,를 하지 않으면 변수로 인식)
# - 튜플은 수정할 수 없음

# 튜플을 사용하는 이유
# - 더 적은 메모리 공간을 사용
# - 읽기 전용이므로 데이터가 실수로 손상될 염려가 없음
# - 튜플을 딕셔너리 키로 사용 가능
# - 리스트보다 간단한 구조라서 성능이 빠름

### 튜플 타입 확인하기

t1 = (10, 20, 30)
print(t1)  # 튜플 출력
print(type(t1))  # 타입 확인

t1 = 10, 20, 30
print(t1)  # 튜플 출력
print(type(t1))  # 타입 확인

t0 = (10)  # 정수형 변수
t1 = (10,)  # 튜플
t2 = 10,  # 튜플
print(t0, t1, t2)  # 변수와 튜플 출력
print(type(t0), type(t1), type(t2))  # 타입 확인

a = 10
b = 20
a, b = b, a  # 튜플을 사용한 값 교환
print(a, b)  # 값 교환 후 출력

### 다양한 튜플 생성

a = (38, 21, 53, 62, 19)  # 정수형 튜플
b = 38, 21, 53, 62, 19  # 정수형 튜플 (소괄호 생략)
person = ('james', 17, 17.5, True)  # 다양한 자료형을 포함한 튜플
tu1 = ('james', [1, 2, 3], True)  # 리스트를 포함한 튜플

print(a)
print(b)
print(person)
print(tu1)

# 튜플은 변경 불가능
# tu1[0] = 'Tom'  # 에러 발생

### 튜플의 연산

tu1 = (10, 20, 30)
tu2 = (40, 50, 60)
tu3 = tu1 + tu2  # 튜플 결합
print(tu3)
print(f'tu3의 길이는 {len(tu3)}')

tu1 = (10, 20, 30)
print(id(tu1))  # 튜플의 ID 확인
tu1 = tu1 * 3  # 튜플 반복
print(id(tu1))  # 새로운 튜플의 ID 확인
print(tu1)

### 튜플 항목 확인

t1 = (10, 20, 30, 40, 50)
print(t1[0])  # 첫 번째 요소
print(t1[0] + t1[1] + t1[2])  # 첫 세 요소의 합

print(t1[0:2])  # 슬라이싱: 인덱스 0부터 1까지
print(t1[1:])  # 슬라이싱: 인덱스 1부터 끝까지
print(t1[:3])  # 슬라이싱: 처음부터 인덱스 2까지

### 튜플의 값 변경
# 튜플은 내부 요소의 값을 변경할 수 없다.
# 변경해야 할 경우에는 리스트로 형변환 한 후 변경한다

mytuple = (1, 2, 3, 4, 5)
mylist = list(mytuple)  # 튜플을 리스트로 변환

mylist.append(60)  # 리스트에 요소 추가
mytuple = tuple(mylist)  # 리스트를 다시 튜플로 변환
print(mytuple)  # 변경된 튜플 출력
