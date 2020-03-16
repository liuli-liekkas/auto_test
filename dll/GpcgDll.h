
// The following ifdef block is the standard way of creating macros which make exporting 
// from a DLL simpler. All files within this DLL are compiled with the GPCGDLL_EXPORTS
// symbol defined on the command line. this symbol should not be defined on any project
// that uses this DLL. This way any other project whose source files include this file see 
// GPCGDLL_API functions as being imported from a DLL, wheras this DLL sees symbols
// defined with this macro as being exported.
#ifdef GPCGDLL_EXPORTS
#define GPCGDLL_API extern "C" __declspec(dllexport)
#else
#define GPCGDLL_API extern "C" __declspec(dllimport)
#endif

//#include "resource.h"

#define DLL_PN		"D4ARTS6"			// 4 Target, 1 GHz ARTS, new IF Module (with dedicated Freq Syn SCLK line)
#define DLL_REV		"0.1"

// ----------------------------------------------------------------------------
// Function Return Codes
//		SUCCESS								= 0
//		FILE_ERROR						= 1
//		TELEM_ERROR						= 2
//		INPUT_PARAM_ERROR			= 3
//		MALLOC_ERROR					= 4
//		INVALID_PASSCODE			= 5
//		DATA_VALIDATION_ERROR = 6
//		OTHER_FAILURE					= 7
// ----------------------------------------------------------------------------

// ----------------------------------------------------------------------------
// ARTS System Commands
// ----------------------------------------------------------------------------

// --------------------------------------------------------
// Ethernet Connection Functions
GPCGDLL_API int Connect( char *sServerIpAddr );					
GPCGDLL_API int Disconnect( void );
GPCGDLL_API int CheckConnectionStatus( void );					// 1=connected; 0=not connected. NOTE: this return code definition doesn't conform
																												// to the return code convention for these functions. Change this later!

// ----------------------------------------------------------------------------
// System Control Functions
GPCGDLL_API int	SetRxAttn( double *p_fRxAttn_dB );
//
// Set Tx Channel Parameters in "engineering units": Freq (Hz), Attn (dB), Delay (nsec).
GPCGDLL_API int	SetTxChanStaticCfg_engineering(
		double fDopplerFreqHzCh1,
		double fDopplerFreqHzCh2,
		double fDopplerFreqHzCh3,
		double fDopplerFreqHzCh4,
		//
		double fTxAttnCh1,						// attn 0-31.75 set on Attn1, 32-62.5 on Attn2, and 62.75 and up in FPGA
		double fTxAttnCh2,
		double fTxAttnCh3,
		double fTxAttnCh4,
		//
		double fDelayNSecCh1,	
		double fDelayNSecCh2,	
		double fDelayNSecCh3,	
		double fDelayNSecCh4,
		//
		double fPhaseOffsetCh1,
		double fPhaseOffsetCh2,
		double fPhaseOffsetCh3,
		double fPhaseOffsetCh4 );
//
// Set Tx Channel Parameters in "normal operating units": Speed (kph), Gain (dB), Range (m).
// 1) range values must be positive, speeds can be positive (opening target) or negative (closing target).
// 2) parameter values are pass by reference. Values will be clamped by function, with clamped values overwriting input values.
GPCGDLL_API int	SetTxChanStaticCfg(
		double *p_fSpeed_kph_Ch1,
		double *p_fSpeed_kph_Ch2,
		double *p_fSpeed_kph_Ch3,
		double *p_fSpeed_kph_Ch4,
		//
		double *p_fGain_dB_Ch1,							
		double *p_fGain_dB_Ch2,
		double *p_fGain_dB_Ch3,
		double *p_fGain_dB_Ch4,
		//
		double *p_fRange_m_Ch1,	
		double *p_fRange_m_Ch2,	
		double *p_fRange_m_Ch3,	
		double *p_fRange_m_Ch4 );

