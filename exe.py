from PyQt5.QtGui import QTextCharFormat
import test_1
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QTableWidgetItem, QMessageBox, QTextEdit

# 建立主窗口和调用程序
app = QApplication(sys.argv)  # 创建应用程序对象
main_window = QMainWindow()  # 创建主窗口
JieMian = test_1.Ui_MainWindow1()  # 创建界面对象
JieMian.setupUi(main_window)  # 创建界面
main_window.setWindowTitle('点点')  # 设置窗口名

# 鼠标放在“shuru”文本框上产生提示信息
GuangBiao = JieMian.shuru.textCursor()  # 0.获取光标对象
shuru_tishi = QTextCharFormat()  # 1.创建一个 QTextCharFormat 对象
# 2.设置相关的参数
shuru_tishi.setToolTip("请勿随意输入内容")  # 设置ToolTip：光标停留在文本上面，光标右下的提示文本框
shuru_tishi.setFontFamily("幼圆")  # 设置字体
shuru_tishi.setFontPointSize(10)  # 设置字体大小
GuangBiao.insertText("运行日志", shuru_tishi)  # 插入文字

# 打开log.txt文件，文件存在则打开，不存在则创建后再打开，默认将log.txt文件创建在与py文件同一个目录下
# 设置mode='a'是将log.txt文件权限设置为可读写，模式为追加
# 设置encoding='utf-8'是为了正常显示中文
# log = open('log.txt', mode='a', encoding='utf-8')  # 创建文件对象
def LogOut(information):
    with open('log.txt', mode='a', encoding='utf-8') as log:
        log.write(information+'\n')
    print(information)

