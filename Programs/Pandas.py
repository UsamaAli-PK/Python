import pandas as pd

file_path = 'result.csv'

df = pd.read_csv(file_path)

uni= df['Name'].unique()

print(uni)
