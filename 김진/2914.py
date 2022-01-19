# 적어도 몇 곡이 저작권이 있는 멜로디인지 구하는 프로그램을 작성
A, I = map(int, input().split())    # A: 앨범 수록곡 수, I: 평균값
print(A * (I - 1) + 1)
