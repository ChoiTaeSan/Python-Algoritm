import random  # random 모듈

def random_number():
    # 1부터 100까지의 랜덤 숫자 반환 함수
    return random.randint(1, 100)

# 정답 숫자
correct = int(random_number())
# 사용자 입력 숫자
guess = 0

# 사용자가 정답을 맞출 때까지 반복 루프
while guess != correct:
    # 사용자로부터 숫자 입력 받기
    guess = int(input("정답을 맞춰주세요:"))
    # 입력한 숫자가 정답보다 작은 경우
    if correct > guess:
        print('더 큰 수입니다')
    # 입력한 숫자가 정답보다 큰 경우
    elif correct < guess:
        print('더 작은 수입니다')
    # 입력한 숫자가 정답과 같은 경우
    elif correct == guess:
        print('정답입니다')
    # 범위 내 숫자가 아닌 경우 (사실상 필요 없는 부분, 중복 입력 방지 조건)
    else:
        print('범위 내 숫자를 입력해주세요')
