import sys
print("----------------欢迎使用CAN报文转换工具交互模式----------------")
print("请输入CAN信号,格式为:startBit:length:minValue:maxValue:setValue")
print("例如：32:1:0:1:1")
print("或者省略minValue和maxValue：35：1：：：1")
print("信号输入结束请再按一次回车")

#十进制转换成二进制list
def octToBin(octNum, bit):
    while(octNum != 0):
        bit.append(octNum%2)
        octNum = int(octNum/2)
    for i in range(64-len(bit)):
        bit.append(0)

sig = []
startBit = []
length = []
setValue = []
#输入CAN信号
while True:
    input_str = input()
    if not len(input_str):
        break
    if(input_str.count(":")<4):
        print("输入格式错误，参数缺少setValue,请重新输入！")
        continue
    if(input_str.split(":")[4]==""):
        print("setValue参数不能为空，请重新输入！")
        continue
    sig.append(input_str)
    print(sig)
#解析CAN信号
for i in range(len(sig)):
    startBit.append(int(sig[i].split(":")[0]))
    length.append(int(sig[i].split(":")[1]))
    setValue.append(int(sig[i].split(":")[4]))
#CAN数组存放CAN报文值
# 0:8:::165
# 24:12:::1701
# 54:5:::25
print(startBit, length, setValue)
CAN = []
for i in range(64):
    CAN.append(-1)
for i in range(len(startBit)):
    #长度超过1Byte的情况，暂不支持
    if(length[i]>16):
        print("CAN信号长度超过2Byte，暂不支持！！！")
        sys.stdin.readline()
        sys.exit()
    #长度未超过1Byte的情况且未跨字节的信号
    if((startBit[i]%8 + length[i])<=8):
        for j in range(length[i]):
            bit = []
            #setValue的二进制值按字节位从低到高填
            octToBin(setValue[i],bit)
            print(bit)
            #填满字节长度值
            if(CAN[startBit[i]+j]==-1):
                CAN[startBit[i]+j] = bit[j]
            #字节存在冲突
            else:
                print(sig[i] + "字节位存在冲突，生成CAN报文失败！！！")
                sys.stdin.readline()
                sys.exit()
    #跨字节的信号
    else:
        #高位位数和低位位数
        highLen = 8 - startBit[i]%8
        lowLen = length[i] - highLen
        bit = []
        #setValue的二进制值按字节位从低到高填
        octToBin(setValue[i],bit)
        #先填进信号的高位
        for j1 in range(highLen):
            if(CAN[startBit[i]+j1]==-1):
                CAN[startBit[i]+j1] = bit[j1]
            #字节存在冲突
            else:
                print(sig[i] + "字节位存在冲突，生成CAN报文失败！！！")
                sys.stdin.readline()
                sys.exit()
        #再填进信号的低位
        for j2 in range(lowLen):
            if(CAN[(int(startBit[i]/8)-1)*8+j2]==-1):
                CAN[(int(startBit[i]/8)-1)*8+j2] = bit[highLen+j2]
            #字节存在冲突
            else:
                print(sig[i] + "字节位存在冲突，生成CAN报文失败！！！")
                sys.stdin.readline()
                sys.exit()
#剩余位默认值设为0
for i in range(64):
    if(CAN[i]==-1):
        CAN[i] = 0
#----------------将二进制list每隔8位转换成十六进制输出----------------
#其中，map()将list中的数字转成字符串，按照Motorola格式每隔8位采用了逆序
# ''.join()将二进制list转换成二进制字符串，int()将二进制字符串转换成十进制
#hex()再将十进制转换成十六进制，upper()转换成大写，两个lstrip()将"0X"删除,
#zfill()填充两位，输出不换行，以空格分隔
print(hex(int(''.join(map(str,CAN[7::-1])),2)).upper().lstrip("0").lstrip("X").zfill(2) + " ",end="")
print(hex(int(''.join(map(str,CAN[15:7:-1])),2)).upper().lstrip("0").lstrip("X").zfill(2) + " ",end="")
print(hex(int(''.join(map(str,CAN[23:15:-1])),2)).upper().lstrip("0").lstrip("X").zfill(2) + " ",end="")
print(hex(int(''.join(map(str,CAN[31:23:-1])),2)).upper().lstrip("0").lstrip("X").zfill(2) + " ",end="")
print(hex(int(''.join(map(str,CAN[39:31:-1])),2)).upper().lstrip("0").lstrip("X").zfill(2) + " ",end="")
print(hex(int(''.join(map(str,CAN[47:39:-1])),2)).upper().lstrip("0").lstrip("X").zfill(2) + " ",end="")
print(hex(int(''.join(map(str,CAN[55:47:-1])),2)).upper().lstrip("0").lstrip("X").zfill(2) + " ",end="")
print(hex(int(''.join(map(str,CAN[63:55:-1])),2)).upper().lstrip("0").lstrip("X").zfill(2))