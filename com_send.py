from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import exe


def XianShi():
    print('hello')
    # 串行端口配置
    SERIAL_PORT = 'COM3'  # 串行端口名称，根据实际情况修改
    BAUDRATE = 9600  # 波特率
    TIMEOUT = 5  # 超时时间（秒）
    client = ModbusClient(method='rtu', port=SERIAL_PORT, baudrate=BAUDRATE, timeout=TIMEOUT)  # 创建一个Modbus RTU客户端
    # 连接到Modbus服务器
    if client.connect():
        exe.JieMian.shuru.append('串口连接成功')
        # print("串口连接成功", file=exe.log)
        exe.LogOut('串口连接成功')
        # 读取设备号为1、起始地址为1、数量为10的连续寄存器
        response = client.read_holding_registers(address=1, count=10, unit=1)
        if not response.isError():
            exe.JieMian.shuru.append('读取成功')
            # print("读取成功", file=exe.log)
            exe.LogOut('读取成功')
        else:
            exe.JieMian.shuru.append('读取失败')
            # print("读取失败", file=exe.log)
            exe.LogOut('读取失败')

        # 向设备的单个寄存器写入数据
        write_response = client.write_register(address=1, value=25, unit=1)
        if not write_response.isError():
            exe.JieMian.shuru.append('写入成功')
            # print("写入成功", file=exe.log)
            exe.LogOut('写入成功')
        else:
            exe.JieMian.shuru.append('写入失败')
            # print("写入失败", file=exe.log)
            exe.LogOut('写入失败')
    else:
        exe.JieMian.shuru.append('连接失败')
        # print("连接失败", file=exe.log)
        exe.LogOut('连接失败')

    # client.close()  # 关闭连接
    exe.JieMian.shuru.append('串口连接断开')
    # print("串口连接断开", file=exe.log)
    exe.LogOut('串口连接断开')

    # log_txt = JieMian.shuru.toPlainText()  # 获取输入框日志信息
    # log.truncate(0)  # 清空文件内容
    # print(log_txt, file=log)  # 将日志信息写入log.txt文件
    # exe.log.close()  # 关闭文件

    # # can通讯 #
    # import can
    # def GetCan():
    #     com_no = JieMian.ComNo.toPlainText()  # 获取设备端口号
    #     device_type = JieMian.DeviceType.toPlainText()  # 获取can设备类型
    #     bit_rate = JieMian.BitRate.toPlainText()  # 获取can通讯波特率
    #     print(1)
    #     bus = can.interface.Bus(channel=com_no, interface=device_type, bitrate=bit_rate)  # 定义can总线接口类型
    #     print(2)
    #     can_id = JieMian.CanId.toPlainText()
    #     data_can = JieMian.CanData.toPlainText()
    #     print(3)
    #     can_test = can.Message(arbitration_id=can_id, data=data_can,
    #                            is_extended_id=False)  # 定义发送的报文。is_extended_id表示是否使用了大于11位的扩展帧ID，若超过则为True
    #     print(4)
    #     # 打开log.txt文件，文件存在则打开，不存在则创建后再打开，默认将log.txt文件创建在与py文件同一个目录下
    #     # 设置mode='a'是将log.txt文件权限设置为可读写
    #     # 设置encoding='utf-8'是为了正常显示中文
    #     log = open('log.txt', mode='a', encoding='utf-8')  # 创建文件对象
    #     JieMian.shuru.append('获取can配置成功')
    #     print('获取can配置成功', file=log)
    #     log.close()  # 关闭文件
    #     if JieMian.CanSend.clicked:
    #         bus.send(can_test)  # 发送报文 //总线名.send(报文名)
    #         log = open('log.txt', mode='a', encoding='utf-8')  # 创建文件对象
    #         JieMian.shuru.append('can数据已发送')
    #         print('can数据已发送', file=log)
    #         while True:
    #             print((bus.recv()), file=log)
    #
    # bus.recv()  # 接收报文 //总线名.recv()
    #
