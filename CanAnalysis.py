import ctypes
from ctypes import wintypes
from cantools import database
import cantools

Struct_USBCAN2C = 4
STATUS_OK = 1


class Struct_INIT_CONFIG(ctypes.Structure):
    _fields_ = (("AccCode", wintypes.DWORD),
                ("AccMask", wintypes.DWORD),
                ("Reserved", wintypes.DWORD),
                ("Filter", ctypes.c_ubyte),
                ("Timing0", ctypes.c_ubyte),
                ("Timing1", ctypes.c_ubyte),
                ("Mode", ctypes.c_ubyte)
                )


class Struct_CAN_OBJ(ctypes.Structure):
    _fields_ = [("ID", ctypes.c_uint),
                ("TimeStamp", ctypes.c_uint),
                ("TimeFlag", ctypes.c_ubyte),
                ("SendType", ctypes.c_ubyte),
                ("RemoteFlag", ctypes.c_ubyte),
                ("ExternFlag", ctypes.c_ubyte),
                ("DataLen", ctypes.c_ubyte),
                ("Data", ctypes.c_ubyte * 8),
                ("Reserved", ctypes.c_ubyte * 3)
                ]


if __name__ == '__main__':
    db = database.load_file('./dbc/ARS408_can_database.dbc')
    # print(db.messages)
    CanDLLName = './dll/ECanVci64.dll'
    canDLL = ctypes.CDLL(CanDLLName)
    ret = canDLL.OpenDevice(Struct_USBCAN2C, 0, 0)
    if ret != STATUS_OK:
        print('调用 Struct_OpenDevice出错\r\n')
    # 初始0通道
    struct_initconfig = Struct_INIT_CONFIG(0, 0xFFFFFFFF, 0, 0, 0, 0x1C, 0)
    ret = canDLL.InitCAN(Struct_USBCAN2C, 0, 0, ctypes.byref(struct_initconfig))
    if ret != STATUS_OK:
        print('调用 Struct_InitCAN出错\r\n')

    ret = canDLL.StartCAN(Struct_USBCAN2C, 0, 0)
    if ret != STATUS_OK:
        print('调用 Struct_StartCAN出错\r\n')

    # 初始1通道
    ret = canDLL.InitCAN(Struct_USBCAN2C, 0, 1, ctypes.byref(struct_initconfig))
    if ret != STATUS_OK:
        print('调用 Struct_InitCAN 1 出错\r\n')
    ret = canDLL.StartCAN(Struct_USBCAN2C, 0, 1)
    if ret != STATUS_OK:
        print('调用 Struct_StartCAN 1 出错\r\n')

    # 通道0发送数据
    # ubyte_array = ctypes.c_ubyte * 8
    # a = ubyte_array(1, 2, 3, 4, 5, 6, 7, 64)
    # ubyte_3array = ctypes.c_ubyte * 3
    # b = ubyte_3array(0, 0, 0)
    # struct_can_obj = Struct_CAN_OBJ(0x0, 0, 0, 1, 0, 0, 8, a, b)
    # ret = canDLL.Transmit(Struct_USBCAN2C, 0, 0, ctypes.byref(struct_can_obj), 1)
    # print(ret, '6')
    # if ret != STATUS_OK:
    #     print('调用 Struct_Transmit 出错\r\n')

    # 通道0接收数据
    ubyte_array = ctypes.c_ubyte * 8
    a = ubyte_array(0, 0, 0, 0, 0, 0, 0, 1)
    ubyte_3array = ctypes.c_ubyte * 3
    b = ubyte_3array(0, 0, 0)
    struct_can_obj = Struct_CAN_OBJ(0x0, 1, 1, 0, 0, 0, 8, a, b)
    while True:
        # print('调用 Struct_Receive 出错\r\n')
        ret = canDLL.Receive(Struct_USBCAN2C, 0, 0, ctypes.byref(struct_can_obj), 1, 10)
        if ret > 0:
            if struct_can_obj.ID == 1547:
                # print(struct_can_obj.ID)
                # print(struct_can_obj.DataLen)
                struct_can_obj_data = list(struct_can_obj.Data)
                for i in range(len(struct_can_obj_data)):
                    print(bin(int(struct_can_obj_data[i], 10)))
                    # struct_can_obj_data = [hex(i) for i in struct_can_obj_data]
                    # print(struct_can_obj_data)


    # 通道1接收数据
    # a = ubyte_array(0, 0, 0, 0, 0, 0, 0, 1)
    # struct_can_obj = Struct_CAN_OBJ(0x0, 0, 0, 1, 0, 0, 8, a, b)
    # ret = canDLL.Receive(Struct_USBCAN2C, 0, 1, ctypes.byref(struct_can_obj), 1, 50)
    # while ret <= 0:
    #     print('调用 Struct_Receive 出错\r\n')
    #     ret = canDLL.Receive(Struct_USBCAN2C, 0, 1, ctypes.byref(struct_can_obj), 1, 50)
    # if ret > 0:
    #     print(struct_can_obj.DataLen)
    #     print(list(struct_can_obj.Data))

    # 关闭
    canDLL.CloseDevice(Struct_USBCAN2C, 0)
