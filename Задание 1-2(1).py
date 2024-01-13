from IPython.display import display
import pandas as pd
df = pd.read_csv('/content/Customers.csv', delimiter=';')
display(df.isna().sum())
print('\n', 'Есть пропуски', '\n')
df.dropna(axis=0, how='any', inplace=True)
display(df.groupby('Profession')['Income'].mean())