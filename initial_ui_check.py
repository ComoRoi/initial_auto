####################################################
#                                                  #
#                  QA AUTOMATION                   #
#                                                  #
####################################################

import uiautomator2 as u2
import xml.etree.ElementTree as ET
import time
from time import sleep
import datetime
import json
import requests
import bot_message as bot
import config
import resultCode
import sys
import err_handling as err

priConSet = config.KJK_CONFIG
# priConSet = config.RSI_CONFIG
comConSet = config.COMMON_CONFIG
errConSet = resultCode.ERROR_CODE
targetService = '[UI TEST] '

# Device 접속
d = u2.connect(priConSet['device_id'])
d.app_stop_all()

# d.debug = True
# d.info
# print(d.alive)

def currentTime():
    global nowDatetime
    nowDatetime = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')
    return nowDatetime


# 화면 열기
d.screen_on()
d.swipe_ext("up", 0.6)
d.press("home")


startTimestamp = time.time()
startTime = datetime.datetime.fromtimestamp(int(startTimestamp)).strftime('%Y-%m-%d %H:%M:%S')
print (currentTime() + targetService + "Start time    : " + str(startTime))

# initial 앱을 실행한다.

if __name__ == '__main__':

    try :
        d.app_start(comConSet['app_package'])

        pid = d.app_wait(comConSet['app_package'], timeout=20.0) #실행대기
        if not pid:
            print(currentTime() + targetService + "com.example.android is not running")
            assert False, f"{comConSet['app_package']}가 정상적으로 수행되지 않았습니다."

        d(resourceId="com.sktelecom.myinitial:id/quitButton").click()

    except :
        sleep(1)

    try :
        # 비밀번호 입력
        d(text="1").click()
        sleep(0.1)
        d(text="2").click()
        sleep(0.1)
        d(text="3").click()
        sleep(0.1)
        d(text="1").click()
        sleep(0.1)
        d(text="2").click()
        sleep(0.1)
        d(text="3").click()

    except :
        errCode = 1000
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        #  고려대 학생증 발급
        sleep(1) #대기
        d.swipe(0.691, 0.236, 0.075, 0.236, 0.1)
        sleep(0.3)
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/list_id_credential"]/android.view.ViewGroup[2]/androidx.cardview.widget.CardView[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/contentPanel").click()
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/iconImg").click()
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="연결하기").click()
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/edit_university_id", text="학번 또는 교직원 번호를 입력해주세요").set_text(priConSet['universityId'])
        d.swipe_ext("up", 0.6)
        sleep(0.3) #대기
        d(text="약관동의 및 증명서 제출", className="android.widget.Button").click()
        sleep(0.3) #대기
        d(text="저장하기").click()

    except :
        errCode = 2010
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        #  고려대 학생증 삭제
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/titleRightSetBtn").click()
        sleep(0.2) #대기
        d(text="삭제").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/flow_end_btn").click()
        sleep(0.2) #대기
        d(text="예").click()
        sleep(0.2) #대기
        d(text="저장").click()
        sleep(0.2) #대기
        d(text="예").click()
        sleep(0.2) #대기
        d(className="android.widget.ImageButton").click()

    except :
        errCode = 2011
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        # 삼성 수리비 영수증 및 내역서
        sleep(0.5) #대기
        d.swipe(0.351, 0.665, 0.351, 0.105, 0.1)
        sleep(1) #대기
        #d(resourceId="com.sktelecom.myinitial:id/nameTxt", text = "수리비 영수증 \n및 내역서").click()
        d(resourceId="com.sktelecom.myinitial:id/txt_shortcut_name", text = "수리비 영수증 및 내역서").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/labelTxt", text="삼성서비스센터").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="연결하기").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="약관동의 및 증명서 제출").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="확인").click()
        sleep(1) #대기
        d(text="확인").click()
        #d(resourceId="com.sktelecom.myinitial:id/closeBtn").click()
        # d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="확인").click()
        #sleep(0.1) #대기
        #d(resourceId="com.sktelecom.myinitial:id/selectChk").click()
        #sleep(0.1) #대기
        #d(resourceId="com.sktelecom.myinitial:id/closeBtn").click()
        #sleep(0.1) #대기
        #d(resourceId="com.sktelecom.myinitial:id/selectChk", className="android.widget.CheckBox").click()
        #d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="발급 신청하기").click()
        #d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text = "저장하기").click()
        #d(resourceId="com.sktelecom.myinitial:id/closeBtn").click()

    except :
        errCode = 2020
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        # LG 수리비 영수증 및 내역서
        sleep(0.5) #대기
        d.swipe(0.351, 0.665, 0.351, 0.105)
        sleep(1) #대기
        #d(resourceId="com.sktelecom.myinitial:id/nameTxt", text = "수리비 영수증 \n및 내역서").click()
        d(resourceId="com.sktelecom.myinitial:id/txt_shortcut_name", text = "수리비 영수증 및 내역서").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/labelTxt", text="LG전자").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="연결하기").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="약관동의 및 증명서 제출").click()
        sleep(1) #대기
        #d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="확인").click()
        d(text="확인").click()

    except :
        errCode = 2021
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        ## 성적증명서 발급준비
        sleep(0.5) #대기
        ## 출입권한증명 PS&M
        d(text="교육").click()
        d(resourceId="com.sktelecom.myinitial:id/txt_shortcut_name", text="대학교 성적증명서").click()
        sleep(0.2)
        # 대학 검색
        d(text="대학명을 검색해주세요").set_text("백석대")
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/searchBtn").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/labelTxt", text="백석대학교").click()
        sleep(0.2) #대기
        d(text="연결하기").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="약관동의 및 증명서 제출").click()

        # 대학 웹뷰 확인
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_gov_close").click()
        sleep(0.2)
        d(text="확인").click()

    except :
        errCode = 2030
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        ## 출입권한증명 PS&M
        d(text = "신분·출입").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/txt_shortcut_name", text = "출입권한증명").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/labelTxt", text = "PS&M").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text = "연결하기").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text = "약관동의 및 증명서 제출").click()
        sleep(0.2) #대기
        #d.xpath('//android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]').click() **********
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/lyt_card"]/android.view.ViewGroup[1]/android.view.View[2]').click()
    except :
        errCode = 2040
        err.errorReport(targetService, errCode, errConSet[errCode])

    # try :
    #     ## 고려대 출입증 - 숏컷
    #     d(text = "신분·출입").click()
    #     sleep(0.2) #대기
    #     d(resourceId="com.sktelecom.myinitial:id/txt_shortcut_name", text = "대학 신분증").click()
    #     d(resourceId="com.sktelecom.myinitial:id/labelTxt", text = "고려대학교").click()
    #     #d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="연결하기").click()  ****************
    #     d(index = "2").click()
    #     d(resourceId="com.sktelecom.myinitial:id/closeBtn").click()
    #
    # except :
    #     errCode = 2012
    #     err.errorReport(targetService, errCode, errConSet[errCode])


    # try :
    #     ## proDS 자격증
    #     d(resourceId="com.sktelecom.myinitial:id/txt_shortcut_name", text = "ProDS 자격증").click()
    #     d(resourceId="com.sktelecom.myinitial:id/labelTxt", text = "멀티캠퍼스 ProDS").click()
    #     d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text = "연결하기").click()
    #       작성중 Cloud SDK 서비스는 연결이 되지 않아 중단함.


    try :
        #행정안정부 전자문서지갑
        sleep(1) #대기
        d.swipe(0.151, 0.305, 0.351, 0.665, 0.1)
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_navigate_to_go_certification_apply", text="증명서 신청").click()
        sleep(1.5) #대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/list_appliable_certificate"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.Button[1]').click()
        sleep(1.5) #대기
        d(text="발급 신청하기").click()
        sleep(1.5) #대기
        d(text="뒤로가기").click()
        sleep(1.5) #대기
        d(text="예").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/lyt_end_button").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_navigate_to_go_certification_wallet", text="정부 전자문서지갑").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/lyt_end_button").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_navigate_to_go_certification_wallet_address", text="지갑주소").click()
        sleep(1.5) #대기
        d(text="주소 복사하기").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/lyt_end_button").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/txt_issuable_certificate_name", text = "건강보험자격득실확인서").click()
        sleep(1.5) #대기
        d(text="발급 신청하기").click()
        sleep(1.5) #대기
        d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]').click()
        d(text="뒤로가기").click()
        sleep(1.5) #대기
        d(text="예").click()

    except :
        errCode = 2000
        err.errorReport(targetService, errCode, errConSet[errCode])

# 앱 종료
d.app_stop_all()

endTimestamp = time.time()
endTime = datetime.datetime.fromtimestamp(int(endTimestamp)).strftime('%Y-%m-%d %H:%M:%S')
print (currentTime() + targetService + "End time      : " + str(endTime))
deltaTimestamp = int(endTimestamp) - int(startTimestamp)

print (currentTime() + targetService + "Duration time : " + str(deltaTimestamp) + "sec")

if comConSet['thresholdValuesForDurationTime'] < deltaTimestamp :
    print (currentTime() + targetService + "Test Result   : Fail !! (initial service is very slow.)")
    errCode = 9999
    err.errorReport(targetService, errCode, errConSet[errCode])

else :
    print (currentTime() + targetService + "Test Result   : Success !!")
    err.normalReport()
    #bot.post_message(botChannel, targetService + "initial service is OK.")
