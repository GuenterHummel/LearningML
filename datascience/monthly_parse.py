from io import StringIO
import pandas as pd
csv_data = '''\
day,hits
2020-01-01,400
2020-02-02,800
2020-02-03,600
'''
df = pd.read_csv(StringIO(csv_data), parse_dates=['day'], dayfirst=True)
print(df['day'].dt.month.unique())