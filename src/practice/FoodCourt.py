from datetime import datetime as dt

menu = {"대들보 밥버거" : 5000, "햄 밥버거" : 5500, "햄 치즈 밥버거" : 6000, "제육 밥버거" : 6500, "치즈제육 밥버거" : 7000}
selectMenu = {}
orderTime = {}
d_2 = {1:"대들보 밥버거", 2:"햄 밥버거", 3:"햄 치즈 밥버거", 4:"제육 밥버거", 5:"치즈제육 밥버거"}
print("----------------------------------------")
print("              대들보 밥버거              ")
print("----------------------------------------")

for i, j in enumerate(menu.items()):
    print(f'{i}. {j[0]} : {j[1]:,}원')

# 메뉴의 키를 리스트로 변환
menu_keys = list(menu.keys())

while True:
    # 사용자로부터 메뉴 인덱스 입력 받기
    selectMenuNum = int(input(f'메뉴를 선택해주세요 (0 ~ {len(menu_keys) - 1}) : '))
        
    # 인덱스 범위 검사
    if 0 <= selectMenuNum < len(menu_keys):
        # 선택된 메뉴 이름과 가격 출력
        selected_menu_name = menu_keys[selectMenuNum]
        selected_menu_price = menu[selected_menu_name]
        print(f"{selected_menu_name}의 가격은 {selected_menu_price}원입니다.")
    else:
        print("잘못된 인덱스..! 다시 시도하세요.")
    
    cnt = int(input('몇 개를 드릴까요? :'))
    print(f"{selected_menu_name} X {cnt} = {selected_menu_price * cnt}원입니다.")
    if(selectMenu.get(selected_menu_name)):
        selectMenu[selected_menu_name] += cnt
    else :
        selectMenu[selected_menu_name] = cnt
    now = dt.now()
    stringNow = now.strftime('%Y-%m-%d %H:%M:%S')
    
    orderTime[selected_menu_name] = stringNow
    
    a = input('더 주문하시겠습니까?(y/n)')
    if a == 'y':
        continue
    elif a == 'n':
        break
    else:
        print('잘못된 입력입니다')

def calculateFee(menuInfo, orderInfo):
    totalFee = 0
    print("----------------------------------------")
    for key, value in orderInfo.items():
        fee = value * menuInfo[key]
        outputString = f"{key} : {value} --- {fee:,}"
        
        print(outputString)
        totalFee += fee # 가격 뽑아와서 주문 개수에 맞게 계산
    print("----------------------------------------")
    print(f"총 가격 : {totalFee:,}")
    return totalFee
total = calculateFee(menuInfo = menu, orderInfo = selectMenu)

fp = open('./order.csv', 'w', encoding='UTF-8')

for menu_name, cnt in selectMenu.items():
    order_time = orderTime[menu_name]
    total_price = menu[menu_name] * cnt
    
    fp.writelines(f"{order_time}, {menu_name}, {cnt}, {total_price}\n")

fp.close()
