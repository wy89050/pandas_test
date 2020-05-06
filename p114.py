# Pandas Series 時間序列

import pandas as pd
import numpy as np



ts = pd.Series(np.random.randn(5),index= pd.date_range('20200101',periods=5)) #頻率為日
print(ts)
print('--------------------------')


ts = pd.Series(np.random.randn(5),index= pd.date_range('2020-01-01',periods=5, freq='M')) #頻率為月
print(ts)
print('--------------------------')



ts = pd.Series(np.random.randn(5),index= pd.date_range('2020/01/01',periods=5, freq='W')) #頻率為周
print(ts)
print('')