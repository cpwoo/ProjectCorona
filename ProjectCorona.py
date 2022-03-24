import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
df = pd.read_excel('코로나바이러스감염증-19_확진환자_발생현황_220324.xlsx', skiprows=[0,1,2,3,5])
df.drop(columns=['국내발생(명)', '해외유입(명)'], inplace=True)
df.rename(columns={'계(명)':'일일확진자', '사망(명)':'일일사망자'}, inplace=True)
df['일자'] = df['일자'].dt.strftime('%y.%m.%d')
df.replace('-', 0, inplace=True)
df['누적확진자'] = df['일일확진자'].cumsum()
df['누적사망자'] = df['일일사망자'].cumsum()
df['발생률'] = df['누적확진자'] / 51625561 * 100
df['치명률'] = df['누적사망자'] / df['누적확진자'] * 100
df30 = df.tail(30)

x = df['일자']; y=df['일일확진자']
plt.title('대한민국 코로나19 일일확진자')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df30['일자']; y=df30['일일확진자']
plt.title('대한민국 코로나19 일일확진자 최근 30일')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df['일자']; y=df['누적확진자']
plt.title('대한민국 코로나19 누적확진자')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df['일자']; y=df['발생률']
plt.title('대한민국 코로나19 발생률')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df30['일자']; y=df30['발생률']
plt.title('대한민국 코로나19 발생률 최근30일')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df['일자']; y=df['일일사망자']
plt.title('대한민국 코로나19 일일사망자')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df30['일자']; y=df30['일일사망자']
plt.title('대한민국 코로나19 일일사망자 최근 30일')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df['일자']; y=df['누적사망자']
plt.title('대한민국 코로나19 누적사망자')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df['일자']; y=df['치명률']
plt.title('대한민국 코로나19 치명률')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()

x = df30['일자']; y=df30['치명률']
plt.title('대한민국 코로나19 치명률 최근 30일')
plt.plot(x, y, color='k')
plt.xticks(range(0, len(x), len(x)//4))
plt.show()