# 파일 입출력에 대한 설명
# 파일 읽기의 3단계:
# 1) 파일 열기: open() 함수에서 파일명을 지정하고, 읽기(Read)를 의미하는 "r"로 설정함
#    변수명 = open("파일경로/파일이름", "r")
#    모드(mode): open() 함수의 마지막 매개변수로, 파일을 열 때 어떤 용도로 열지 결정함. 파일 읽기는 “r”
# 2) 파일 읽기: 파일에서 데이터를 읽어 옴
#    readline() - 파일의 내용을 한 행씩 읽어 옴
#    readlines() - 파일의 내용을 한꺼번에 읽어 리스트에 저장함
# 3) 파일 닫기: 파일과 관련된 모든 작업이 끝나면 파일을 닫아줌
#    변수명.close()

# 파일 읽기 예제
fp = open('./filewrite.txt', 'r', encoding='UTF-8')  # 파일 열기 (읽기 모드)
indatas = fp.readlines()  # 파일의 모든 내용을 읽어 리스트에 저장
for indata in indatas:
    print(indata)  # 각 행을 출력
fp.close()  # 파일 닫기

# 파일 쓰기의 3단계:
# 1) 파일 열기: open() 함수에서 파일명을 지정하고, 쓰기(write)를 의미하는 "w"로 설정함
#    변수명 = open("파일경로/파일이름", "w")
#    모드(mode): open() 함수의 마지막 매개변수로, 파일을 열 때 어떤 용도로 열지 결정함. 파일 쓰기는 “w”
#    기존 파일에 추가해서 저장할 때에는 “a”를 사용
#    파일 경로에 같은 이름의 파일이 있다면 기존 파일을 덮어쓰고, 없으면 새로운 파일을 만듦
# 2) 파일 쓰기: 파일에 데이터를 저장
#    write() - 단일 문자열을 파일에 저장
#    writelines() - 리스트의 각 문자열을 파일에 저장
# 3) 파일 닫기: 파일과 관련된 모든 작업이 끝나면 파일을 닫아줌
#    변수명.close()

# 파일 쓰기 예제
fp = open('./filewrite.txt', 'w', encoding='UTF-8')  # 파일 열기 (쓰기 모드)
outStr = '안녕하세요 만나서 반갑습니다'
fp.writelines(outStr + '\n')  # 문자열을 파일에 저장

outStr = '우리 자주 만나요'
fp.writelines(outStr + '\n')  # 문자열을 파일에 저장
fp.close()  # 파일 닫기
