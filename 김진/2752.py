# 숫자 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성
num_list = list(map(int, input().split()))
num_list.sort()
for i in range(len(num_list)):
    print(num_list[i], end = " ")
