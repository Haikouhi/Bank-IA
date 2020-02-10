import pandas as pd
import seaborn as sns

df = pd.read_csv('Train_v2 (1).csv')
print(df)

#df[(df['bank_account'] == 'Yes') & (df['cellphone_access'] == 'Yes')]
test = sns.countplot(data=df, x='cellphone_access', hue='bank_account')

test = sns.countplot(data=df, x='bank_account', hue='location_type')

