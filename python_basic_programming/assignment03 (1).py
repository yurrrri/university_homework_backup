# -*- coding: utf-8 -*-

""" 학번 : 20161048, 이름 : 이유리
과제 : 과제 3
제출일자 : 2016.9.27
"""

def plural(): #함수를 정의한다.
    w = input('문자열 (명사단수): ')
    n=len(w) #len:문자열의 길이를 숫자로 변환해준다.
    m=n-1
    o=n-2

    if w[m] == 'y' : #if-elif-else 문: 선택이 여러가지 일때 사용
        p = w[:m] + 'ies'
    elif w[o:]=='ro' or w[o:]=='to' or w[o:]=='no':
        p = w+'es'
    elif w[m]=='s' or w[m]=='h' or w[m]=='x':
        p = w+'es'
    elif w[o:]=='fe':
        p= w[:o]+'ves'
    else:
        p = w+'s'
    return p #함수에 해당하는 명령문을 실행하는 도중, 함수를 호출한 지점으로 복귀하게 해주는 문장

def main(): #함수를 정의한다.
    pr=plural()
    print('복수형:'+pr)

main() #해당하는 이름의 함수를 호출한다.

