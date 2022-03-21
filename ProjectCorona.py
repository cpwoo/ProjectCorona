import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
df = pd.read_excel('코로나바이러스감염증-19_확진환자_발생현황_220321.xlsx', skiprows=[0,1,2,3,5])
df.replace('-', 0, inplace=True)

df['누적확진'] = df['계(명)'].cumsum()
df['누적사망'] = df['사망(명)'].cumsum()
df['발생률'] = df['누적확진'] / 51625561 * 100
df['치명률'] = df['누적사망'] / df['누적확진'] * 100

df30 = df.tail(30)

x = df['일자']; y = df['계(명)']
plt.title('대한민국 코로나19 일일확진자')
plt.plot(x, y, color='k')
plt.xticks(['2020-03-01', '2021-03-01', '2022-03-01'])
plt.show()

x = df30['일자']; y = df30['계(명)']
plt.title('대한민국 코로나19 일일확진자 최근 30일')
plt.plot(x, y, color='k')
plt.xticks(['2022-02-21', '2022-03-07', '2022-03-21'])
plt.show()

x = df['일자']; y = df['누적확진']
plt.title('대한민국 코로나19 누적확진자')
plt.plot(x, y, color='k')
plt.xticks(['2020-03-01', '2021-03-01', '2022-03-01'])
plt.show()

x = df['일자']; y = df['발생률']
plt.title('대한민국 코로나19 발생률')
plt.plot(x, y, color='k')
plt.xticks(['2020-03-01', '2021-03-01', '2022-03-01'])
plt.show()

x = df30['일자']; y = df30['발생률']
plt.title('대한민국 코로나19 발생률 최근30일')
plt.plot(x, y, color='k')
plt.xticks(['2022-02-21', '2022-03-07', '2022-03-21'])
plt.show()

x = df['일자']; y = df['사망(명)']
plt.title('대한민국 코로나19 일일사망자')
plt.plot(x, y, color='k')
plt.xticks(['2020-03-01', '2021-03-01', '2022-03-01'])
plt.show()

x = df30['일자']; y = df30['사망(명)']
plt.title('대한민국 코로나19 일일사망자 최근 30일')
plt.plot(x, y, color='k')
plt.xticks(['2022-02-21', '2022-03-07', '2022-03-21'])
plt.show()

x = df['일자']; y = df['누적사망']
plt.title('대한민국 코로나19 누적사망자')
plt.plot(x, y, color='k')
plt.xticks(['2020-03-01', '2021-03-01', '2022-03-01'])
plt.show()

x = df['일자']; y = df['치명률']
plt.title('대한민국 코로나19 치명률')
plt.plot(x, y, color='k')
plt.xticks(['2020-03-01', '2021-03-01', '2022-03-01'])
plt.show()

x = df30['일자']; y = df30['치명률']
plt.title('대한민국 코로나19 치명률 최근 30일')
plt.plot(x, y, color='k')
plt.xticks(['2022-02-21', '2022-03-07', '2022-03-21'])
plt.show()