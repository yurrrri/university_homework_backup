# -*- coding: utf-8 -*-
'''
학번 : 20161048, 이름: 이유리
과제번호: 과제  1.2
제출일 : 2016.9.18
'''

p = input('분값: ') #키보드를 통해 분값 입력
q = int(p) #연산식의 결과를 정수로 변환한다.
r = q//60 #분값을 60분(1시간)으로 정수 나눗셈 한다. 

s = q%60 #분값을 60분(1시간)으로 나눈 나머지를 구한다.
print(r, '시간', s, '분')