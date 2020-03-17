import pyvisa
import time
import ctypes
import math


class RSC:
    def __init__(self, ip, att, freq):
        self.ip = ip
        self.att = att
        self.freq = freq
        self.address = 'TCPIP::%s::inst0::INSTR' % self.ip
        self.resourceManager = pyvisa.ResourceManager()

    def open(self):
        self.instance = self.resourceManager.open_resource(self.address)

    def close(self):
        if self.instance is not None:
            self.instance.close()
            self.instance = None

    def reset(self):
        self.instance.write('*RST')

    def read_idn(self):
        idn = self.instance.query('*IDN?')
        print(idn)
        return idn

    def set_att(self):
        self.instance.write('ATT1:ATT %s' % self.att)

    def set_freq(self):
        self.instance.write('ATT1:FREQ %s' % self.freq)

    def set_corr_on(self):
        self.instance.write('ATT1:CORR ON')

    def set_corr_off(self):
        self.instance.write('ATT1:CORR OFF')


class HMP:
    def __init__(self):
        self.resourceManager = pyvisa.ResourceManager()

    def open(self, ip):
        address = 'TCPIP::%s::5025::SOCKET' % ip
        self.instance = self.resourceManager.open_resource(address, read_termination='\n')

    def close(self):
        if self.instance is not None:
            self.instance.close()
            self.instance = None

    def reset(self):
        self.instance.write('*RST')

    def set_default(self, chan, volt, curr):
        self.instance.write('INST:NSEL %s' % chan)
        self.instance.write('VOLT %s' % volt)
        self.instance.write('CURR %s' % curr)

    def return_status_idn(self):
        idn = self.instance.query('*IDN?')
        print('设备IDN号为：' + idn)
        return idn

    def return_status_chan(self):
        chan = self.instance.query('INST:NSEL?')
        print('当前选择的通道：' + chan)
        return chan

    def return_status_volt(self):
        volt = self.instance.query('VOLT?')
        print('当前设置的电压值：' + volt)
        return volt

    def return_status_curr(self):
        curr = self.instance.query('CURR?')
        print('当前设置的电流值：' + curr)
        return curr

    def return_status_volt_output(self):
        volt = self.instance.query('MEAS:VOLT?')
        print('当前输出的电压值：' + volt)
        return volt

    def return_status_curr_output(self):
        curr = self.instance.query('MEAS:CURR?')
        print('当前输出的电流值：' + curr)
        return curr

    def select_chan(self, chan):
        self.instance.write('INST:NSEL %s' % chan)

    def set_volt(self, volt):
        self.instance.write('VOLT %s' % volt)

    def set_curr(self, curr):
        self.instance.write('CURR %s' % curr)

    def set_chan_on(self):
        self.instance.write('OUTP:SEL ON')

    def set_chan_off(self):
        self.instance.write('OUTP:SEL OFF')

    def set_output_on(self):
        self.instance.write('OUTP ON')

    def set_output_off(self):
        self.instance.write('OUTP OFF')


class FSW:
    def __init__(self, ip):
        self.ip = ip
        self.address = 'TCPIP0::%s::inst0::INSTR' % self.ip
        self.resourceManager = pyvisa.ResourceManager()

    def open(self):
        self.instance = self.resourceManager.open_resource(self.address)

    def close(self):
        if self.instance is not None:
            self.instance.close()
            self.instance = None

    def reset(self):
        self.instance.write('*RST')

    def read_idn(self):
        idn = self.instance.query("*IDN?")
        print(idn)


class RTO:
    def __init__(self, ip):
        self.ip = ip
        self.address = 'TCPIP0::%s::inst0::INSTR' % self.ip
        self.resourceManager = pyvisa.ResourceManager()

    def open(self):
        self.instance = self.resourceManager.open_resource(self.address)

    def close(self):
        if self.instance is not None:
            self.instance.close()
            self.instance = None

    def reset(self):
        self.instance.write('*RST')

    def read_idn(self):
        idn = self.instance.query('*IDN?')
        print(idn)
        return idn


class SMW:
    def __init__(self, ip):
        self.ip = ip
        self.address = 'TCPIP::%s::inst0::INSTR' % self.ip
        self.resourceManager = pyvisa.ResourceManager()

    def open(self):
        self.instance = self.resourceManager.open_resource(self.address)

    def close(self):
        if self.instance is not None:
            self.instance.close()
            self.instance = None

    def reset(self):
        self.instance.write('*RST')

    def read_idn(self):
        idn = self.instance.query('*IDN?')
        print(idn)
        return idn


