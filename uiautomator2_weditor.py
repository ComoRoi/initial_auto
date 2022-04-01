####################################################
#                                                  #
#                  QA 자동화                         #
#                                                  #
####################################################
#####
import uiautomator2 as u2
import xml.etree.ElementTree as ET
import time
import json
import requests


# device_id정의
device_id = "2a55145a08027ece"
# device_id = "192.168.1.123:7912" #와이파이로 연결한 기기 접속 

# Device 접속
d = u2.connect(device_id)
# d.debug = True
# d.info
# print(d.alive)
assert d.alive, "디바이스가 정상적으로 연결되었습니다."
#print(device.info)
#assert not device.alive, "디바이스가 정상적으로 연결되지 않았습니다."

# 화면 열기
d.screen_on()
d.swipe_ext("up", 0.6)
d.press("home")

# initial 앱을 실행한다.
app_package = "com.sktelecom.myinitial"
d.app_start(app_package)

pid = d.app_wait(app_package, timeout=20.0) #실행대기
if not pid:
    print("com.example.android is not running")
    assert False, f"{app_package}가 정상적으로 수행되지 않았습니다."

#time.sleep(5) #대기
# 비밀번호 입력
d(text="1").click()
d(text="2").click()
d(text="3").click()
d(text="1").click()
d(text="2").click()
d(text="3").click()

# 수리비 영수증 및 내역서
d(resourceId="com.sktelecom.myinitial:id/nameTxt", text = "수리비 영수증 및 내역서").click()
d(resourceId="com.sktelecom.myinitial:id/labelTxt", text="삼성서비스센터").click()
d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="연결하기").click()
d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="동의 및 증명서 제출").click()
d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="확인").click()
d(resourceId="com.sktelecom.myinitial:id/selectChk", className="android.widget.CheckBox").click()
d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="발급 신청하기").click()
d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text = "저장하기")

print("1. Samsung SVC : test OK")

# Bot User OAuth Token
# xoxb-626859161682-2169397185921-yU0zeIWzF4z1qmaskndWqVGE


#bbb = d(resourceId="com.sktelecom.myinitial:id/txt_name")
#xml = d.dump_hierarchy(aaa.click())

#xml = aaa.page_source

#aaa.click()



d.app_stop_all()



# 참고자료
# https://www.fatalerrors.org/a/how-to-use-python-uiautomator2.html