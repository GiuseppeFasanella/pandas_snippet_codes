## Do not forget this parse_dates stuff otherwise plotting with matplotlib is forever
df_ = pd.read_csv(file_name, index_col='date', parse_dates=['date'])

## Also, to be explicit, you can use this:
df = pd.read_csv("data.csv", sep=";")
df.loc[:, 'datetime'] = df.loc[:, 'datetime'].apply(lambda s: datetime.strptime(s, '%Y-%m-%d %H:%M:%S'))
df = df.set_index('datetime')
print(df)
