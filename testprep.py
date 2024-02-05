import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('dataset/data.csv')

# Dropping rows containing "ahegao"
df = df[~df['label'].str.contains('ahegao')]

train_df, test_val_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['label'])
test_df, val_df = train_test_split(test_val_df, test_size=0.5, random_state=42, stratify=test_val_df['label'])

# Saving the datasets to CSV files
train_df.to_csv('dataset/train.csv', index=False)
test_df.to_csv('dataset/test.csv', index=False)
val_df.to_csv('dataset/val.csv', index=False)

