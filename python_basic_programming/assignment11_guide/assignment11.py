#*-* coding:utf-8 -*-
import operator

def getWordList(filename):         
    ''' 지정된 텍스트 파일(filename)로부터 문장들을 읽은 후, 특수문자들은 모두 삭제하고 
                 영어 단어로만 이루어진 리스트 반환 
    '''  
    file = open(filename, 'r')
    documents = file.read()
    file.close()
    
    symbols = "~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?"
    documents = documents.lower()
    for ch in symbols :
        documents = documents.replace(ch, ' ')
    
    return documents.split()

def getWordsInDocument(wordList):
    ''' 영어 단어들로 이루어진 문자열 리스트(wordlist, 중복된 단어들 존재)를 이용하여 단어들에 대한 빈도를 계산하여, 
                  키(key)가 단어이고 값(value)가 빈도인 딕셔너리를 반환
    '''    
    wordDict = {}
    
    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    
    return wordDict

def getSortedWords(wordList):
    ''' 단어들로 이루어진 문자열 리스트(wordlist, 중복된 단어들 존재)를 이용하여 
                  중복되지 않은 단어들을 만들어진 정렬된(알파벳 순) 리스트를 반환
    '''    








       

def getWordFrequency(wordList):
    ''' 단어들로 이루어진 문자열 리스트(wordlist, 중복된 단어들 존재)를 이용하여 단어들에 대한 빈도를 계산하여, 
                  각 단어들의 빈도에 따라 정렬된(내림차순) 리스트를 반환
    '''
    wordDict = getWordsInDocument(wordList)    
    freqList = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    #freqList = sorted(wordDict.items(), key=lambda x: x[1], reverse = True)     #위의 sorting 명령과 동일        
         
    return freqList        
        
def getLengthWords(wordList, n):
    ''' 단어들로 이루어진 문자열 리스트(wordlist, 중복된 단어들 존재)를 이용하여, 
                  단어의 길이가 주어진 길이(n)보다 큰 단어들로만 구성된 리스트를 반환(단, 알파벳 순으로 정렬)
    '''
    







def getXFreqWords(wordList, n):
    ''' 단어들로 이루어진 문자열 리스트(wordlist, 중복된 단어들 존재)를 이용하여, 
                  단어의 빈도가  주어진 값(n)보다 큰 단어들로만 구성된 리스트를 반환(단, 빈도순으로 정렬)
    '''








def main():
    statements = getWordList('gettysburg_address.txt')
    print(statements)
    wordList = getSortedWords(statements)
    print(wordList)
    wordFreqList = getWordFrequency(statements)
    print(wordFreqList)
    wordLenList = getLengthWords(wordList, 10)
    print(wordLenList)
    wordFrList = getXFreqWords(statements, 10)
    print(wordFrList)

    
main() 
# [5] Have your script process tale and print out the following.
# How many word tokens it has,
# How many word types it has,
# How many times 'was' occurs in the text,
# Words that are at least 10 characters long,
# Words that occur at least 10 times,
# And finally, *EVERY WORD TYPE* in tale followed by its frequency count. 
# YOUR CODE BELOW.
