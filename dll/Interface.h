#pragma once;  
using namespace std;
#ifdef DLL_IMPLEMENT
#define DLL_API __declspec(dllexport)  
#else  
#define DLL_API __declspec(dllimport)  
#endif  
//*******************************扫描架标准接口函数**************************************//
//参数说明：
//iDevice=0
//nAxis = 1------X轴
//nAxis = 2------Y轴
//nAxis = 3------Z轴
//nAxis = 4------P轴
//pos----各个轴所要运动的距离值，单位为mm
//vel----各个轴所要运动的速度值，单位为mm/s
//fToStart----各个轴所要运动的距离值，位置值在发送脉冲起始角之前，单位为mm
//fToEnd----各个轴所要运动的距离值，位置值在发送脉冲起始角之前，单位为mm
//fToSpeed----各个轴到fToStart位置时的速度，单位为mm/s
//fStartEqu----各个轴发送脉冲的起始位置值，单位为mm
//fEndEqu----各个轴发送脉冲的终止位置值，单位为mm
//fStepPos----各个轴发送脉冲的间隔值，单位为mm
//fSpeed----各个轴发送脉冲运动过程中的速度值，单位为mm/s
//fDeltaStep----默认为0
//iTime----默认为0

//连接控制器
extern "C" DLL_API BOOL ConnectImac(short iDevice);

//断开连接
extern "C" DLL_API BOOL DisConnectImac(short iDevice);

//停止运动
extern "C" DLL_API BOOL Stop(short iDevice, short nAxis);

//寻零
extern "C" DLL_API BOOL SHome(short iDevice, short nAxis) ;

//参数参数isAbsolute表示绝对运动与相对运动,参数pos表示运动到的位置
extern "C" DLL_API BOOL MoveDeviceToPos(short iDevice, short nAxis, double pos,double vel, bool isAbsolute = true);

//发送脉冲运动
extern "C" DLL_API BOOL MoveToPosByType(short iDevice, short nAxis, double fToStart,double fToEnd,double fToSpeed,double fStartEqu, double fEndEqu, double fStepPos,  double fSpeed, double fDeltaStep = 0, int iTime = 0);

//电机运动状态
//是否停止，TRUE-停止，FALSE-运动；
extern "C" DLL_API BOOL GetMotorIdle(short iDevice,short nAxis);

//是否正限位，TRUE-正限位，FALSE-未正限位；
extern "C" DLL_API BOOL GetPosLimit(short iDevice,short nAxis);

//是否负限位，TRUE-负限位，FALSE-未负限位；
extern "C" DLL_API BOOL GetNegLimit(short iDevice,short nAxis);

//是否负限位，TRUE-寻零完成，FALSE-寻零未完成；
extern "C" DLL_API BOOL GetHomeComplete(short iDevice,short nAxis);


//获取当前位置
extern "C" DLL_API double  GetPos(short iDevice,short nAxis);

//单个脉冲
extern "C" DLL_API BOOL SinglePulse(short iDevice,short nAxis);

//获取控制器是否正常连接
extern "C" DLL_API BOOL GetPmacPower(short iDevice);

extern "C" DLL_API BOOL SetAccTime(short iDevice,short nAxis,short nTime);

//*******************************扫描架标准接口函数**************************************//




