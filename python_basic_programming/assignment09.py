# -*-coding:utf-8 -*-
'''학번:20161048 이름 :이유리
과제번호:과제9
제출일자:2016.10.17
'''

def perfectShuffle(x):
    ''' 
        완벽한 섞기 리스트를 만들어 반환
        매개변수 x : 짝수 길이 리스트
    '''
    m=len(x)//2
    a1=x[:m]
    a2=x[m:]
    z=[]
    
    for k in range(m):
        a=a1.pop(k)
        z.append(a)
        a=a1.insert(k,a)
        
        b=a2.pop(k)
        z.append(b)
        b=a2.insert(k,b)
        
    return z


def numPerfectShuffle(x):
    ''' 
        매개변수로 전달된 리스트에 대해 나누고 섞는 과정을 반복하여 원래 리스트와 같아 지는 데 소요되는 횟수를 반환 
        매개변수 x : 짝수 길이 리스트
    '''
    
    a=x
    count=1
    
    while a!=perfectShuffle(x):
        
        count+=1
        x=perfectShuffle(x)
        perfectShuffle(x)
        
    return count
    


def main():
    x = [0, 1, 2, 3, 4, 5, 6, 7]
    num = numPerfectShuffle(x)
    print('원래 리스트가 되는 횟 수 : %d' %num)

main()