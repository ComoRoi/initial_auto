import requests
import json
import config
import time
from time import sleep
import datetime
import sys
import bot_message as bot
import db_handling as db

comConSet = config.COMMON_CONFIG
targetService = '[UI TEST] '
arguments = sys.argv

def currentTime():
    global nowDatetime
    nowDatetime = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')
    return nowDatetime

def setBotChannel(argument):
    global botChannel
    argunemts = sys.argv

    if len(arguments) ==1:
        print(currentTime() + targetService + "No Argument")
    
    elif arguments[1] == "s" or arguments[1] == "S":
        botChannel = comConSet['botShareChannel']

    elif arguments[1] == "h" or arguments[1] =="H":
        botChannel = comConSet['botHiddenChannel']
    
    else :
        print(currentTime() + targetService + "Unsupported Argument")
    
    return botChannel

setBotChannel(arguments)

if __name__ == '__main__':
    try :
        setBotChannel(arguments)

    except :
        print(currentTime() + targetService +"Bot Channel 설정에 실패했습니다.")

def errorReport(type, code, message):
    recordCount = db.selectCount()
    if recordCount == 0 :  # DB조회 후 기존 오류가 없을 경우
        db.setMessage(type, code, message)
        print(recordCount)

    elif recordCount >= 1 : # DB조회 후 기존 오류가 있을 경우
        errorCode = db.selectCode()
        if errorCode == code :  # DB조회 후 기존 오류가 현재 발생한 오류와 동일할 경우
            bot.post_message(botChannel, targetService + message)

        elif errorCode != code :  # DB조회 후 기존 오류가 현재 발생한 오류와 상이할 경우
            db.deleteAllMessage()  # all message를 삭제해야 함.
            db.setMessage(type, code, message)

def normalReport():
    recordCount = db.selectCount()
    if recordCount == 0 :  # DB조회 후 기존 오류가 없을 경우
        print("Service is normal")

    elif recordCount >= 1 : # DB조회 후 기존 오류가 있을 경우
        db.deleteAllMessage()  #


