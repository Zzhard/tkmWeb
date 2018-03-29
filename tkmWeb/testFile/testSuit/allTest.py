import  unittest
from config.config import basedir
from comm import HTMLTestRunner_PY3
suits=unittest.defaultTestLoader.discover(basedir+'/testFile/testcase')
outfile=open(basedir+'/report/Report.html','wb')
runner=HTMLTestRunner_PY3.HTMLTestRunner(
    stream=outfile,
    title='tkmWeb Test Report',
    description='太空马前端个人中心'
)

runner.run(suits)
outfile.close()
from comm import configEmail
configEmail.send_mail_report('太空马前端测试报告')