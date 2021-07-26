#股市行情数据获取和作图 -2
from  Ashare import *          #股票数据库    https://github.com/mpquant/Ashare
from  MyTT import *            #myTT麦语言工具函数指标库  https://github.com/mpquant/MyTT
from matplotlib.pylab import datestr2num

# 证券代码兼容多种格式 通达信，同花顺，聚宽
# sh000001 (000001.XSHG)    sz399006 (399006.XSHE)   sh600519 ( 600519.XSHG ) 

df=get_price('603185.XSHG',frequency='1d',count=44)      #默认获取今天往前120天的日线行情
print('上证指数日线行情\n',df.tail(5))

#-------有数据了，下面开始正题 -------------
CLOSE=df.close.values;         OPEN=df.open.values           #基础数据定义，只要传入的是序列都可以  Close=df.close.values 
HIGH=df.high.values;           LOW=df.low.values             #例如  CLOSE=list(df.close) 都是一样
TIME=df.day.values

MA5=MA(CLOSE,5)                                #获取5日均线序列
MA10=MA(CLOSE,10)                              #获取10日均线序列
up,mid,lower=BOLL(CLOSE)                       #获取布林带指标数据

#-------------------------作图显示-----------------------------------------------------------------
import matplotlib.pyplot as plt ;  from matplotlib.ticker import MultipleLocator
plt.figure(figsize=(8,4))
#plt.plot(CLOSE,label='SHZS');
#plt.plot(up,label='UP');           #画图显示
#plt.plot(mid,label='MID');
#plt.plot(LOW,label='LOW');
#plt.plot(MA10,label='MA10',linewidth=0.5,alpha=0.7);
#plt.axhline(200, c = "r", ls = "-")
#plt.axvline(30, c = "y", ls = "-")
plt.legend();
plt.grid(linewidth=0.5,alpha=0.7);
plt.gcf().autofmt_xdate(rotation=45);
x = range(len(TIME))
print(TIME)
y = datestr2num("2020-07-21")
print(y)
x_date = []
p_value = []
#x_date = [datestr2num(i) for i in TIME]
for i in TIME:
    #print("enter")
    x_date.append(datestr2num(str(i)))
    p_value.append(200)
print(x_date)
plt.plot_date(x_date,CLOSE,'-',label="收盘价")
#plt.plot_date(x_date,p_value,'-',label="记录价")
plt.axvline(x=18772, c = "y", ls = "-")
plt.axhline(y=300, c = "y", ls = "-")
#plt.gca().xaxis.set_major_locator(MultipleLocator(len(CLOSE)/10))    #日期最多显示30个
plt.title('SH-INDEX   &   BOLL SHOW',fontsize=20);
plt.savefig('./603185.jpg')
plt.show()
