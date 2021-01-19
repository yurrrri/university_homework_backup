# -*- coding:utf-8 -*-

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





def howManyTriplets(s1, s2):
    '''     
         매개변수 s1의  크기가 3인 부분 문자열들이  문자열 s2에 포함된  갯수를 계산하여 반환
    s1 : 문자열, s2 : 문자열 
    '''    





    
def A1(s):      
    '''
        매개변수 s에 대한 가산점 기준 A1에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    


def A2(s):
    '''
        매개변수 s에 대한 가산점 기준 A2에 대한 점수를 계산하여 반환
    s : 문자열
    '''
    






    
def A3(s):
    '''
        매개변수 s에 대한 가산점 기준 A3에 대한 점수를 계산하여 반환
    s : 문자열
    '''




def A4(s):
    '''
        매개변수 s에 대한 가산점 기준 A4에 대한 점수를 계산하여 반환
    s : 문자열
    '''



def A5(s):
    '''
        매개변수 s에 대한 가산점 기준 A5에 대한 점수를 계산하여 반환
    s : 문자열
    '''








def A6(s):
    '''
        매개변수 s에 대한 가산점 기준 A6에 대한 점수를 계산하여 반환
    s : 문자열
    '''








    
def D1(s):
    '''
        매개변수 s에 대한 감점 기준 D1에 대한 점수를 계산하여 반환
    s : 문자열
    '''






    
def D2(s):
    '''
        매개변수 s에 대한 감점 기준 D2에 대한 점수를 계산하여 반환
    s : 문자열
    '''







    
def D3(s):
    '''
        매개변수 s에 대한 감점 기준 D3에 대한 점수를 계산하여 반환
    s : 문자열
    '''









def D4(s):
    '''
        매개변수 s에 대한 감점 기준 D4에 대한 점수를 계산하여 반환
    s : 문자열
    '''












def D5(s):
    '''
        매개변수 s에 대한 감점 기준 D5에 대한 점수를 계산하여 반환
    s : 문자열
    '''







def D6(s):
    '''
        매개변수 s에 대한 감점 기준 D5에 대한 점수를 계산하여 반환
    s : 문자열
    '''







def D7(s):
    '''
        매개변수 s에 대한 감점 기준 D7에 대한 점수를 계산하여 반환
    s : 문자열
    '''





def D8(s):
    '''
        매개변수 s에 대한 감점 기준 D8에 대한 점수를 계산하여 반환
    s : 문자열
    '''




def getPassword():    
    '''
        허용하는 문자로만 구성된 비밀번호를 입력받아 반환
    '''
    
    repeatFlag = True
    while repeatFlag:            
        pwd = input('비밀번호 : ')
        # 나머지 코드 완성
    
    
    
    
    
    
    
    
    return pwd

def main(): 
    '''
        비밀번호 강도가 50이상 일 때까지 비밀번호를 입력읋 받은 후  비밀번호 강도 점수와 가산점수, 감점점수를 출력
        단,가산점수(A1~A6), 감점점수(D1~D8)는 리스트로 저장하여 처리
    '''
         
    repeatFlag = True
    while repeatFlag:
        myPwd = getPassword()
        ascore = [A1(myPwd), A2(myPwd), A3(myPwd), A4(myPwd), A5(myPwd), A6(myPwd)]
        dscore = [D1(myPwd), D2(myPwd), D3(myPwd), D4(myPwd), D5(myPwd), D6(myPwd), D7(myPwd), D8(myPwd)]
        # 나머지 코드 완성





    
    print('입력 암호 : %s --> 강도 : %d' %(myPwd, score))
    print('가산 점수 : %3d %3d %3d %3d %3d %3d' %(ascore[0], ascore[1], ascore[2], ascore[3], ascore[4], ascore[5]))
    print('감점 점수 : %3d %3d %3d %3d %3d %3d %3d %3d' %(dscore[0], dscore[1], dscore[2], dscore[3], dscore[4], dscore[5], dscore[6], dscore[7]))
    
main()
    