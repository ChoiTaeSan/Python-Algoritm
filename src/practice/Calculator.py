def calculator():
    print("간단한 계산기")
    print("두 숫자와 연산자를 입력하세요 (+, -, *, /)")

    # 사용자 입력 받기
    num1 = float(input("첫 번째 숫자: "))
    operator = input("연산자 (+, -, *, /): ")
    num2 = float(input("두 번째 숫자: "))

    # 계산 및 결과 출력
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("오류: 0으로 나눌 수 없습니다.")
            return
    else:
        print("오류: 유효하지 않은 연산자입니다.")
        return

    # 결과 출력
    print(f"결과: {num1} {operator} {num2} = {result}")

# 계산기 함수 실행
calculator()
