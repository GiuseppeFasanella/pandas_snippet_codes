## Do not forget this parse_dates stuff otherwise plotting with matplotlib is forever
df_ = pd.read_csv(file_name, index_col='date', parse_dates=['date'])
