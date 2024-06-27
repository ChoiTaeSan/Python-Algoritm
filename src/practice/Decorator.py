import time

# 실행 시간을 측정하는 데코레이터 함수
def running_time_decorator(func):
    # 데코레이터가 감쌀 함수의 래퍼 함수 정의
    def wrapper(*arg):
        # 시작 시간 기록
        start_time = time.time()
        # 원래 함수 실행
        func(*arg)
        # 끝 시간 기록
        end_time = time.time()
        # 실행 시간 계산
        running_time = end_time - start_time
        # 실행 시간 출력
        print(f"{func.__name__} 함수를 실행하는데 {running_time:.4f}초 걸렸습니다")
    # 래퍼 함수를 반환
    return wrapper

# 데코레이터를 이용해 실행 시간을 측정할 카운트 다운 함수
@running_time_decorator
def count_down(num):
    # num이 0이 될 때까지 감소
    while num:
        num -= 1

# 데코레이터를 이용해 실행 시간을 측정할 합산 함수
@running_time_decorator
def sum_up_to(num):
    result = 0
    # 0부터 num까지의 수를 모두 더함
    for i in range(0, num + 1):
        result += i
    # 최종 합계를 출력
    print('누적 합계는', result)

# count_down 함수 실행
count_down(100000)

# sum_up_to 함수 실행
sum_up_to(100000)
