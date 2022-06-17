import matplotlib.pyplot as plt
import warnings
import numpy as np
import pandas as pd
import yfinance as yf

from scipy import stats
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = [8, 4.5]
plt.rcParams['figure.dpi'] = 300
warnings.simplefilter(action='ignore', category=FutureWarning)

RISKY_ASSET = 'TSLA'
START_DATE = '2015-01-01'
END_DATE = '2022-01-01'
df = yf.download(RISKY_ASSET, start=START_DATE, end=END_DATE, adjusted=True)
print(f'Descargados {df.shape[0]} renglones de datos.')
print(df)

adj_close = df['Adj Close']
returns = adj_close.pct_change().dropna()   

ax = returns.plot()
ax.set_title(f'{RISKY_ASSET} rendimientos: {START_DATE} - {END_DATE}', 
             fontsize=16)

plt.tight_layout()
plt.show()

print(f'Rendimiento promedio: {100 * returns.mean():.2f}%')
