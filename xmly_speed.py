import requests
import os
import re
import time
from datetime import datetime
from dateutil import tz


def loadFileContent(downloadUrl) :
    return requests.get(downloadUrl).text

def writeFile(content,fileName):
    file = './'+fileName
    with open(file, 'w', encoding='utf-8') as f: f.write(content.replace('\r\n','\n'))

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

def readSecret(key):
    if key in os.environ and not os.environ[key].strip()=='':
        return os.environ[key]
    else:
        return None
    
def isOver():
    hourLimit = readSecret("XMLY_ACCUMULATE_HOURS")
    print("HOURS:"+str(safe_cast(hourLimit,int,-1)))
    if not hourLimit is None and safe_cast(hourLimit,int,0) > 0:
        date_stamp = (int(time.time())-57600) % 86400
        print(datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
        print("今日已过秒数: ", date_stamp)
        if date_stamp > int(hourLimit) * 60 * 60:
            return True
        else:
            return False
    else:
        print("未配置XMLY_ACCUMULATE_HOURS,因此不会对执行时长进行限制")
        return False

def isJumpIndex(idx):
    indexLimit = readSecret("XMLY_ACCUMULATE_INDEX")
    if indexLimit is None:
        return False
    xmly_accumulate_index = [safe_cast(i,int,-1) for i in indexLimit.split(",")]
    if len(xmly_accumulate_index) <= 0:
        xmly_accumulate_index = None
    index = -1
    try:
        index = xmly_accumulate_index.index(idx+1)
    except ValueError:
        print("无需禁用")
    return index >= 0

def run():
    cookies = readSecret("XMLY_SPEED_COOKIE")
    if cookies is None:
        print("无法获取Cookie,请在Secrets中配置XMLY_SPEED_COOKIE")
        return
    print("\n同步文件中...")
    webFileContent = loadFileContent(os.environ["SYNCURL"])
    print("\n文件同步完毕, 处理中...")
    agentPattern = re.compile(r'UserAgent = \"[\d\D]*?\"',re.S)

    rewriteAgent = readSecret("XMLY_ANDROID_AGENT")
    if rewriteAgent is None:
        rewriteAgent = 'UserAgent = "ting_1.8.30(Redmi+7,Android28)"'
    else:
        rewriteAgent = 'UserAgent = "' + rewriteAgent + '"'
    for idx,xmlyCookie in enumerate(cookies.split('\n')):
        executeContent = webFileContent.replace('xmly_speed_cookie = os.environ["XMLY_SPEED_COOKIE"]','xmly_speed_cookie = "' + xmlyCookie + '"',1)
        if xmlyCookie.find("_device=android") > 0:#此时表示是获取的安卓的cookie,需要使用安卓的agent
            executeContent = re.sub(agentPattern,rewriteAgent,executeContent)
        if isOver():
            executeContent = executeContent.replace("XMLY_ACCUMULATE_TIME = 1","XMLY_ACCUMULATE_TIME = 0",1).replace("action 自动刷时长打开","action 自动刷时长2指定关闭",1)
            print("已接受XMLY_ACCUMULATE_HOURS配置,为索引"+str(idx)+"的数据执行了禁用刷新时长的操作")
        if isJumpIndex(idx+1):
            executeContent = executeContent.replace("XMLY_ACCUMULATE_TIME = 1","XMLY_ACCUMULATE_TIME = 0",1).replace("action 自动刷时长打开","action 自动刷时长被指定关闭",1)
            print("已接受XMLY_ACCUMULATE_INDEX配置,为索引"+str(idx)+"的数据执行了禁用刷新时长的操作")
        writeFile(executeContent,'execute'+str(idx)+'.py')
        os.system('python ./'+'execute'+str(idx)+'.py')
    print("\n***************************\n文件全部执行完毕")
    exit(0) 

run()