// --------------------------------------------------------------------------
// dynamic (waveform) target control
GPCGDLL_API int GenerateTargetWaveform(
		double *p_fStartSpeed_kph_Ch1,
		double *p_fStartSpeed_kph_Ch2,
		double *p_fStartSpeed_kph_Ch3,
		double *p_fStartSpeed_kph_Ch4,
		//
		double *p_fStopSpeed_kph_Ch1,
		double *p_fStopSpeed_kph_Ch2,
		double *p_fStopSpeed_kph_Ch3,
		double *p_fStopSpeed_kph_Ch4,
		//
		double *p_fStartRange_m_Ch1,
		double *p_fStartRange_m_Ch2,
		double *p_fStartRange_m_Ch3,
		double *p_fStartRange_m_Ch4,
		//
		double *p_fStopRange_m_Ch1,
		double *p_fStopRange_m_Ch2,
		double *p_fStopRange_m_Ch3,
		double *p_fStopRange_m_Ch4,
		//
		double *p_fGain_dB_Ch1,							
		double *p_fGain_dB_Ch2,
		double *p_fGain_dB_Ch3,
		double *p_fGain_dB_Ch4,
		//
		int	nR4Enable,									// enable 1/R^4 power attenuation with distance variation
		//
		int nWaveformFormatCode,				// 0=no file created; 1=binary file; 2=ASCII file 	
		char* sWaveformFileName					// can be NULL if no file created
);
GPCGDLL_API int DownloadWaveform(
		int nWaveformFormatCode,				// 0=no file used, download from DLL internal memory; 1=binary file; 2=ASCII file 	
		char* sWaveformFileName					// can be NULL if no file used
);
GPCGDLL_API int RunWaveform(
		int nContinuous,								// 0=one-shot playback; 1=continuously looping playback
		int nExtTrigger									// 0=start playback immediately; 1=wait for external trigger
);
// --------------------------------------------------------------------------


//
GPCGDLL_API int SetTrims(
	double fGainTrimCh1_dB,
	double fGainTrimCh2_dB,
	double fGainTrimCh3_dB,
	double fGainTrimCh4_dB,
	//
	double fMinRangeTrimCh1_m,
	double fMinRangeTrimCh2_m,
	double fMinRangeTrimCh3_m,
	double fMinRangeTrimCh4_m,
	//
	double	fRUTDistance_m );
//
GPCGDLL_API int TxChanEnable(
	int nEnTxChan1,								// 1=enable, 0=disable
	int nEnTxChan2,
	int nEnTxChan3,
	int nEnTxChan4 );

GPCGDLL_API int IfTestModeEnable( int nTestModeEnable );		// 1=enable, 0=disable

GPCGDLL_API int SetStaticMode( int nStaticMode );						// 1=Static Mode, 0=Dynamic Mode

GPCGDLL_API int SetAdcSatThreshBackoff(											// Set ADC saturation threshold backoff, in dB. Input siganl level above this will trigger 
	double fAdcSatThreshBackoff_dB );													//	cause a saturation detection flag to be set.

GPCGDLL_API int SetTrEn( int nTrEn );												// TR enable

GPCGDLL_API int SetRelays( int nRelay3, int nRelay2, int nRelay1 );		// Set Relays, 3 bit field

GPCGDLL_API int	Reset(void);	// cause an instrument reset. This will stop a running waveform, and return instrument to ready state.

GPCGDLL_API	int ProgramEpcqDevice( char* sFpgaFileName  );	// program FPGA Firmware Configuration file into EPCQ device

GPCGDLL_API int Reboot( void );															// reboot embedded micro-controller

GPCGDLL_API int IncrPllPhaseOffset( void );									// bump phase offset of FPGA PLL - test purposes only!

// ----------------------------------------------------------------------------
// Phase Matrix Frequency Synthesizer Functions
GPCGDLL_API int SetRfFreq_kHz( int *p_nFreq_kHz );					// Program instrument's RF frequency in kHz
GPCGDLL_API int	SetSynthRFOutput( int nRFOutput );					// 0-OFF, 1-ON - via SPI


// ----------------------------------------------------------------------------

// General System Status -
GPCGDLL_API	int	GetSystemStatus( 
		// IF Module Supplied Status
		int *p_n2810MHzLock,
		int *p_n2700MHzLock,
		int *p_nSynthRef,
		int *p_nSynthLock,
		int *p_nRefLock,
		int *p_nExtRef,
		double *p_fSynthTemp,
		//
		// FPGA Module Supplied Status
		int *p_nAdcSaturation,
		int *p_nAdcPllLock,
		int *p_nTxCh1PllLock,
		int *p_nTxCh2PllLock,
		int *p_nTxCh3PllLock,
		int *p_nTxCh4PllLock,
		int *p_nWaveformRunning,
		double *p_fFpgaTemp,
		double *p_fPowerLevel );


