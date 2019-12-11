plt.figure()
print(refresh_nn_data.columns)
df = refresh_nn_data.groupby(pd.Grouper(freq="1H")).apply(new_gain([0.5,0.5], 4))

fig, ax = plt.subplots(figsize=(14,8))
t = df.index
color = 'tab:red'
ax.set_xlabel('Date', fontsize='large', fontweight='bold')
ax.set_ylabel('Price', color=color, fontsize='large', fontweight='bold')
ax.plot(t, df['dayahead_price'], color=color)
for label in ax.get_xmajorticklabels():
    label.set_rotation(90)

fig.tight_layout()  # otherwise the right y-label is slightly clipped                                                                                                              
plt.show()
