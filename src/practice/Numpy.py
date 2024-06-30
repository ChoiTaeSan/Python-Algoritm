# NumPy

# 벡터 및 행렬 연산을 위한 선형대수 기능 제공
# 고성능 수치계산을 위해 C언어로 구현된 수치해석용 파이썬 패키지 (C & 포트란)
# Python의 기본 List에 비해 실행 속도가 빠르고 강력한 기능 제공 (데이터가 클수록 파이썬 리스트가 비효율적)
# 배열(ndarray, n dimension array)구조 사용
# 1차원: [ ], 2차원: [[ ]], 3차원: [[[ ]]]

# numpy 라이브러리 설치
# !pip install numpy

# numpy 라이브러리 import 후 array 함수에 리스트를 넣어 배열로 변환
import Numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)
print(type(arr))  # <class 'numpy.ndarray'>

# 넘파이 타입
# array에서는 list와는 다르게 1개의 단일 데이터 타입만 허용
# 문자형이 하나라도 있으면 모두 문자형, 실수형이 하나라도 있으면 모두 실수형, 정수형만 있을 때만 정수형으로 표시
arr1 = np.array([1, 2, 3, 4, 5.5, 'abc', 6, 7, 8, 9, 10])
arr2 = np.array([1, 2, 3, 4, 5.5, 6, 7, 8, 9, 10])
print(arr1)  # ['1' '2' '3' '4' '5.5' 'abc' '6' '7' '8' '9' '10']
print(arr2)  # [ 1.  2.  3.  4.  5.5  6.  7.  8.  9. 10.]
print(type(arr1))  # <class 'numpy.ndarray'>
print(type(arr2))  # <class 'numpy.ndarray'>

# 벡터화 연산(vectorized operation)
# 배열의 모든 요소에 함수나 연산을 동시에 적용하는 기능을 의미
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = np.array(data)
print(x * 2)  # [ 2  4  6  8 10 12 14 16 18 20]

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)  # [11 22 33]
print(2 * a + b)  # [12 24 36]

print(a == 2)  # [False  True False]
print(b > 10)  # [False  True  True]
print((a == 2) & (b > 10))  # [False  True False]

# 배열연산

# 배열의 덧셈
arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # (2,3)
arr2 = np.array([[10, 11, 12], [13, 14, 15]])  # (2,3)
arr3 = np.array([10, 20, 30])  # (3,)
print(arr1 + arr2)  # [[11 13 15] [17 19 21]]
print(arr1 + arr3)  # [[11 22 33] [14 25 36]]
print(arr1 + 2)  # [[3 4 5] [6 7 8]]

# 배열의 뺄셈
print(arr1 - arr2)  # [[-9 -9 -9] [-9 -9 -9]]
print(arr1 - arr3)  # [[ -9 -18 -27] [ -6 -15 -24]]
print(arr1 - 5)  # [[-4 -3 -2] [-1  0  1]]

# 배열의 곱셈
print(arr1 * arr2)  # [[10 22 36] [52 70 90]]
print(arr1 * arr3)  # [[ 10  40  90] [ 40 100 180]]
print(arr1 * 5)  # [[ 5 10 15] [20 25 30]]

# 배열의 나눗셈
print(arr1 / arr2)  # [[0.1 0.18181818 0.25 ] [0.30769231 0.35714286 0.4 ]]
print(arr1 / arr3)  # [[0.1 0.1 0.1 ] [0.4 0.25 0.2 ]]
print(arr1 / 5)  # [[0.2 0.4 0.6] [0.8 1.  1.2]]

# 2차원 배열 만들기
arr1 = np.array([[1, 2, 3], [3, 4, 5]])
print(arr1)
print(len(arr1))  # 행의 개수: 2
print(len(arr1[0]))  # 열의 개수: 3

# 3차원 배열 만들기
arr3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                 [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]])
print(arr3)
print(len(arr3), len(arr3[0]), len(arr3[0][0]))  # 면, 행, 열의 개수: 2 3 4

# 배열의 차원 크기 알아보기
arr1 = np.array([1, 2, 3])  # (1, 3)
arr2 = np.array([[10, 11, 12], [13, 14, 15]])  # (2, 3)
arr3 = np.array([[[10, 11, 12], [13, 14, 15]], [[100, 110, 120], [130, 140, 150]]])  # (2, 2, 3)

print(arr1.ndim, arr1.shape)  # 1 (3,)
print(arr2.ndim, arr2.shape)  # 2 (2, 3)
print(arr3.ndim, arr3.shape)  # 3 (2, 2, 3)

# 배열의 차원 변형
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f'1차원 -> {arr}')

arr = np.reshape(arr, (2, 4))
print(f'2차원 -> {arr}')

arr = np.reshape(arr, (8,))
print(f'1차원 -> {arr}')

arr2 = np.array([[10, 11, 12], [13, 14, 15]])  # (2, 3)
arr3 = np.array([[[10, 11, 12], [13, 14, 15]], [[100, 110, 120], [130, 140, 150]]])  # (2, 2, 3)

array_1d = arr2.flatten()
print(array_1d)  # [10 11 12 13 14 15]

array_1d = arr3.flatten()
print(array_1d)  # [ 10  11  12  13  14  15 100 110 120 130 140 150]

# 배열 행과 열의 전치
arr2 = np.array([[10, 11, 12], [13, 14, 15]])
print(f' 배열 -> {arr2}')

t_arr2 = np.transpose(arr2)
print(f' 배열 전치 -> {t_arr2}')

t_arr2 = arr2.T
print(f' T속성 배열 전치 -> {t_arr2}')

# 특정 범위의 숫자를 배열로 생성하기
arr = np.arange(1, 11, 1)
print(arr)  # [ 1  2  3  4  5  6  7  8  9 10]

arr = np.arange(1, 11, 2)
print(arr)  # [1 3 5 7 9]

arr = np.arange(1, 2.0, 0.1)
print(arr)  # [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]

# 특정 값으로 이루어진 배열 만들기
arr = np.zeros(10)
print(arr)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

arr = np.ones(10)
print(arr)  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# numpy 통계 함수들
a = np.arange(12).reshape(3, 4)
print(a)  # [[ 0  1  2  3] [ 4  5  6  7] [ 8  9 10 11]]

print(a.max())  # 최대값: 11
print(np.max(a))  # 최대값: 11

print(a.min())  # 최소값: 0
print(np.min(a))  # 최소값: 0

print(a.sum())  # 합: 66
print(a.mean())  # 평균: 5.5

print(a.std())  # 표준편차: 3.452052529534663
print(a.var())  # 분산: 11.916666666666666
print(np.median(a))  # 중위수: 5.5

# 사분위수
print('25%:', np.percentile(a, 25))  # 1사분위수(Q1): 2.75
print('50%:', np.percentile(a, 50))  # 2사분위수(Q2): 5.5
print('75%:', np.percentile(a, 75))  # 3사분위수(Q3): 8.25
