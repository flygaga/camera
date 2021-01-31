# 思路
1、通过opencv调用摄像头拍照保存图像到本地

2、用email库构造邮件内容，保存图片以附件形式插入邮件内容

3、用smtplib库发送邮件到指定邮箱

4、生成 .exe 文件

5、设置开机自启（每次开机自动运行，启动相机，拍下照片发送到指定邮箱）

# 导入工具
import cv2  # pip install opencv-python -i {指定镜像源}   控制摄像头

from email.mime.image  imort  MIMEImage #用来构造邮件内容的库

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import smtplib   #发送邮件

# 编译环境
系统：Windows10

软件：Miniconda3-latest-Windows-x86_64

模块：opencv-python smtplib  numpy email pyinstaller

# 生成exe文件
pyinstaller -F -w path/camera.py

# 设置开机自启
1.右击exe 创建快捷方式

2.win+r 输入以下命令 shell:startup 点击确定打开一个文件夹

3.将生成的快捷文件复制到打开的文件中，下次开机exe程序就会自动启动





python代码实现调用摄像头，并拍照发送邮件
