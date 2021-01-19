# -*- coding: utf-8 -*-

""" 학번 : 20161048, 이름 : 이유리
과제번호 : 과제 2.1
제출일 : 2016.9.22
"""

w = input('문자열(명사 단수): ') #키보드로부터 문자열(명사 단수)을 입력받는다.
n=len(w) #특정한 변수에 저장된 문자열의 철자 갯수를 저장한다
m=n-1
o=n-2

if w[m] == 'y' :
    plural = w[:m] + 'ies'
elif w[o:]=='ro' or w[o:]=='to' or w[o:]=='no': #여러 개의 선택사항이 있는 경우 if-elif-else 문을 사용한다.
    plural=w+'es'
elif w[m]=='s' or w[m]=='h' or w[m]=='x':
    plural=w+'es'
elif w[o:]=='fe':
    plural=w[:o]+'ves'
else:
    plural=w+'s'

print('%s의 복수형 : %s' %(w,plural))