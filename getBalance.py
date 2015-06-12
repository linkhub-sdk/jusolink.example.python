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
    print("주소링크 잔여포인트 확인")

    balance = jusolinkService.getBalance()

    print("잔여 포인트 : %f" % balance)
except JusolinkException as JE:

    print("Exception Occur : [%d] %s" % (JE.code, JE.message))