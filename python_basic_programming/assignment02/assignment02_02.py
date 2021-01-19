# -*- coding: utf-8 -*-

""" 학번 : 20161048, 이름 : 이유리
과제번호 : 과제 2.2
제출일 : 2016.9.22
"""

from random import randint  # 지정된 모듈(random) 내의 필요한 특정 함수(randint)만을 불러들임

n1 = randint(0, 9)  # 랜덤 수 생성
n2 = randint(0, 9)
n3 = randint(0, 9)

count = 0

x = input('첫번 째 1자리 정수를 입력하시오 :')  # 키보드로부터 1자리 정수를 입력받는다.
y = input('두번 째 1자리 정수를 입력하시오 :')
z = input('세번 째 1자리 정수를 입력하시오 :')

if n1==x or n1==y or n1==z:
    count +=1
if n2==x or n2==y or n2==z:
    count+=1
if n3==x or n3==y or n3==z:
    count+=1

if count==3:
    print("1등입니다")
elif count==2:
    print("2등입니다")
elif count==1:
    print("3등입니다")
else:
    print("꼴찌입니다")
