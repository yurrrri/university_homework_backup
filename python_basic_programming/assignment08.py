# -*- coding:utf-8 -*-
""" 
과제: 20161048, 이름: 이유리
과제번호: 과제 8
제출일자 : 2016.10.17
"""

import math

DIGITS = '1234567890'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
SPECIAL = '!"#$%&\’()*+,-./:;<=>?@[\\]^_‘{|}~'

def howMany(s1, s2):        
    '''     
         매개변수 s1의 문자들이  매개변수 s2에 포함된  갯수를 계산하여 반환
    s1 : 문자열, s2 : 문자열 
    '''     
    s1=str(s1)
    s2=str(s2)
    
    count=0 #포함된 갯수를 계산하기 위한 변수
    
    for m in range(len(s1)):
        if s1[m] in s2:
            count+=1
            
    return count

def howManyTriplets(s1, s2):
    '''     
         매개변수 s1의  크기가 3인 부분 문자열들이  문자열 s2에 포함된  갯수를 계산하여 반환
    s1 : 문자열, s2 : 문자열 
    '''
    s1=str(s1)
    s2=str(s2)
   
    k=0
    a=s1[k:k+3]
    count=0 #포함된 갯수를 계산하기 위한 변수
    
    while k+3<=len(s1):
        if a in s2:
            count+=1
        k+=1
        
    return count
            
    
def A1(s):      
    '''
        매개변수 s에 대한 가산점 기준 A1에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    a1_n=len(s)
    a1=3*(a1_n)
    
    if 3*(a1_n)<=45:
        return a1
    else:
        return 45


def A2(s):
    '''
        매개변수 s에 대한 가산점 기준 A2에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    l=howMany(s,LOWER)
    u=howMany(s,UPPER)
    m=howMany(s,LOWER+UPPER)
    
    if m==0:
        return 0
    else:
        a2=math.floor(40*(1-l/m)*(1-u/m))
    
        return a2

    
def A3(s):
    '''
        매개변수 s에 대한 가산점 기준 A3에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    a3_n=howMany(s,DIGITS)
    
    a3=4*a3_n
    
    return a3

def A4(s):
    '''
        매개변수 s에 대한 가산점 기준 A4에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    a4_n=howMany(s,SPECIAL)
    a4=6*a4_n
    
    return a4

def A5(s):
    '''
        매개변수 s에 대한 가산점 기준 A5에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    k=len(s)
    a5_n5_1=howMany(s[1:k-1],DIGITS)
    a5_n5_2=howMany(s[1:k-1],SPECIAL)
    
    a5_n=a5_n5_1+a5_n5_2
    a5=3*a5_n

    return a5

def A6(s):
    '''
        매개변수 s에 대한 가산점 기준 A6에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    if (howMany(s,DIGITS)+howMany(s,UPPER)+howMany(s,LOWER)+howMany(s,SPECIAL))==len(s):
        a6=10
    else:
        a6=0

    return a6
    
def D1(s):
    '''
        매개변수 s에 대한 감점 기준 D1에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    if len(s)==(howMany(s,UPPER)+howMany(s,LOWER)):
        d1=len(s)
    else:
        d1=0

    return d1
    
def D2(s):
    '''
        매개변수 s에 대한 감점 기준 D2에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    if len(s)==howMany(s,DIGITS):
        d2=len(s)
    else:
        d2=0

    return d2
 
def D3(s):
    '''
        매개변수 s에 대한 감점 기준 D3에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    d3_n=len(s)
    m=0
    
    for k in range(d3_n):
        x=s[k]
        y=s.count(x)
        
        if y==1:
            m+=1
            
    d3=3*(d3_n-m)
        
    return d3

def D4(s):
    '''
        매개변수 s에 대한 감점 기준 D4에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    k=0
    d4_n_1=0  #해당하는 갯수를 계산하기 위한 변수
    d4_n_2=0
    d4_n_3=0
    d4_n_4=0
    
    while k+1<len(s):
        if s[k] in UPPER and s[k+1] in UPPER:
            d4_n_1+=1
        elif s[k] in LOWER and s[k+1] in LOWER:
            d4_n_2+=1
        elif s[k] in DIGITS and s[k+1] in DIGITS:
            d4_n_3+=1
        elif s[k] in SPECIAL and s[k+1] in SPECIAL:
            d4_n_4+=1
        k+=1
        
    d4=2*(d4_n_1+d4_n_2+d4_n_3+d4_n_4)
    
    return d4

def D5(s):
    '''
        매개변수 s에 대한 감점 기준 D5에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    d5_n=howManyTriplets(s,DIGITS)
    d5=3*(d5_n)
    
    return d5

def D6(s):
    '''
        매개변수 s에 대한 감점 기준 D6에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    d6_n=howManyTriplets(s,'qwertyuiopdml')
    d6=3*(d6_n)
    
    return d6

def D7(s):
    '''
        매개변수 s에 대한 감점 기준 D7에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    s=str(s)
    d7_n=howManyTriplets(s,'asdfghjkl')
    d7=3*(d7_n)
    
    return d7

def D8(s):
    '''
        매개변수 s에 대한 감점 기준 D8에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    d8_n=howManyTriplets(s,'zxcvbnm')
    d8=3*(d8_n)
    
    return d8


def getPassword():    
    '''
        허용하는 문자로만 구성된 비밀번호를 입력받아 반환
    '''
    
    repeatFlag = True
    while repeatFlag: #아래의 조건문을 무한 반복          
        pwd = input('비밀번호: ')
        
        n1=howMany(pwd,UPPER)
        n2=howMany(pwd,LOWER)
        n3=howMany(pwd,DIGITS)
        n4=howMany(pwd,SPECIAL)
        
        if (n1+n2+n3+n4)!=(len(pwd)):
            print('허용하지 않는 문자가 있습니다')
        else:
            repeatFlag=False #허용하는 문자로만 이루어졌을 때 비밀번호의 입력 반복을 멈추어야 하므로 False로 지정하여 while 반복문을 끝냄
            
    return pwd
def main(): 
    '''
        비밀번호 강도가 50이상 일 때까지 비밀번호를 입력읋 받은 후  비밀번호 강도 점수와 가산점수, 감점점수를 출력
        단,가산점수(A1~A6), 감점점수(D1~D8)는 리스트로 저장하여 처리
    '''
         
    repeatFlag = True #아래의 조건문을 무한 반복   
    while repeatFlag:
        myPwd = getPassword()
        ascore = [A1(myPwd), A2(myPwd), A3(myPwd), A4(myPwd), A5(myPwd), A6(myPwd)]
        dscore = [D1(myPwd), D2(myPwd), D3(myPwd), D4(myPwd), D5(myPwd), D6(myPwd), D7(myPwd), D8(myPwd)]
        
        score=sum(ascore)-sum(dscore)
        
        if score <60:
            print('비밀번호 강도 점수 : %d ---> 비밀번호의 강도 수준이 너무 낮습니다. 다시 입력하세요.' %(score))
        else:
            repeatFlag=False #강도가 60이상일 때 비밀번호의 입력 반복을 끝내야 하므로 False로 지정하여 while 반복문을 끝냄
            print('입력 암호: %s --> 강도 : %d' %(myPwd, score))
            print('가산 점수 : %3d %3d %3d %3d %3d %3d' %(ascore[0], ascore[1], ascore[2], ascore[3], ascore[4], ascore[5]))
            print('감점 점수 : %3d %3d %3d %3d %3d %3d %3d %3d' %(dscore[0], dscore[1], dscore[2], dscore[3], dscore[4], dscore[5], dscore[6], dscore[7]))
    
main()