class ARTS:
    def __init__(self):
        self.dll = ctypes.CDLL('./dll/D4ARTS6x64.dll')
        self.status = 0
        self.output = 0
        self.tr = 0
        self.mode = 1
        self.freq = 0
        self.gain_s = 46
        self.rut_distance = 0

    def connect(self, ip):
        if self.status == 0:
            self.dll.Connect(ip.encode('utf-8'))
            self.status = 1
            print('ARTS连接成功')
        else:
            print('ARTS已连接')

    def disconnect(self):
        if self.status == 1:
            self.dll.Disconnect()
            self.status = 0
            print('ARTS成功断开连接')
        else:
            print('ARTS未连接')

    def check_connect_status(self):
        self.status = self.dll.CheckConnectionStatus()
        if self.status == 1:
            print('系统连接中......')
        else:
            print('系统未连接')
        return self.status

    def reboot(self):
        result = self.dll.Reboot()
        if result == 0:
            print('系统开始重启......')
        return result

    def set_freq(self, freq):
        self.freq = freq
        result = self.dll.SetRfFreq_kHz(freq)
        if result == 0:
            print('频率已设置为%dKHz' % freq)
        return result

    def set_trims(self, gain_trim, range_trim, rut_distance):
        self.rut_distance = rut_distance
        result = self.dll.SetTrims(gain_trim, gain_trim, gain_trim, gain_trim, range_trim, range_trim, range_trim, range_trim, rut_distance)
        if result == 0:
            print('已设置GainTrim为%ddB，已设置RangeTrim为%dm,已设置RUTDistance为%dm ' % (gain_trim, range_trim, rut_distance))
        return result

    def set_rx_attenuation(self, attenuation):
        result = self.dll.SetRxAttn(attenuation)
        if result == 0:
            print('RF Attenuation已成功设置为%ddB' % attenuation)
        return result

    def set_adc_saturation_threshold(self, threshold):
        result = self.dll.SetAdcSatThreshBackoff(threshold)
        if result == 0:
            print('ADC采样阈值已成功设置为%ddB' % threshold)
        return result

    def set_mode_static(self):
        result = 1
        if self.mode == 1:
            print('当前为静态工作模式')
        else:
            result = self.dll.SetStaticMode(1)
            if result == 0:
                self.mode = 1
                print('已设置为静态工作模式')

    def set_mode_dynamic(self):
        result = 1
        if self.mode == 0:
            print('当前为动态工作模式')
        else:
            result = self.dll.SetStaticMode(0)
            if result == 0:
                self.mode = 0
                print('已设置为动态工作模式')
        return result

    def set_tx_chan_static(self, speed_ch1, speed_ch2, speed_ch3, speed_ch4,
                           rcs_ch1, rcs_ch2, rcs_ch3, rcs_ch4,
                           range_ch1, range_ch2, range_ch3, range_ch4):
        # Set Tx Channel Parameters in "normal operating units": Speed (kph), Gain (dB), Range (m).
        wave_speed = 3*10**8
        wave_period = 1/(self.freq*10**6)
        gama = wave_speed * wave_period
        gain_ch1 = rcs_ch1 * 4 * math.pi * range_ch1**4 / (self.gain_s**2 * gama**2 * (range_ch1 + self.rut_distance)**4)
        gain_ch2 = rcs_ch2 * 4 * math.pi * range_ch2**4 / (self.gain_s**2 * gama**2 * (range_ch2 + self.rut_distance)**4)
        gain_ch3 = rcs_ch3 * 4 * math.pi * range_ch3**4 / (self.gain_s**2 * gama**2 * (range_ch3 + self.rut_distance)**4)
        gain_ch4 = rcs_ch4 * 4 * math.pi * range_ch4**4 / (self.gain_s**2 * gama**2 * (range_ch4 + self.rut_distance)**4)
        result = self.dll.SetTxChanStaticCfg(speed_ch1, speed_ch2, speed_ch3, speed_ch4,
                                             gain_ch1, gain_ch2, gain_ch3, gain_ch4,
                                             range_ch1, range_ch2, range_ch3, range_ch4)

    def set_chan_dynamic(self, start_speed_ch1, start_speed_ch2, start_speed_ch3, start_speed_ch4,
                         stop_speed_ch1, stop_speed_ch2, stop_speed_ch3, stop_speed_ch4,
                         start_range_ch1, start_range_ch2, start_range_ch3, start_range_ch4,
                         stop_range_ch1, stop_range_ch2, stop_range_ch3, stop_range_ch4,
                         rcs_ch1, rcs_ch2, rcs_ch3, rcs_ch4, r4_enable, waveform_formate_code, ):
        # // enable 1/R^4 power attenuation
        # // 0=no file created; 1=binary file; 2=ASCII file
        # // can be NULL if no file created



    def set_tx_chan_enable(self, tx1, tx2, tx3, tx4):
        # Transmit Channel Enable. Enables (1) or disables (0) each of the four transmit channels.
        result = self.dll.TxChanEnable(tx1, tx2, tx3, tx4)
        if result == 0:
            print('通道工作设置成功')
            if tx1 == 1:
                print('通道1打开')
            else:
                print('通道1关闭')
            if tx2 == 1:
                print('通道2打开')
            else:
                print('通道2关闭')
            if tx3 == 1:
                print('通道3打开')
            else:
                print('通道3关闭')
            if tx4 == 1:
                print('通道4打开')
            else:
                print('通道4关闭')
        return result

    def download_wave_form(self, waveform_format_code, waveform_filename):
        # // 0=DLL internal memory; 1=binary file; 2=ASCII file
        # // can be NULL if no file used
        result = self.dll.DownloadWaveform(waveform_format_code, waveform_filename)
        if result == 0:
            print('波形入口已选择')
            if waveform_format_code == 0:
                print('波形入口为当前界面')

    def run_wave_form(self, continuous, ext_trigger):
        # // 0=one-shot playback; 1=continuously looping playback
        # // 0=start playback immediately; 1=wait for external trigger
        result = self.dll.RunWaveform(continuous, ext_trigger)
        if result == 0:
            print('波形模式已载入')
            if continuous == 0:
                print('已选择单次模式')
            else:
                print('已选择循环模式')
            if ext_trigger == 0:
                print('发射模式不载入外部触发信号')
            else:
                print('发射模式载入外部触发信号')

    def reset(self):
        result = self.dll.Reset()
        if result == 0:
            print('系统完成重置')
        return result

    def set_tr_on(self):
        result = 1
        if self.tr == 0:
            result = self.dll.SetTrEn(1)
            self.tr = 1
            if result == 0:
                print('ARTS成功打开T/R模块')
        else:
            print('ARTS已打开T/R模块')
        return result

    def set_tr_off(self):
        result = 1
        if self.tr == 1:
            result = self.dll.SetTrEn(0)
            self.tr = 0
            if result == 0:
                print('ARTS成功关闭T/R模块')
        else:
            print('ARTS未打开T/R模块')
        return result

    def set_output_on(self):
        result = 1
        if self.output == 0:
            result = self.dll.SetSynthRFOutput(1)
            self.output = 1
            if result == 0:
                print('ARTS成功打开RF发射')
        else:
            print('ARTS已打开RF发射')
        return result

    def set_output_off(self):
        result = 1
        if self.output == 1:
            result = self.dll.SetSynthRFOutput(0)
            self.output = 0
            if result == 0:
                print('ARTS成功关闭RF发射')
        else:
            print('ARTS已关闭RF发射')
        return result


