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
    print("주소검색 단가 확인")

    unitCost = jusolinkService.getUnitCost()

    print("검색 단가 : %f" % unitCost)
except JusolinkException as JE:

    print("Exception Occur : [%d] %s" % (JE.code, JE.message))