import pyvisa
import math
import ctypes
from ctypes import wintypes
# from cantools import database
import numpy as np


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
		if self.instance:
			result = True
			print('连接成功')
		else:
			result = False
			print('连接失败')
		return result
	
	def close(self):
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
		self.dll = ctypes.CDLL('D:\\files\python_learn\\auto_test\\dll\\D4ARTS6x64.dll')
		self.status = 0
		self.output = 0
		self.tr = 0
		self.mode = 1
		self.freq = 76250000
		self.gain_s = 46
		self.rut_distance = 0
	
	def connect(self, ip):
		self.ip = ctypes.c_char_p(ip.encode('utf-8'))
		if self.status == 0:
			result = self.dll.Connect(self.ip)
			if result == 0:
				self.status = 1
				print('ARTS连接成功')
			else:
				print('连接失败')
		else:
			print('ARTS已连接')
	
	def disconnect(self):
		if self.status == 1:
			result = self.dll.Disconnect()
			if result == 0:
				self.status = 0
				print('ARTS成功断开连接')
			else:
				print('断开连接失败')
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
		result = self.dll.SetRfFreq_kHz(ctypes.byref(ctypes.c_int(freq)))
		if result == 0:
			print('频率已设置为%dKHz' % freq)
		return result
	
	def set_trims(self, gain_trim, range_trim, rut_distance):
		self.gain_trim = ctypes.c_double(gain_trim)
		self.range_trim = ctypes.c_double(range_trim)
		self.rut_distance = rut_distance
		result = self.dll.SetTrims(
			self.gain_trim, self.gain_trim, self.gain_trim, self.gain_trim,
			self.range_trim, self.range_trim, self.range_trim, self.range_trim,
			self.rut_distance)
		if result == 0:
			print('已设置GainTrim为%ddB，已设置RangeTrim为%dm,已设置RUTDistance为%dm ' %
				  (gain_trim, range_trim, rut_distance))
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
		result = self.dll.SetStaticMode(1)
		if result == 0:
			print('已设置为静态工作模式')
		return result
	
	def set_mode_dynamic(self):
		result = self.dll.SetStaticMode(0)
		if result == 0:
			self.mode = 0
			print('已设置为动态工作模式')
		return result
	
	def set_tx_chan_static(self, speed_ch1, speed_ch2, speed_ch3, speed_ch4,
			rcs_ch1, rcs_ch2, rcs_ch3, rcs_ch4,
			range_ch1, range_ch2, range_ch3, range_ch4):
		# Set Tx Channel Parameters in "normal operating units": Speed (kph), Gain (dB), Range (m).
		wave_speed = 3 * 10 ** 8
		wave_period = 1 / (self.freq * 10 ** 3)
		gama = wave_speed * wave_period
		gain_ch1 = rcs_ch1 * 4 * math.pi * range_ch1 ** 4 / (self.gain_s ** 2 * gama ** 2 * (range_ch1 + self.rut_distance) ** 4)
		gain_ch2 = rcs_ch2 * 4 * math.pi * range_ch2 ** 4 / (self.gain_s ** 2 * gama ** 2 * (range_ch2 + self.rut_distance) ** 4)
		gain_ch3 = rcs_ch3 * 4 * math.pi * range_ch3 ** 4 / (self.gain_s ** 2 * gama ** 2 * (range_ch3 + self.rut_distance) ** 4)
		gain_ch4 = rcs_ch4 * 4 * math.pi * range_ch4 ** 4 / (self.gain_s ** 2 * gama ** 2 * (range_ch4 + self.rut_distance) ** 4)
		self.speed_ch1 = ctypes.c_double(speed_ch1)
		self.speed_ch2 = ctypes.c_double(speed_ch2)
		self.speed_ch3 = ctypes.c_double(speed_ch3)
		self.speed_ch4 = ctypes.c_double(speed_ch4)
		self.rcs_ch1 = ctypes.c_double(rcs_ch1)
		self.rcs_ch2 = ctypes.c_double(rcs_ch2)
		self.rcs_ch3 = ctypes.c_double(rcs_ch3)
		self.rcs_ch4 = ctypes.c_double(rcs_ch4)
		self.range_ch1 = ctypes.c_double(range_ch1)
		self.range_ch2 = ctypes.c_double(range_ch2)
		self.range_ch3 = ctypes.c_double(range_ch3)
		self.range_ch4 = ctypes.c_double(range_ch4)
		result = self.dll.SetTxChanStaticCfg(
			ctypes.byref(self.speed_ch1),
			ctypes.byref(self.speed_ch2),
			ctypes.byref(self.speed_ch3),
			ctypes.byref(self.speed_ch4),
			ctypes.byref(self.rcs_ch1),
			ctypes.byref(self.rcs_ch2),
			ctypes.byref(self.rcs_ch3),
			ctypes.byref(self.rcs_ch4),
			ctypes.byref(self.range_ch1),
			ctypes.byref(self.range_ch2),
			ctypes.byref(self.range_ch3),
			ctypes.byref(self.range_ch4))
		if result == 0:
			print('静态目标设置成功\n'
				  '目标1：速度%dkm/h，距离%dm，RCS%ddBsm\n'
				  '目标2：速度%dkm/h，距离%dm，RCS%ddBsm\n'
				  '目标3：速度%dkm/h，距离%dm，RCS%ddBsm\n'
				  '目标4：速度%dkm/h，距离%dm，RCS%ddBsm\n' %
				  (speed_ch1, range_ch1, rcs_ch1,
				   speed_ch2, range_ch2, rcs_ch2,
				   speed_ch3, range_ch3, rcs_ch3,
				   speed_ch4, range_ch4, rcs_ch4))
		return result
	
	def set_tx_chan_dynamic(self,
			start_speed_ch1, start_speed_ch2, start_speed_ch3, start_speed_ch4,
			stop_speed_ch1, stop_speed_ch2, stop_speed_ch3, stop_speed_ch4,
			start_range_ch1, start_range_ch2, start_range_ch3, start_range_ch4,
			stop_range_ch1, stop_range_ch2, stop_range_ch3, stop_range_ch4,
			rcs_ch1, rcs_ch2, rcs_ch3, rcs_ch4):
		# // enable 1/R^4 power attenuation
		# // 0=no file created; 1=binary file; 2=ASCII file
		# // can be NULL if no file created
		wave_speed = 3 * 10 ** 8
		wave_period = 1 / (self.freq * 10 ** 6)
		gama = wave_speed * wave_period
		gain_ch1 = rcs_ch1 * 4 * math.pi * start_range_ch1 ** 4 / (self.gain_s ** 2 * gama ** 2 * (start_range_ch1 + self.rut_distance) ** 4)
		gain_ch2 = rcs_ch2 * 4 * math.pi * start_range_ch2 ** 4 / (self.gain_s ** 2 * gama ** 2 * (start_range_ch2 + self.rut_distance) ** 4)
		gain_ch3 = rcs_ch3 * 4 * math.pi * start_range_ch3 ** 4 / (self.gain_s ** 2 * gama ** 2 * (start_range_ch3 + self.rut_distance) ** 4)
		gain_ch4 = rcs_ch4 * 4 * math.pi * start_range_ch4 ** 4 / (self.gain_s ** 2 * gama ** 2 * (start_range_ch4 + self.rut_distance) ** 4)
		self.start_speed_ch1 = ctypes.c_double(start_speed_ch1)
		self.start_speed_ch2 = ctypes.c_double(start_speed_ch2)
		self.start_speed_ch3 = ctypes.c_double(start_speed_ch3)
		self.start_speed_ch4 = ctypes.c_double(start_speed_ch4)
		self.stop_speed_ch1 = ctypes.c_double(stop_speed_ch1)
		self.stop_speed_ch2 = ctypes.c_double(stop_speed_ch2)
		self.stop_speed_ch3 = ctypes.c_double(stop_speed_ch3)
		self.stop_speed_ch4 = ctypes.c_double(stop_speed_ch4)
		self.start_range_ch1 = ctypes.c_double(start_range_ch1)
		self.start_range_ch2 = ctypes.c_double(start_range_ch2)
		self.start_range_ch3 = ctypes.c_double(start_range_ch3)
		self.start_range_ch4 = ctypes.c_double(start_range_ch4)
		self.stop_range_ch1 = ctypes.c_double(stop_range_ch1)
		self.stop_range_ch2 = ctypes.c_double(stop_range_ch2)
		self.stop_range_ch3 = ctypes.c_double(stop_range_ch3)
		self.stop_range_ch4 = ctypes.c_double(stop_range_ch4)
		self.gain_ch1 = ctypes.c_double(rcs_ch1)
		self.gain_ch2 = ctypes.c_double(rcs_ch2)
		self.gain_ch3 = ctypes.c_double(rcs_ch3)
		self.gain_ch4 = ctypes.c_double(rcs_ch4)
		result = self.dll.GenerateTargetWaveform(
			ctypes.byref(self.start_speed_ch1),
			ctypes.byref(self.start_speed_ch2),
			ctypes.byref(self.start_speed_ch3),
			ctypes.byref(self.start_speed_ch4),
			ctypes.byref(self.stop_speed_ch1),
			ctypes.byref(self.stop_speed_ch2),
			ctypes.byref(self.stop_speed_ch3),
			ctypes.byref(self.stop_speed_ch4),
			ctypes.byref(self.start_range_ch1),
			ctypes.byref(self.start_range_ch2),
			ctypes.byref(self.start_range_ch3),
			ctypes.byref(self.start_range_ch4),
			ctypes.byref(self.stop_range_ch1),
			ctypes.byref(self.stop_range_ch2),
			ctypes.byref(self.stop_range_ch3),
			ctypes.byref(self.stop_range_ch4),
			ctypes.byref(self.gain_ch1),
			ctypes.byref(self.gain_ch2),
			ctypes.byref(self.gain_ch3),
			ctypes.byref(self.gain_ch4),
			1, 0)
		if result == 0:
			print('静态目标设置成功\n'
				  '目标1：起始速度%dkm/h，终止速度%dkm/h，起始距离%dm，终止距离%dm，RCS%ddBsm\n'
				  '目标2：起始速度%dkm/h，终止速度%dkm/h，起始距离%dm，终止距离%dm，RCS%ddBsm\n'
				  '目标3：起始速度%dkm/h，终止速度%dkm/h，起始距离%dm，终止距离%dm，RCS%ddBsm\n'
				  '目标4：起始速度%dkm/h，终止速度%dkm/h，起始距离%dm，终止距离%dm，RCS%ddBsm\n' %
				  (start_speed_ch1, stop_speed_ch1, start_range_ch1, stop_range_ch1, rcs_ch1,
				   start_speed_ch2, stop_speed_ch2, start_range_ch2, stop_range_ch2, rcs_ch2,
				   start_speed_ch3, stop_speed_ch3, start_range_ch3, stop_range_ch3, rcs_ch3,
				   start_speed_ch4, stop_speed_ch4, start_range_ch4, stop_range_ch4, rcs_ch4,
				   ))
		# if r4_enable == 1:
		#     print('功率距离自适应开启')
		return result
	
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
	
	def download_wave_form(self, waveform_format_code):
		# // 0=DLL internal memory; 1=binary file; 2=ASCII file
		# // can be NULL if no file used
		result = self.dll.DownloadWaveform(waveform_format_code)
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
		if self.dll.CheckConnectionStatus() == 1:
			result = self.dll.SetTrEn(1)
			self.tr = 1
			if result == 0:
				print('ARTS成功打开T/R模块')
		else:
			print('ARTS未连接')
		return result
	
	def set_tr_off(self):
		result = 1
		if self.dll.CheckConnectionStatus() == 1:
			result = self.dll.SetTrEn(0)
			self.tr = 0
			if result == 0:
				print('ARTS成功关闭T/R模块')
		else:
			print('ARTS未连接')
		return result
	
	def set_output_on(self):
		result = 1
		if self.dll.CheckConnectionStatus() == 1:
			result = self.dll.SetSynthRFOutput(1)
			self.output = 1
			if result == 0:
				print('ARTS成功打开RF发射')
		else:
			print('ARTS未连接')
		return result
	
	def set_output_off(self):
		result = 1
		if self.dll.CheckConnectionStatus() == 1:
			result = self.dll.SetSynthRFOutput(0)
			self.output = 0
			if result == 0:
				print('ARTS成功关闭RF发射')
		else:
			print('ARTS未连接')
		return result
	
	def get_system_status(self):
		self.dll.GetSystemStatus()


