# 딕셔너리(Dictionary)에 대한 특징과 설명
# - 하나의 변수(대표이름)에 다수의 데이터를 저장하는 자료형
# - 키(key): 값(value)이 쌍을 이루어 하나의 항목에 저장됨
# - 인덱스가 아닌 키(key)로 자료에 접근
# - 파이썬 3.7부터 입력한 순서대로 저장됨

# 딕셔너리에서 값 추출하기
# 딕셔너리명[키] : 존재하지 않으면 오류 발생
# 딕셔너리명.get(키, '없어요') : 존재하지 않으면 default값 리턴

dict_1 = {'홍길동': 90, '강길동': 80, '정길동': 100}
print(dict_1.get('최길동', '없음'))  # 키 '최길동'이 존재하지 않으면 '없음' 반환

# 딕셔너리에 키 값이 존재하는지 여부 알아보기
# key in dict
if '강길동' in dict_1:
    print('있습니다')
else:
    print('없습니다')

# 딕셔너리 값 수정
# 키가 있으면 수정, 없으면 추가
dict_1['홍길동'] = 50  # 기존 값 수정
dict_1['최길동'] = 100  # 새로운 키-값 추가
print(dict_1)

# 딕셔너리에서 항목 삭제하기
# del(딕셔너리명[키]) 또는 딕셔너리명.pop(키)
del dict_1['홍길동']  # 키 '홍길동'의 항목 삭제
dict_1.pop('강길동')  # 키 '강길동'의 항목 삭제
print(dict_1)

# 모든 항목 삭제
dict_1.clear()
print(dict_1)

# 딕셔너리의 키, 값, 항목 출력하기
dict_1 = {'홍길동': 90, '강길동': 80, '정길동': 100}
print(dict_1.keys())    # 키만 출력
print(dict_1.values())  # 값만 출력
print(dict_1.items())   # 키-값 쌍 출력

# for 반복문으로 딕셔너리의 키, 값 모두 출력하기
for key, value in dict_1.items():
    print(key, value)

# 딕셔너리의 데이터 정렬
# 딕셔너리 정렬: sorted() 사용
print(sorted(dict_1.keys()))    # 키를 기준으로 정렬
print(sorted(dict_1.values()))  # 값을 기준으로 정렬
print(sorted(dict_1.items()))   # 항목을 기준으로 정렬

# 키를 정렬하여 키 순서대로 출력
for k, v in sorted(dict_1.items(), reverse=True):
    print(k, v)
