import pyvisa
import time


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
    def __init__(self, ip, chan, volt, curr):
        self.ip = ip
        self.chan = chan
        self.volt = volt
        self.curr = curr
        self.address = 'TCPIP::%s::5025::SOCKET' % self.ip
        self.resourceManager = pyvisa.ResourceManager()

    def open(self):
        self.instance = self.resourceManager.open_resource(self.address, read_termination='\n')

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

    def set_default(self):
        self.instance.write('INST:NSEL %s' % self.chan)
        self.instance.write('VOLT %s' % self.volt)
        self.instance.write('CURR %s' % self.curr)

    def return_status(self):
        print('当前选择的通道：' + self.instance.query('INST:NSEL?'))
        print('电压设置：' + self.instance.query('VOLT?'))
        print('电流设置：' + self.instance.query('CURR?'))
        print('电流输出值：' + self.instance.query('MEAS:CURR?'))
        print('电压输出值:' + self.instance.query('MEAS:VOLT?'))

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
    def __init__(self, ip):
        self.ip = ip
        self.address = 'TCPIP::%s::inst0::INSTR' % self.ip

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
    hmp = HMP('192.168.0.105', '1', '24', '1')
    hmp.open()
    # hmp.reset()
    # time.sleep(1)
    # hmp.select_chan('2')
    # hmp.set_volt(18)
    # hmp.set_curr(2)
    # hmp.set_chan_on()
    # hmp.set_output_on()
    # hmp.read_idn()
    hmp.return_status()
    hmp.close()
    # fsw = FSW('192.168.0.30')
    # fsw.open()
    # fsw.read_idn()
    # fsw.close()
    # rto = RTO('192.168.0.33')
    # rto.open()
    # rto.read_idn()
    # rto.close()
    # smw = SMW('192.168.0.22')
    # smw.open()
    # smw.read_idn()
    # smw.close()