class TurnTable:
	# nAxis - 轴：nAxis == 1 时为俯仰轴；
	# nAxis - 轴：nAxis == 2 时为方位轴；
	# fSetPos：单位为°（对转台而言）或者mm(对扫描架而言)
	# fSetVel：° / s（对转台而言）或者mm / s(对扫描架而言)
	# iDevice：设备地址号，转台iDevice = 0。
	def __init__(self):
		self.dll = ctypes.CDLL("C:\\Users\\liuli\\PycharmProjects\\auto_test\\dll\\PcommDllx64.dll")
		self.i_device = ctypes.c_short(0)
	
	def connect(self):
		# // 参数：iDevice –设备地址号，对本扫描架来说iDevice = 0；
		# // 返回值：true - 成功、false - 失败
		result = self.dll.ConnectImac(self.i_device)
		if result == 1:
			print('转台连接成功')
		else:
			print('转台连接失败')
	
	def disconnect(self):
		# // 参数：iDevice –设备地址号；
		# // 返回值：true - 成功、false - 失败
		result = self.dll.DisConnectImac()
		if result == 1:
			print('转台断开成功')
		else:
			print('转台断开失败')
	
	def move_to_position(self, n_axis, set_pos, set_vel, b_abs=True):
		# // 参数：fSetPos –对应轴号所设置的位置值；
		# // 参数：fSetVel –对应轴号所设置的速度值；
		# // 参数：bIsAbs –对于轴号运动方式，true - 绝对运动，false - 相对运动；
		# // 返回值：true - 成功、false - 失败
		# fSetPos：单位为°（对转台而言）或者mm(对扫描架而言)
		# fSetVel：° / s（对转台而言）或者mm / s(对扫描架而言)
		# iDevice：设备地址号，转台iDevice = 0。
		result = self.dll.MoveDeviceToPos(self.i_device, ctypes.c_short(n_axis), ctypes.c_double(set_pos), ctypes.c_double(set_vel), b_abs)
		print('发送指令......')
		if result == 1:
			print('开始常规模式转动' + str(set_pos) + '°\n')
		return result
	
	def move_to_position_by_type(self, n_axis, to_start, to_end, to_speed, start_equ, end_equ, step_pos, speed, delta_step, i_time):
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
		result = self.dll.MoveToPosByType(self.i_device, ctypes.c_short(n_axis), to_start, to_end, to_speed, start_equ, end_equ, step_pos, speed, delta_step, i_time)
		if result == 1:
			print('开始TTL模式转动')
		return result
	
	def get_motor_idle(self, n_axis):
		# // 电机运动状态
		# // 是否停止，TRUE - 停止1，FALSE - 运动；
		result = self.dll.GetMotorIdle(self.i_device, ctypes.c_short(n_axis))
		if result == 1:
			print('电机处于停止状态')
		else:
			print('电机处于运动状态')
		return result
	
	def get_pos_limit(self, n_axis):
		# // 是否正限位，TRUE - 正限位，FALSE - 未正限位；
		result = self.dll.GetPosLimit(self.i_device, ctypes.c_short(n_axis))
		if result == 1:
			print('电机已正限位')
		else:
			print('电机未正限位')
		return result
	
	def get_neg_limit(self, n_axis):
		# // 是否负限位，TRUE - 负限位，FALSE - 未负限位；
		result = self.dll.GetNegLimit(self.i_device, ctypes.c_short(n_axis))
		if result == 1:
			print('电机已负限位')
		else:
			print('电机未负限位')
		return result
	
	def get_home_complete(self, n_axis):
		# // 寻零是否完成，TRUE - 寻零完成，FALSE - 寻零未完成；
		result = self.dll.GetHomeComplete(self.i_device, ctypes.c_short(n_axis))
		if result == 1:
			print('电机已完成寻零')
		else:
			print('电机未完成寻零')
		return result
	
	def stop(self, n_axis):
		# // 停止转动；nAxis - 轴，详见前文说明；
		# // 返回值：true - 成功、false - 失败
		result = self.dll.Stop(self.i_device, ctypes.c_short(n_axis))
		if result == 1:
			print('设备已停止转动')
		return result
	
	def s_home(self, n_axis):
		# // 停止转动；nAxis - 轴，详见前文说明；
		# // 返回值：true - 成功、false - 失败
		result = self.dll.SHome(self.i_device, ctypes.c_short(n_axis))
		if result == 1:
			print('设备开始寻零')
		return result
	
	def get_position(self, n_axis):
		# // 获取位置；nAxis - 轴，详见前文说明；
		# // 参数iDevice恒定为0；
		# // 返回值：实时位置值，单位为°。
		self.dll.GetPos.restype = ctypes.c_double
		result = self.dll.GetPos(self.i_device, ctypes.c_short(n_axis))
		# print('当前角度为：%f°' % result)
		return result


