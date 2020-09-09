features_v1 = pd.read_csv("data_pred_v1.csv",sep=";",decimal=",",encoding='latin-1')
features_v1['datetime'] = features_v1['datetime'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
features_v1 = features_v1.set_index('datetime')
