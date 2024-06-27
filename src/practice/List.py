# 리스트(List)에 대한 특징과 설명
# - 여러 개의 자료를 하나의 변수에 저장하여 사용하고 관리한다.
# - 여러 가지 자료를 저장할 수 있는 목록으로 [] 안에 자료를 넣으며, 내부 요소는 ','로 구분한다.
# - 리스트 안에 들어가는 여러 가지 자료를 요소(element)라고 한다.
# - 각각의 요소는 유의미한 순서를 갖는다.
# - 0부터 순서대로 번호를 붙여 사용하고 이것을 인덱스(index)라고 부른다. (리스트[인덱스])
# - 숫자, 문자열, 불린 등의 기본 자료형 여러 개를 하나의 리스트에 저장할 수 있다.

# 리스트 생성 예제
num_list = []
hap = 0
for i in range(4):
    num_list.append(int(input(f'{i+1}번째 숫자를 입력하세요: ')))
    hap += num_list[i]
print(f"합계: {hap}")

# 리스트 항목 추가
a = [4, 3]
a.append(1)  # 맨 뒤에 요소 1 추가
a.append(2)  # 맨 뒤에 요소 2 추가
print(f"append 후: {a}")

a.insert(2, 5)  # 인덱스 2에 요소 5 삽입
print(f"insert 후: {a}")

a.extend([10, 20])  # 리스트에 [10, 20] 확장
print(f"extend 후: {a}")

# 리스트 수정
a[0] = 100  # 인덱스 0의 값을 100으로 수정
print(f"수정 후: {a}")

# 리스트 삭제
a.remove(2)  # 값 2를 삭제
print(f"remove 후: {a}")

a.pop()  # 마지막 요소 삭제
print(f"pop 후: {a}")

del a[1]  # 인덱스 1의 요소 삭제
print(f"del 후: {a}")

# 리스트 합치기
food1 = ['라면', '짬뽕', '짜장']
food2 = ['콜라', '사이다']
food3 = food1 + food2  # 두 리스트 합치기
print(f"합친 리스트: {food3}")

# 리스트 반복하기
food4 = food1 * 3  # 리스트 반복
print(f"반복된 리스트: {food4}")

# 리스트 인덱싱 및 슬라이싱
fruit = [2, True, 'red', 'blue', 'green', 'yellow']
fruit[-1] = 'purple'  # 인덱스 -1의 요소 변경
print(f"변경된 리스트: {fruit}")

sliced_fruit = fruit[0:2]  # 슬라이싱: 인덱스 0부터 1까지
print(f"슬라이싱 결과: {sliced_fruit}")

# 리스트 메소드 사용 예제
lst = [10, 20, 30, 40, 10, 20, 40, 60, 30, 10]
print(f"10의 개수: {lst.count(10)}")  # 요소 10의 개수 반환
print(f"30의 인덱스: {lst.index(30)}")  # 요소 30의 인덱스 반환

lst.reverse()  # 리스트 반전
print(f"반전된 리스트: {lst}")

lst.sort()  # 리스트 정렬
print(f"정렬된 리스트: {lst}")

lst.sort(reverse=True)  # 리스트 내림차순 정렬
print(f"내림차순 정렬된 리스트: {lst}")

print(f"최대값: {max(lst)}")  # 리스트의 최대값
print(f"최소값: {min(lst)}")  # 리스트의 최소값
print(f"합계: {sum(lst)}")  # 리스트의 합계

# 얕은 복사와 깊은 복사
a = [2, 5]
b = a  # 얕은 복사
a.append(7)
print(f"얕은 복사 후: a={a}, b={b}")

d = a.copy()  # 깊은 복사
a.append(8)
print(f"깊은 복사 후: a={a}, d={d}")

# 해보기 문제 해결
singer = ['멜로망스', '잔나비', '이센스', '10센티', '이영지']
singer.append('비오')  # 맨 뒤에 '비오' 추가
singer.insert(2, '딥플로우')  # '잔나비' 뒤에 '딥플로우' 추가
singer.extend(['지코', '스윙스'])  # '지코', '스윙스' 한 번에 추가
singer.remove('지코')  # '지코' 제거
singer.clear()  # 리스트 모두 제거
print(f"최종 리스트: {singer}")