class Struct_INIT_CONFIG(ctypes.Structure):
	_fields_ = (("AccCode", wintypes.DWORD),
				("AccMask", wintypes.DWORD),
				("Reserved", wintypes.DWORD),
				("Filter", ctypes.c_ubyte),
				("Timing0", ctypes.c_ubyte),
				("Timing1", ctypes.c_ubyte),
				("Mode", ctypes.c_ubyte))


class Struct_CAN_OBJ(ctypes.Structure):
	_fields_ = [("ID", ctypes.c_uint),
				("TimeStamp", ctypes.c_uint),
				("TimeFlag", ctypes.c_ubyte),
				("SendType", ctypes.c_ubyte),
				("RemoteFlag", ctypes.c_ubyte),
				("ExternFlag", ctypes.c_ubyte),
				("DataLen", ctypes.c_ubyte),
				("Data", ctypes.c_ubyte * 8),
				("Reserved", ctypes.c_ubyte * 3)]


class CanControl:
	def __init__(self):
		self.db = database.load_file('./dbc/ARS408_can_database.dbc')
		self.canDLL = ctypes.CDLL('D:\\files\python_learn\\auto_test\\dll\\ECanVci64.dll')
		# self.canDLL = ctypes.CDLL('./dll/ECanVci64.dll')
		self.struct_initconfig = Struct_INIT_CONFIG(0, 0xFFFFFFFF, 0, 0, 0, 0x1C, 0)
		self.Struct_USBCAN2C = 4
		self.STATUS_OK = 1
		self.data = np.array([[-1, -1, -1, -1, -1, -1, -1]])
		# 定义DBC数据格式
		self.id_start = 0
		self.id_length = 8
		self.id_factor = 1
		self.id_offset = 0
		self.id_start_handle = (self.id_start // 8 + 1) * 8 - self.id_start % 8 - self.id_length
		self.dist_long_start = 19
		self.dist_long_length = 13
		self.dist_long_factor = 0.2
		self.dist_long_offset = -500
		self.dist_long_start_handle = (self.dist_long_start // 8 + 1) * 8 - self.dist_long_start % 8 - self.dist_long_length
		self.dist_lat_start = 24
		self.dist_lat_length = 11
		self.dist_lat_factor = 0.2
		self.dist_lat_offset = -204.6
		self.dist_lat_start_handle = (self.dist_lat_start // 8 + 1) * 8 - self.dist_lat_start % 8 - self.dist_lat_length
		self.verl_long_start = 46
		self.verl_long_length = 10
		self.verl_long_factor = 0.25
		self.verl_long_offset = -128
		self.verl_long_start_handle = (self.verl_long_start // 8 + 1) * 8 - self.verl_long_start % 8 - self.verl_long_length
		self.verl_lat_start = 53
		self.verl_lat_length = 9
		self.verl_lat_factor = 0.25
		self.verl_lat_offset = -64
		self.verl_lat_start_handle = (self.verl_lat_start // 8 + 1) * 8 - self.verl_lat_start % 8 - self.verl_lat_length
		self.dyn_prop_start = 48
		self.dyn_prop_length = 3
		self.dyn_prop_factor = 1
		self.dyn_prop_offset = 0
		self.dyn_prop_start_handle = (self.dyn_prop_start // 8 + 1) * 8 - self.dyn_prop_start % 8 - self.dyn_prop_length
		self.rcs_start = 56
		self.rcs_length = 8
		self.rcs_factor = 0.5
		self.rcs_offset = -64
		self.rcs_start_handle = (self.rcs_start // 8 + 1) * 8 - self.rcs_start % 8 - self.rcs_length
	
	def open(self):
		result = self.canDLL.OpenDevice(self.Struct_USBCAN2C, 0, 0)
		if result != self.STATUS_OK:
			print('调用 Struct_OpenDevice出错\r\n')
	
	def init_channel(self, channel):
		result = self.canDLL.InitCAN(self.Struct_USBCAN2C, 0, channel, ctypes.byref(self.struct_initconfig))
		if result != self.STATUS_OK:
			print('调用 Struct_InitCAN' + channel + '出错\r\n')
		result = self.canDLL.StartCAN(self.Struct_USBCAN2C, 0, channel)
		if result != self.STATUS_OK:
			print('调用 Struct_StartCAN' + channel + '出错\r\n')
	
	def send_message(self, channel):
		byte_array = ctypes.c_ubyte * 8
		information = byte_array(1, 2, 3, 4, 5, 6, 7, 64)
		byte_3array = ctypes.c_ubyte * 3
		remain = byte_3array(0, 0, 0)
		can_obj = Struct_CAN_OBJ(0x0, 0, 0, 1, 0, 0, 8, information, remain)
		result = self.canDLL.Transmit(self.Struct_USBCAN2C, 0, channel, ctypes.byref(can_obj), 1)
		if result != self.STATUS_OK:
			print('调用 Struct_Transmit 出错\r\n')
	
	def get_message(self, channel):
		# 接收通道数据
		byte_array = ctypes.c_ubyte * 8
		information = byte_array(0, 0, 0, 0, 0, 0, 0, 1)
		byte_3array = ctypes.c_ubyte * 3
		remain = byte_3array(0, 0, 0)
		self.can_obj = Struct_CAN_OBJ(0x0, 1, 1, 0, 0, 0, 8, information, remain)
		ret = self.canDLL.Receive(self.Struct_USBCAN2C, 0, channel, ctypes.byref(self.can_obj), 1, 1)
		if ret > 0:
			if self.can_obj.ID == 1547:
				# start = time.clock()
				struct_can_obj_data = list(self.can_obj.Data)
				# print(self.can_obj.TimeStamp)
				message = ''
				# 16进制转化为2进制
				for i in struct_can_obj_data:
					bin_i = bin(i)
					# 每比特转化成2进制，空位补零
					bin_i = bin_i[2:].rjust(8, '0')
					message += bin_i
				# 根据DBC文件取ID
				obj_id_bin = message[self.id_start_handle:self.id_start_handle + self.id_length]
				obj_dist_long_bin = message[self.dist_long_start_handle:self.dist_long_start_handle + self.dist_long_length]
				obj_dist_lat_bin = message[self.dist_lat_start_handle:self.dist_lat_start_handle + self.dist_lat_length]
				obj_verl_long_bin = message[self.verl_long_start_handle:self.verl_long_start_handle + self.verl_long_length]
				obj_verl_lat_bin = message[self.verl_lat_start_handle:self.verl_lat_start_handle + self.verl_lat_length]
				obj_dyn_prop_bin = message[self.dyn_prop_start_handle:self.dyn_prop_start_handle + self.dyn_prop_length]
				obj_rcs_bin = message[self.rcs_start_handle:self.rcs_start_handle + self.rcs_length]
				obj_id = int(obj_id_bin, 2) * self.id_factor + self.id_offset
				# 将截取的二进制数据转化为十进制
				obj_dist_long = int(obj_dist_long_bin, 2) * self.dist_long_factor + self.dist_long_offset
				obj_dist_lat = int(obj_dist_lat_bin, 2) * self.dist_lat_factor + self.dist_lat_offset
				obj_verl_long = int(obj_verl_long_bin, 2) * self.verl_long_factor + self.verl_long_offset
				obj_verl_lat = int(obj_verl_lat_bin, 2) * self.verl_lat_factor + self.verl_lat_offset
				obj_dyn_prop = int(obj_dyn_prop_bin, 2) * self.dyn_prop_factor + self.dyn_prop_offset
				obj_rcs = int(obj_rcs_bin, 2) * self.rcs_factor + self.rcs_offset
				self.data = [obj_id, round(obj_dist_long, 2), round(obj_dist_lat, 2), obj_verl_long, obj_verl_lat, obj_rcs, obj_dyn_prop]
			# 定义数据为新数据
			# message_status = 1
			# for i in range(len(self.data)):
			#     if self.data[i, 0] == data_basic[0]:
			#         self.data[i] = data_basic
			# print('数据刷新')
			# 数据状态更新
			# message_status = 0
			# if message_status == 1:
			#     self.data = np.row_stack((self.data, data_basic))
			# print('数据新增')
			# print(self.data)
			# end = time.clock()
			# print(round(end-start, 3))
	
	def close(self):
		result = self.canDLL.CloseDevice(self.Struct_USBCAN2C, 0)
		if result != self.STATUS_OK:
			print('调用 Struct_CloseDevice出错\r\n')


if __name__ == '__main__':
	#RCS连接测试
	rsc = RSC('192.168.0.101', 50, 2000000)
	rsc.open()
	rsc.reset()
	time.sleep(3)
	rsc.read_idn()
	rsc.set_att()
	rsc.set_freq()
	rsc.set_corr_on()
	time.sleep(3)
	rsc.set_corr_off()
	rsc.close()
	
	# HMP连接测试
	# hmp = HMP()
	# hmp.open('192.168.0.105')
	# hmp.reset()
	# time.sleep(1)
	# hmp.select_chan(2)
	# hmp.set_volt(18)
	# hmp.set_curr(2)
	# hmp.set_chan_on()
	# hmp.set_output_on()
	# hmp.read_idn()
	# hmp.return_status()
	# hmp.close()
	
	# FSW连接测试
	# fsw = FSW('192.168.0.30')
	# fsw.open()
	# time.sleep(2)
	# fsw.reset()
	# fsw.read_idn()
	# fsw.close()
	
	# RTO连接测试
	# rto = RTO('192.168.0.33')
	# rto.open()
	# rto.read_idn()
	# rto.close()
	
	# SMW连接测试
	# smw = SMW('192.168.0.22')
	# smw.open()
	# smw.read_idn()
	# smw.close()
	
	# turntable连接测试
	# turntable = TurnTable()
	# turntable.connect()
	# time.sleep(2)
	# # turntable.move_to_position(1, 20, 1)
	# # time.sleep(2)
	# turntable.get_position(1)
	# turntable.s_home(1)
	# turntable.s_home(2)
	
	# ARTS连接测试
	# arts = ARTS()
	# arts.connect('192.168.0.20')
# time.sleep(1)
# arts.set_freq(76250000)
# arts.set_tr_on()
# time.sleep(2)
# arts.set_tr_off()
# time.sleep(2)
# arts.set_mode_static()
# arts.set_mode_dynamic()
# arts.reset()
# arts.set_trims(10, 10, 5)
# time.sleep(2)
# arts.set_tx_chan_static(0,0,0,0,-5,10,10,-10,100,80,120,140)
# arts.set_tx_chan_dynamic(5, 20, 30, 40, 5, 20, 30, 40, 80, 100, 110, 120, 180, 190, 200, 210, 15, -5, -5, -5)
# arts.reset()
# time.sleep(4)
# arts.set_tx_chan_enable(1, 0, 0, 0)
# time.sleep(1)
# arts.set_tr_on()
# time.sleep(4)
# arts.set_output_on()
# time.sleep(3)
# arts.download_wave_form(0)
# time.sleep(4)
# arts.run_wave_form(1, 0)
# time.sleep(4)
# arts.set_output_off()
# time.sleep(2)
# arts.set_tr_off()
# arts.disconnect()
