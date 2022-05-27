####################################################
#                                                  #
#                  QA AUTOMATION                   #
#                                                  #
####################################################
#https://www.codetd.com/ko/article/11719595
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

#priConSet = config.KJK_CONFIG
priConSet = config.RSI_CONFIG
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

        pid = d.app_wait(comConSet['app_package'], timeout=3.0) #실행대기
        if not pid:
            print(currentTime() + targetService + "initial app is not running")
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
        sleep(1)
        if d(resourceId="com.sktelecom.myinitial:id/cb_do_not_show_days").exists():  
            d.xpath('//*[@text="확인"]').click()
            print("Close the pop-up window.")
        else :
            print("There is no pop-up window.")
    except :
        print("Pop-up windows error")

    try :
        #  고려대 학생증 발급
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_issuing_credentials").click()
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="대학 신분증").click()
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="고려대학교").click()
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="대학 신분증").click()
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/edit_university_id", text="학번 또는 교직원 번호 정보를 입력해주세요").set_text(priConSet['universityId'])
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/txt_sub_title", text="고려대학교").click()
        sleep(0.3) #대기
        d(text="약관동의 및 증명서 제출", className="android.widget.Button").click()
        sleep(0.3) #대기
        d(text="보관함에서 확인하기").click()
        sleep(0.3)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/img_qr", className="android.widget.ImageView").click()
        sleep(0.3)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/btn_close", className="android.widget.ImageButton").click()
        sleep(0.3)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/btn_close", className="android.widget.ImageButton").click()
    except :
        errCode = 2010
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        #  고려대 학생증 삭제
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_edit_id_credential").click()
        sleep(0.2) #대기
        d(className="android.widget.TextView", text="삭제").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/flow_end_btn").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_positive",text="예").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_save", text="저장").click()
        sleep(0.2) #대기
        d(className="android.widget.Button", text="예").click()
        sleep(0.2) #대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/btn_back"]').click()

    except :
        errCode = 2011
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        # 삼성 수리비 영수증 및 내역서
        sleep(0.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_issuing_credentials").click()
        sleep(1)  # 대기
        d(className="android.widget.TextView", text="증명서").click()
        sleep(1)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="수리비 영수증 및 내역서").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="삼성서비스센터").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="약관동의 및 증명서 제출").click()
        sleep(1) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="확인").click()
        sleep(1) #대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/lyt_card"]/android.view.ViewGroup[1]/android.view.View[2]').click()
        sleep(1)  # 대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/btn_back"]').click()
        sleep(1)  # 대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/lyt_end_button"]').click()

    except :
        errCode = 2020
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        # LG 수리비 영수증 및 내역서
        sleep(0.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_issuing_credentials").click()
        sleep(1) #대기
        d(className="android.widget.TextView", text="증명서").click()
        sleep(1)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="수리비 영수증 및 내역서").click()
        sleep(1)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="LG전자").click()
        sleep(1)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="약관동의 및 증명서 제출").click()
        sleep(1)  # 대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/lyt_card"]/android.view.ViewGroup[1]/android.view.View[2]').click()
        sleep(1)  # 대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/btn_back"]').click()
        sleep(1)  # 대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/lyt_end_button"]').click()

    except :
        errCode = 2021
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        ## 성적증명서 발급준비
        sleep(0.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_issuing_credentials").click()
        sleep(1)  # 대기
        d(className="android.widget.TextView", text="증명서").click()
        sleep(0.5)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="대학교 성적증명서").click()
        sleep(0.2)
        # 대학 검색
        d(text="찾으시는 대학명을 입력해주세요.").set_text("백석대학교")
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_search_query").click()
        sleep(1)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="백석대학교").click()
        sleep(0.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text="약관동의 및 증명서 제출").click()

        # 대학 웹뷰 확인
        sleep(0.3) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_gov_close").click()
        sleep(0.2)
        d(text="확인").click()
        sleep(0.2)
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/lyt_end_button"]').click()

    except :
        errCode = 2030
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        ## 출입권한증명 PS&M
        sleep(0.5)  # 대기
        d(resourceId="com.sktelecom.myinitial:id/btn_issuing_credentials").click()
        sleep(1)  # 대기
        d(className="android.widget.TextView", text="증명서").click()
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text="출입권한증명").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/txt_name", text = "PS&M").click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/confirmBtn", text = "약관동의 및 증명서 제출").click()
        sleep(0.2) #대기
        d.xpath('//*[@resource-id="com.sktelecom.myinitial:id/lyt_card"]/android.view.ViewGroup[1]/android.view.View[2]').click()
        sleep(0.2) #대기
        d(resourceId="com.sktelecom.myinitial:id/lyt_end_button").click()


    except :
        errCode = 2040
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        #행정안정부 전자문서지갑
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
        d(resourceId="com.sktelecom.myinitial:id/btn_navigate_to_go_certification_wallet", text="전자문서지갑").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/lyt_end_button").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/btn_navigate_to_go_certification_wallet_address", text="지갑주소").click()
        sleep(1.5) #대기
        d(text="주소 복사하기").click()
        sleep(1.5) #대기
        d(resourceId="com.sktelecom.myinitial:id/lyt_end_button").click()

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









