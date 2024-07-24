# import time
from PyQt5.QtGui import QTextCharFormat
import can_send
import exe
import sys
import com_send


exe.JieMian.CanConnect.clicked.connect(can_send.CanSend)  # 点击can连接按钮发送can数据
exe.JieMian.CanSend.clicked.connect(can_send.CanReceive)  # 点击can发送按钮接收can数据
exe.JieMian.dianji.clicked.connect(com_send.XianShi)  # 点击串口连接按钮发送com口数据

if __name__ == "__main__":
    exe.main_window.show()  # 显示主窗口
    print('程序启动')
    sys.exit(exe.app.exec_())  # 直到窗口关闭再退出程序