// ----------------------------------------------------------------------------
// Calibration Functions -
GPCGDLL_API int	RunIfGainAutoCal( void );								// cause IF Auto Calibration procedure to be run.
GPCGDLL_API int GetIfGainAutoCal(												// retrieve results of last Auto Cal procedure. 
		double	*p_fIfGainCh1_dB, 
		double	*p_fIfGainCh2_dB, 
		double	*p_fIfGainCh3_dB, 
		double	*p_fIfGainCh4_dB );	
GPCGDLL_API int GetSysCal(															// retrieve system calibration values from Flash memory
	double  *p_fSysGain_dB, 
	double	*p_fRxGain_dB,
	double	*p_fIfGainCh1_dB, 
	double	*p_fIfGainCh2_dB, 
	double	*p_fIfGainCh3_dB, 
	double	*p_fIfGainCh4_dB,		
	int			*p_nSynthAttn_dB,		
	int			*p_nEBandPad_dB,
	int			*p_nKBandPad_dB,
	char		*sCalibrationText,
	double	*p_fFullScaleAdcInPower_dB,				//		Input Power Level into DSP Module corresponding to ADC Full-Scale Signal
	double	*p_fAutoCalRxIfAttn_dB,							
	double	*p_fAutoCalTxIfAttn_dB,
	double	*p_fMinRange_m,	
	double	*p_fTxIfGainOffsetCh1_dB,
	double	*p_fTxIfGainOffsetCh2_dB,
	double	*p_fTxIfGainOffsetCh3_dB,
	double	*p_fTxIfGainOffsetCh4_dB,
	int			*p_nNe,														// E-Band Synthesizer Multiplier
	int			*p_nNk,														// K-Band Synthesizer Multiplier
	double	*p_fMaxOperatingGain_dB						// max allowed operating gain (dB)
	);	


// ----------------------------------------------------------------------------
// Instrument Configuration Status - 
// Identification information is retrieved as NULL terminated ASCII strings. The information is stored in Flash memory. 
// The sPartNum (part number) and sSerNum (serial number) strings are length 17 (16 ASCII characters, plus a NULL terminator) 
// and the sRev (revision code) is length 5 (4 ASCII characters, plus a NULL terminator).
//
GPCGDLL_API int GetInstId( char *sPartNum, char *sSerNum, char *sRev );				// instrument top-level ID information
//
GPCGDLL_API int GetPloId( char *sPartNum, char *sSerNum, char *sRev );				// PLO module ID information	
GPCGDLL_API int GetIfId( char *sPartNum, char *sSerNum, char *sRev );					// IF module ID information
GPCGDLL_API int GetDspId( char *sPartNum, char *sSerNum, char *sRev );				// DSP module ID information
GPCGDLL_API int GetFreqSynthId( char *sPartNum, char *sSerNum, char *sRev );	// Frequency Synthesizer ID information
//
GPCGDLL_API int GetTxRxId( int nTRModIdx, char *sPartNum, char *sSerNum, char *sRev );	// Tx/Rx module ID information - 5 modules nTRModIdx=[0-4]
//
GPCGDLL_API int GetFpgaFwId( char *sPartNum, char *sRev );										// FPGA Firmware Configuration information
GPCGDLL_API int GetNbFwId( char *sPartNum, char *sRev );											// embedded Microcontroller Firmware Configuration information
GPCGDLL_API int GetDllId(char *sPartNum, char *sRev);													// DLL (this) Configuration information


// ----------------------------------------------------------------------------
// Debug Functions
GPCGDLL_API void InitDebugWindow( void );																// Open up debug window on which DLL and GUI debug statements can be printed.
GPCGDLL_API void DebugWindowPrint( char *sStr );												// Print a string to the debug window.

// ----------------------------------------------------------------------------
// Protected Calibration and Config Programming - 
//	This is used to program instrument-specific "factory-settings" into Flash memory and is passcode protected.
GPCGDLL_API int SetSysCalCfgInfo(												// program system calibration and configuration information in Flash memory
	void *pCalCfgInfo,																		//	pointer to calibration and configuration info structure
	char *sPasscode);



