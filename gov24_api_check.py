####################################################
#                                                  #
#                  QA AUTOMATION                   #
#                                                  #
####################################################


# -*- coding: utf-8 -*-
import json
import requests
import time
import bot_message as bot
import config
import resultCode
import sys
import datetime
import err_handling as err

now = datetime.datetime.now()
nowDatetime = now.strftime('[%Y-%m-%d %H:%M:%S] ')

arguments = sys.argv
priConSet = config.RSI_CONFIG
comConSet = config.COMMON_CONFIG
errConSet = resultCode.ERROR_CODE

targetService = '[API Server] '
makeToken = comConSet['gov24TokenUrl'] + 'ssw/token'
validationCheckWallet = comConSet['gov24Url'] + 'v1/wallets/' + priConSet['walletAddr']

myWalletUrl = comConSet['gov24Url'] + 'v1/myWallets/' + priConSet['walletAddr']
docs =  myWalletUrl + '/docs'
notifications = myWalletUrl + '/notifications'
popupMsgs = myWalletUrl + '/popupMsgs'

headers = {
    'Content-Type': 'application/json',
    'apiToken': '',
    'deviceId': ''
    }

data = {
    'walletAddr':''
}

# def setBotChannel(argument):
#     global botChannel
#     argunemts = sys.argv

#     if len(arguments) ==1:
#         print(nowDatetime + "No Argument")

#     elif arguments[1] == "s" or arguments[1] == "S":
#         botChannel = comConSet['botShareChannel']

#     elif arguments[1] == "h" or arguments[1] =="H":
#         botChannel = comConSet['botHiddenChannel']

#     else :
#         print(nowDatetime + "Unsupported Argument")

#     return botChannel

def reqCommand(command):
    global tokenKey
    timestamp = str(int(time.time()))
    # pStr = json.dumps().replace(" ", "")
    # body = str(pStr)

    if (command == makeToken):
        # 토근 발급
        response = requests.get(command)
        response1 = response.json()
        #print("Response: %s"%response1)
        jsonString = json.dumps(response1)
        jsonObject = json.loads(jsonString)
        tokenKey = jsonObject.get("result").get("apiToken")
        #print("tokenKey: %s"%tokenKey)

    else :
        headers['apiToken'] = tokenKey
        headers['deviceId'] = priConSet['devId']
        data['walletAddr'] = priConSet['walletAddr']
        response = requests.get(command, data=json.dumps(data), headers=headers)
        response1 = response.json()
        jsonString = json.dumps(response1)
        jsonObject = json.loads(jsonString)
        result = jsonObject.get("response").get("message")
        # print("result: %s" % result)
        


###############################################################################
# Main Function
###############################################################################

if __name__ == '__main__':

    # try :
    #     setBotChannel(arguments)

    # except :
    #     print(currentTime() + targetSerice +"Bot Channel 설정에 실패했습니다.")

    try :
        reqCommand(makeToken)

    except :
        print(nowDatetime + targetService +"Token 발급에 실패했습니다.")
        errCode = 3000
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        reqCommand(validationCheckWallet)   # 지갑 주소 유효성 확인

    except :
        print(nowDatetime + targetService + "Wallet 유효성체크에 실패했습니다.")
        errCode = 3001
        err.errorReport(targetService, errCode, errConSet[errCode])
    
    try :
        reqCommand(notifications)   # 개인 전자문서지갑 알림함 조회
    
    except :
        print(nowDatetime + targetService + "개인 전자문서지갑 알림함 조회에 실패했습니다.")
        errCode = 3002
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        reqCommand(docs)   # 전자증명서 발급 목록 조회

    except :
        print(nowDatetime + targetService + "전자증명서 발급 목록 조회에 실패했습니다.")
        errCode = 3003
        err.errorReport(targetService, errCode, errConSet[errCode])

    try :
        reqCommand(popupMsgs) # 개인 전자문서지갑 팝업함 조회
        #bot.post_message(botChannel, targetService + "API service is OK.")
        
    except :
        print(nowDatetime + targetService + "개인 전자문서지갑 팝업함 조회에 실패했습니다.")
        errCode = 3004
        err.errorReport(targetService, errCode, errConSet[errCode])


