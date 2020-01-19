import os #导入操作系统
import time

os.system("calc")
time.sleep(3)
os.system("tasklist | findstr WeChat")
#os.system("taskkill /f /im QQ.exe")#结束进程