class TurnTable:
    # nAxis - 轴：nAxis == 2 时为俯仰轴；
    # nAxis - 轴：nAxis == 1 时为方位轴；
    # fSetPos：单位为°（对转台而言）或者mm(对扫描架而言)
    # fSetVel：° / s（对转台而言）或者mm / s(对扫描架而言)
    # iDevice：设备地址号，转台iDevice = 0。
    def __init__(self):
        self.dll = ctypes.CDLL('./dll/PcommDllx64.dll')
        self.status = 0

    def connect(self):
        # // 参数：iDevice –设备地址号，对本扫描架来说iDevice = 0；
        # // 返回值：true - 成功、false - 失败
        if self.status == 0:
            self.dll.ConnectImac(0)
            self.status = 1
            print('转台连接成功')
        else:
            print('转台已连接')

    def disconnect(self):
        # // 参数：iDevice –设备地址号；
        # // 返回值：true - 成功、false - 失败
        if self.status == 1:
            self.dll.DisConnectImac()
            self.status = 0
            print('转台成功断开连接')
        else:
            print('转台未连接')

    def move_to_position(self, n_axis, set_pos, set_vel, b_abs=True):
        # // 参数：iDevice –设备地址号；
        # // 参数：nAxis  –轴号；
        # // 参数：fSetPos –对应轴号所设置的位置值；
        # // 参数：fSetVel –对应轴号所设置的速度值；
        # // 参数：bIsAbs –对于轴号运动方式，true - 绝对运动，false - 相对运动；
        # // 返回值：true - 成功、false - 失败
        result = 0
        if self.status == 1:
            result = self.dll.MoveDeviceToPos(0, n_axis, set_pos, set_vel, b_abs)
            if result == 1:
                print('开始常规模式转动')
        return result

    def move_to_position_by_type(self, device, n_axis, to_start, to_end, to_speed, start_equ, end_equ, step_pos, speed, delta_step, i_time):
        # // 参数：iDevice –设备地址号；
        # // 参数：nAxis –轴号；
        # // 参数：fToStart - ---各个轴所要运动的距离值，位置值在发送脉冲起始角之前，单位为mm
        # // 参数：fToEnd - ---各个轴所要运动的距离值，位置值在发送脉冲起始角之前，单位为mm
        # // 参数：fToSpeed - ---各个轴到fToStart位置时的速度，单位为mm / s
        # // 参数：fStartEqu - ---各个轴发送脉冲的起始位置值，单位为mm
        # // 参数：fEndEqu - ---各个轴发送脉冲的终止位置值，单位为mm
        # // 参数：fStepPos - ---各个轴发送脉冲的间隔值，单位为mm
        # // 参数：fSpeed - ---各个轴发送脉冲运动过程中的速度值，单位为mm / s
        # // 参数：fDeltaStep - ---默认为0
        # // 参数：iTime - ---默认为0
        # // 返回值：true - 成功、false - 失败
        result = 0
        if self.status == 1:
            result = self.dll.MoveToPosByType(device, n_axis, to_start, to_end, to_speed, start_equ, end_equ, step_pos, speed, delta_step, i_time)
            if result == 1:
                print('开始TTL模式转动')
        return result

    def get_motor_idle(self, device, n_axis):
        # // 电机运动状态
        # // 是否停止，TRUE - 停止1，FALSE - 运动；
        result = self.dll.GetMotorIdle(device, n_axis)
        if result == 1:
            print('电机处于停止状态')
        else:
            print('电机处于运动状态')
        return result

    def get_pos_limit(self, device, n_axis):
        # // 是否正限位，TRUE - 正限位，FALSE - 未正限位；
        result = self.dll.GetPosLimit(device, n_axis)
        if result == 1:
            print('电机已正限位')
        else:
            print('电机未正限位')
        return result

    def get_neg_limit(self, device, n_axis):
        # // 是否负限位，TRUE - 负限位，FALSE - 未负限位；
        result = self.dll.GetNegLimit(device, n_axis)
        if result == 1:
            print('电机已负限位')
        else:
            print('电机未负限位')
        return result

    def get_home_complete(self, device, n_axis):
        # // 寻零是否完成，TRUE - 寻零完成，FALSE - 寻零未完成；
        result = self.dll.GetHomeComplete(device, n_axis)
        if result == 1:
            print('电机已完成寻零')
        else:
            print('电机未完成寻零')
        return result

    def stop(self, device, n_axis):
        # // 停止转动；nAxis - 轴，详见前文说明；
        # // 返回值：true - 成功、false - 失败
        result = 0
        if self.status == 1:
            result = self.dll.Stop(device, n_axis)
            if result == 1:
                print('设备已停止转动')
        return result

    def s_home(self, device, n_axis):
        # // 停止转动；nAxis - 轴，详见前文说明；
        # // 返回值：true - 成功、false - 失败
        result = 0
        if self.status == 1:
            result = self.dll.SHome(device, n_axis)
            if result == 1:
                print('设备开始寻零')
        return result

    def get_position(self, device, n_axis):
        # // 获取位置；nAxis - 轴，详见前文说明；
        # // 参数iDevice恒定为0；
        # // 返回值：实时位置值，单位为°。
        result = self.dll.GetPos(device, n_axis)
        print('当前角度为：%f°' % result)
        return result


if __name__ == '__main__':
    # rsc = RSC('192.168.0.101', 50, 2000000)
    # rsc.open()
    # rsc.reset()
    # time.sleep(3)
    # rsc.read_idn()
    # rsc.set_att()
    # rsc.set_freq()
    # rsc.set_corr_on()
    # time.sleep(3)
    # rsc.set_corr_off()
    # rsc.close()
    # hmp = HMP('192.168.0.105', '1', '24', '1')
    # hmp.open()
    # hmp.reset()
    # time.sleep(1)
    # hmp.select_chan('2')
    # hmp.set_volt(18)
    # hmp.set_curr(2)
    # hmp.set_chan_on()
    # hmp.set_output_on()
    # hmp.read_idn()
    # hmp.return_status()
    # hmp.close()
    fsw = FSW('192.168.0.30')
    fsw.open()
    time.sleep(2)
    fsw.reset()
    fsw.read_idn()


    fsw.close()
    # rto = RTO('192.168.0.33')
    # rto.open()
    # rto.read_idn()
    # rto.close()
    # smw = SMW('192.168.0.22')
    # smw.open()
    # smw.read_idn()
    # smw.close()
