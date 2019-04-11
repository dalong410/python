import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

sales = { '시간': [9, 10, 11, 12, 13, 14, 15],
        '제품1': [10, 15, 12, 11, 12, 14, 13],
        '제품2': [9, 11, 14, 12, 13, 10, 12]}

df = pd.DataFrame(sales, index = sales['시간'], columns = ['제품1', '제품2'])
df.index.name = '시간'  	

matplotlib.rcParams['font.family'] = 'Malgun Gothic'    
matplotlib.rcParams['axes.unicode_minus'] = False

product_plot = df.plot(grid = True, style = ['-*', 'o'], title='시간대별 생산량')
product_plot.set_ylabel("생산량")

# 파일 저장 위치를 지정해주세요(에러발생함)
image_file = 'D:/python/fig_for excel1.png' 	
plt.savefig(image_file, dpi = 400) 			
plt.show()
