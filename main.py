# import time
from PyQt5.QtGui import QTextCharFormat
import can_send
import exe
import sys
import com_send


# 鼠标放在“shuru”文本框上产生提示信息
GuangBiao = exe.JieMian.shuru.textCursor()  # 0.获取光标对象
shuru_tishi = QTextCharFormat()  # 1.创建一个 QTextCharFormat 对象
# 2.设置相关的参数
shuru_tishi.setToolTip("请勿随意输入内容")  # 设置ToolTip：光标停留在文本上面，光标右下的提示文本框
shuru_tishi.setFontFamily("幼圆")  # 设置字体
shuru_tishi.setFontPointSize(10)  # 设置字体大小
GuangBiao.insertText("运行日志", shuru_tishi)  # 插入文字


exe.JieMian.CanConnect.clicked.connect(can_send.CanSend)  # 点击can连接按钮发送can数据
exe.JieMian.CanSend.clicked.connect(can_send.CanReceive)  # 点击can发送按钮接收can数据
exe.JieMian.dianji.clicked.connect(com_send.XianShi)  # 点击串口连接按钮发送com口数据

if __name__ == "__main__":
    exe.main_window.show()  # 显示主窗口
    print('程序启动')
    sys.exit(exe.app.exec_())  # 直到窗口关闭再退出程序
