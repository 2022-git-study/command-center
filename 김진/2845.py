# 각 신문 기사에 실려있는 참가자의 수가 몇 명 만큼 잘못되어있는지 구하는 프로그램을 작성
L, P = map(int, input().split())      # L: 1m^2 당 사람의 수, P: 파티가 열린 장소의 넓이

newsList = list(map(int, input().split()))
for i in newsList:
    print(i - (L * P), end = " ")
