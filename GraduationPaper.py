import os
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StudentScore(object):
    def __init__(self, className: str, studentName: str , regularScore: float, middleScore: float ,finalScore: float):
        self.className=className
        self.studentName=studentName
        self.regularScore=regularScore
        self.middleScore=middleScore
        self.finalScore=finalScore
        

class EduSys:
    url='https://zhxy.jxyjxy.com:8078/lyuapServer/login?service=http://218.87.96.236:4106/shiro-cas'
    user_xpath='//*[@id="userName"]'
    psw_xpath='//*[@id="password"]'
    login_xpath='/form/button[1]'
    auth_xpath='//*[@id="captcha"]'
    def start_Edge(self):
        self.driver=webdriver.Edge()        
        self.driver.implicitly_wait(10)# seconds,等待时间,如果网页元素节点没加载,默认等待10s。
        self.driver.get(url=EduSys.url)
        assert "统一身份认证平台" in self.driver.title

        #找到用户名输入栏
        user_name=self.driver.find_element(By.XPATH,self.user_xpath)
        user_name.send_keys("202109010")
        #找到密码输入栏
        psw=self.driver.find_element(By.XPATH,self.psw_xpath)
        psw.send_keys("pxa@961224")
        #找到验证码输入栏
        authCode=self.driver.find_element(By.XPATH,self.auth_xpath)
        user_input=input('请输入验证码:\n')
        authCode.send_keys(user_input)
        authCode.send_keys(Keys.ENTER)


    def read_excel(self,path):
        """"读取excel成绩数据"""
        df=pd.read_excel(path)
        StudentScore.studentName=df['学生姓名']
        StudentScore.className=df['班级']
        StudentScore.regularScore=df['指导']
        StudentScore.middleScore=df['评阅']
        StudentScore.finalScore=df['答辩']

    def run(self):
        try:
            while 1:
                path='毕业论文成绩汇总表.xlsx'
                if os.path.exists(path):
                    self.read_excel(path)
                    self.start_Edge()
                else:
                    print('文件不存在')
        except Exception as e:
            import traceback
            print(traceback.print_exc())

if __name__=='__main__':
    Edu_sys=EduSys()
    Edu_sys.run()