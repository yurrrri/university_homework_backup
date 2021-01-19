# -*- coding: utf-8 -*-
""" 
학번 : 20161048, 이름 : 이유리
과제번호 : 과제 6
제출일 : 2016.10.10
"""

from random import randint as randi

def GenCoinToss(n): #n번의 동전던지기를 하여 문자열을 반환하는 함수
    s=''
    
    for k in range(n):
        i=randi(0,1)
        if i==1:
            s=s+'H'
        else:
            s=s+'T'
            
    return s

def isSandwich(t): #문자열이 길이-n 샌드위치 문자열인가를 알아내는 함수
    n=len(t)
    Meat=t[1:n-1]
    Type1=t[0]=='H' and t[n-1]=='H'
    Type1=Type1 and Meat.count('T')==n-2
    
    Type2=t[0]=='T' and t[n-1]=='T'
    Type2=Type2 and Meat.count('H')==n-2
    
    return Type1 or Type2

def isStreak(s,k,n): #문자열이 길이-n 스트릭인가를 알아내는 함수
    t=s[k:k+n]
    
    if k+n>len(s):
        return False
    elif t.count('H')<n and t.count('T')<n:
        return False
    elif k>0 and (s[k-1]==s[k]):
        return False
    elif (k+n<len(s)) and (s[k+n-1]==s[k+n]):
        return False
    else:
        return True

def FindStreak(s,n): #길이-n 스트릭을 찾아내는 함수
    k=0
    
    while k<len(s) and (not isStreak(s,k,n)):
        k=k+1
        
    if k<len(s):
        return k
    else:
        return -1
    
def main():
    s=GenCoinToss(300)
    print(s)
    
    k=0
    m=0 #길이-10 샌드위치 문자열의 개수를 세기 위한 변수
    
    while k+10<=300:
        t=s[k:k+10]
        
        if isSandwich(t): #k=0부터 차례대로 길이 10짜리 샌드위치 문자열인가를 확인한 후 맞으면 1개를 더해줌
            m+=1
        
        k+=1
    
    if m==0:
        print('길이-10짜리 샌드위치 문자열이 존재하지 않습니다.')
    else:
        print('길이-10짜리 샌드위치 문자열이 %d개 존재합니다.' %m)
        
    k=0
    p=0 #길이-10 스트릭의 개수를 세기 위한 변수
        
    while k+10<=300 and (not FindStreak(s,10)==-1):
        
        t=s[k:k+10]
        
        if isStreak(s,k,10): #k=0부터 차례대로 길이 10짜리 스트릭인가를 확인한 후 맞으면 1개를 더해줌
            p+=1
            
        k+=1
    
    if p==0:
        print ('길이-10짜리 스트릭이 존재하지 않습니다.')
    else:
        print ('길이-10짜리 스트릭이 %s개 존재합니다.' %p)
        
main()