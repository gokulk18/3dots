import pandas as pd

# Load data
deliveries = pd.read_csv('./archive/deliveries.csv')
matches = pd.read_csv('./archive/matches.csv')

# Preview
print("Deliveries:", deliveries.shape)
print("Matches:", matches.shape)

print(deliveries.isnull().sum())

deliveries.head()
