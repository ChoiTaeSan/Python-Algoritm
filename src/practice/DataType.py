# 파이썬 자료형 예제 코드

# 정수형 (Integer)
# 소수점이 없는 숫자. 예: 0, 1, -5
int_var = 10
print(f"정수형: {int_var}, 타입: {type(int_var)}")  # 출력: 정수형: 10, 타입: <class 'int'>

# 부동소수점 수 (Floating point number)
# 소수점을 포함하는 숫자. 예: 0.0, -2.7, 3.14
float_var = 3.14
print(f"부동소수점 수: {float_var}, 타입: {type(float_var)}")  # 출력: 부동소수점 수: 3.14, 타입: <class 'float'>

# 문자열 (String)
# 텍스트 데이터를 표현. 작은따옴표(')나 큰따옴표(")로 묶습니다. 예: 'Hello', "Python"
str_var = "Hello, World!"
print(f"문자열: {str_var}, 타입: {type(str_var)}")  # 출력: 문자열: Hello, World!, 타입: <class 'str'>

# 불린형 (Boolean)
# 참(True) 또는 거짓(False) 값을 가집니다. 논리적 조건을 나타낼 때 사용. 예: True, False
bool_var = True
print(f"불린형: {bool_var}, 타입: {type(bool_var)}")  # 출력: 불린형: True, 타입: <class 'bool'>

# 리스트 (List)
# 여러 값을 순서대로 저장할 수 있는 가변적 자료형. 대괄호([])로 묶고, 값은 쉼표(,)로 구분. 예: [1, 2, 3]
list_var = [1, 2, 3, 4, 5]
print(f"리스트: {list_var}, 타입: {type(list_var)}")  # 출력: 리스트: [1, 2, 3, 4, 5], 타입: <class 'list'
# 튜플 (Tuple)
# 여러 값을 순서대로 저장할 수 있는 불변적 자료형. 소괄호(())로 묶고, 값은 쉼표(,)로 구분. 예: (1, 2, 3)
tuple_var = (1, 2, 3)
print(f"튜플: {tuple_var}, 타입: {type(tuple_var)}")  # 출력: 튜플: (1, 2, 3), 타입: <class 'tuple'>

# 딕셔너리 (Dictionary)
# 키-값 쌍으로 데이터를 저장하는 자료형. 중괄호({})로 묶고, 키:값 형태로 표현. 예: {"name": "John", "age": 30}
dict_var = {"name": "John", "age": 30}
print(f"딕셔너리: {dict_var}, 타입: {type(dict_var)}")  # 출력: 딕셔너리: {'name': 'John', 'age': 30}, 타입: <class 'dict'>

# 집합 (Set)
# 중복되지 않는 값을 저장하는 자료형. 중괄호({})로 묶고, 값은 쉼표(,)로 구분. 예: {1, 2, 3}
set_var = {1, 2, 3, 4, 5}
print(f"집합: {set_var}, 타입: {type(set_var)}")  # 출력: 집합: {1, 2, 3, 4, 5}, 타입: <class 'set'>

# None 타입
# 값이 없음을 나타내는 자료형. 변수에 값이 아직 설정되지 않았음을 표시. 예: None
none_var = None
print(f"None 타입: {none_var}, 타입: {type(none_var)}")  # 출력: None 타입: None, 타입: <class 'NoneType'>
