import  os
import logging
brotype= 2
url=''
username='13193205886'
password1='123456'
#数据库配置
host='aeasydb01.mysql.rds.aliyuncs.com'
user='p2pdev'
password='p2pdev'
database='p2psys_temp'
port=3306
#邮箱配置
sender='1178145190@qq.com'#发送方
receiver='1178145190@qq.com' #接收方
emailusername='1178145190@qq.com'#登录邮箱用户名
emailpassword='zxuhgazkykxwiedj'#登录邮箱密码
server='smtp.qq.com' #smtp服务器
#项目目录
basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#数据目录
datapath=os.path.join(basedir,'data')
#报告目录
reportpath=os.path.join(basedir,'report')
#日志配置
logdir=os.path.join(basedir,'log')
logpath=os.path.join(logdir,'log.txt')

logger=logging.getLogger('tkmWeb')
logger.setLevel(logging.DEBUG)
fh=logging.FileHandler(logpath,encoding='utf-8')
datafmt='%Y-%m-%d %H:%M:%S'
fm=logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt=datafmt)
fh.setFormatter(fm)
logger.addHandler(fh)
logging.getLogger('requests').setLevel(logging.WARNING)
if __name__ == '__main__':
    logger.info('this is test')
