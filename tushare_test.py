import tushare as ts

ts.set_token('b54c4caabdbf0e036fc04e0d89fe08011ffb7258b747bfde7ec393d0')
pro = ts.pro_api()
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date',is_open='0')
print(df)