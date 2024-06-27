# import threading
# import time

# def func(sec, delay, name):
#   print(f'{name}에게 업무가 할당 되었습니다')
#   for i in range(sec):
#     print(f'{name}이 {i+1}번째 일을 하고 있습니다')
#     time.sleep(delay)
#   print(f'{name}이 퇴근합니다')

# thread1 = threading.Thread(target=func, args =(5, 0.2, '최태산')) # 5초 동안 0.2초 간격
# thread1.start()

# thread2 = threading.Thread(target=func, args =(8, 0.3, '장태산')) 
# thread2.start()

# thread3 = threading.Thread(target=func, args =(10, 0.5, 'ADMIN')) # 데몬 쓰레드
# thread3.setDaemon(True)
# thread3.start()

import threading  
import time  

빵준비 = threading.Event()
토핑준비 = threading.Event()

# 첫 번째 작업: 빵을 준비하는 함수
def prepare_dough():
    print("Chef 1: 빵을 만들 준비중...")
    time.sleep(2)  # 2초 동안 빵을 준비하는 시간을 가정
    print("Chef 1: 빵을 만들 준비 완료")
    빵준비.set()  # 빵 준비 완료를 알리는 이벤트 설정

# 두 번째 작업: 토핑을 추가하는 함수
def add_toppings():
    빵준비.wait()  # 빵 준비가 완료될 때까지 대기
    print("Chef 2: 토핑 올리는 중...")
    time.sleep(1)  # 1초 동안 토핑을 추가하는 시간을 가정
    print("Chef 2: 토핑 완료")
    토핑준비.set()  # 토핑 준비 완료를 알리는 이벤트 설정

# 세 번째 작업: 피자를 굽는 함수
def bake_pizza():
    토핑준비.wait()  # 토핑 준비가 완료될 때까지 대기
    print("Chef 3: 피자 굽는 중")
    time.sleep(3)  # 3초 동안 피자를 굽는 시간을 가정
    print("Chef 3: 피자 굽기 완성")

# 각각의 작업을 수행할 스레드를 생성
chef1 = threading.Thread(target=prepare_dough)
chef2 = threading.Thread(target=add_toppings)
chef3 = threading.Thread(target=bake_pizza)

# 스레드 실행을 시작
chef1.start()
chef2.start()
chef3.start()

# 모든 스레드가 작업을 마칠 때까지 대기
chef1.join()
chef2.join()
chef3.join()

print("피자 만들기 끝")



