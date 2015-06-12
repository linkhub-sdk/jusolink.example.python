# -*- coding: utf-8 -*-
# code for console Encoding difference. Don't mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Except as E: pass

import testValue

from jusolink import Jusolink, JusolinkException

jusolinkService = Jusolink(testValue.LinkID,testValue.SecretKey)

try:
    print("[주소검색 결과확인]")

    #검색어 
    indexWord = "테헤란로" 
 
    pageNum = 1           # 페이지번호
    perPage = 20          # 페이지당 목록 갯수, 최대 100개
    noSuggest = False     # 수정제시어 끄기
    noDiffer = False      # 차둥금색 끄기

    result = jusolinkService.search(indexWord, pageNum, perPage, noSuggest, noDiffer)
        
    tmp = "검색문자열 : " + str(result.searches) + "\n"
    tmp += "수정제시어 : " + str(result.suggest) + "\n"
    tmp += "총 검색 결과 수 : " + str(result.numFound) + "\n"
    tmp += "검색된 페이지 번호 : " + str(result.page) + "\n"
    tmp += "총 페이지 수 : " + str(result.totalPage) + "\n"
    tmp += "페이지 목록 갯수 : " + str(result.listSize) + "\n"
    tmp += "과금 여부 : " + str(result.chargeYN) + "\n\n"
    
    if result.juso != None :
        tmp += "[주소정보 리스트] \n"
        i = 0 
        for i in range(0, len(result.juso)):
            tmp += str(result.juso[i].zipcode)+ "|"	  # 우편번호
            tmp += str(result.juso[i].sectionNum)+ "|"  # 새우편번호
            tmp += str(result.juso[i].roadAddr1)+ "|"   # 도로명주소
            tmp += str(result.juso[i].roadAddr2)+ "|"   # 도로명주소(참고항목)
            tmp += str(result.juso[i].jibunAddr)+ "|"   # 지번주소
            
            if result.juso[i].relatedJibun != None:
                tmp += "|"
                j = 0 
                for j in range(0, len(result.juso[i].relatedJibun)):   # 관련지번 목록 
                    tmp += str(result.juso[i].relatedJibun[j])+ " "
            
            tmp += "\n"
    print(tmp)   
except JusolinkException as JE:
    print("Exception Occur : [%d] %s" % (JE.code, JE.message))