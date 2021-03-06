import unittest
import os
import time
import HTMLTestRunnerCN

if __name__=='__main__':
    report_path=os.path.dirname(os.path.abspath('.'))+'/test_report/'
#报告路径

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#系统时间

    HtmlFile=report_path+now+"HTMLtemplate.html"
    fp=open(HtmlFile,'wb')

    suite=unittest.TestLoader().discover("testcase")
    runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title=u"邮招聘自动化测试报告",description=u"用例测试情况")
    runner.run(suite)
    fp.close()
