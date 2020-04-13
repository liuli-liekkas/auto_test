import numpy as np
import pyqtgraph as pg

app = pg.mkQApp()

win = pg.GraphicsWindow()
win.setWindowTitle(u'pyqtgraph plot demo')
win.resize(600, 400)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setLabel(axis='left', text=u'Amplitude / V')
p.setLabel(axis='bottom', text=u't / s')
p.setTitle('y1=sin(x)  y2=cos(x)')
p.addLegend()

curve1 = p.plot(pen='r', name='y1')
curve2 = p.plot(pen='g', name='y2')

Fs = 1024.0 #采样频率
N = 1024    #采样点数
f0 = 5.0    #信号频率
pha = 0     #初始相位
t = np.arange(N) / Fs   #时间向量

def plotData():
    global pha
    pha += 10
    curve1.setData(t, np.sin(2 * np.pi * f0 * t + pha*np.pi/180.0))
    curve2.setData(t, np.cos(2 * np.pi * f0 * t + pha*np.pi/180.0))

timer = pg.QtCore.QTimer()
timer.timeout.connect(plotData)
timer.start(50)

app.exec_()