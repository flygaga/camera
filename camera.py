import cv2
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# import smtplib #发送邮件
import smtplib
from smtplib import SMTP
import time

host = 'smtp.qq.com' #邮箱的接口
port = '25' #端口
pwd = 'neelrhh88******ch' #授权码
sender = '邮箱地址' #发送方
receiver = "邮箱地址" #接收方

path = r'./' #图像保存路径
images = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())

def GetPicture():
    """
    拍照保存图像
    """
    #创建一个窗口camera
    cv2.namedWindow('camera',1) #'1' 表示窗口不能随意拖动
    #调用摄像头
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read() #读取摄像头内容
    cv2.imwrite(path+images+".jpg",frame)  #保存到磁盘


    #释放摄像头
    cap.release()
    #关闭窗口
    cv2.destroyWindow("camera")

def SetMsg():
    '''
    设置邮件格式
    ：return：
    '''
    msg = MIMEMultipart('mixed')
    #标题
    msg['Subject'] = '电脑已开机'
    msg['From'] = sender
    msg['To'] = receiver
    #邮件正文内容
    text = '电脑已开机，请查收图片确认是否为本人'
    text_plain = MIMEText(text,'plain','utf-8') #正文转码
    msg.attach(text_plain)

    #图片
    SendImageFile = open(path+images+'.jpg','rb').read()
    image = MIMEImage(SendImageFile)
    image['Content-Disposition'] = 'attachment;filename="people.jpg"'
    msg.attach(image)
    return msg.as_string()

def SendEmail(msg):
    '''
    发送邮件
    ：msg :邮件内容
    :return
    '''
    try:
        smtp = smtplib.SMTP_SSL(host,port) #创建一个邮件服务
        # smtp.connect(host)
        smtp.login(sender,pwd)
        smtp.sendmail(sender,receiver,msg)
        time.sleep(3)
        smtp.quit() #退出邮件服务
    except smtplib.SMTPException as e:
        print("e")
#实现开机自启动
#打包实现启动  例：exe 

if __name__ == '__main__':
    # 1.拍照保存
    GetPicture()
    # 2. 设置邮件格式
    msg = SetMsg()
    # 3. 发送邮件
    SendEmail(msg)





