    ## Scatter plots
    n_rows=2
    n_cols=5
    ## num_rows of n_cols plots each
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(30,15)) 
    i=0
    j=0
    for feat in most_correlated_feats:
        axs[i%n_rows, j%n_cols].scatter(df[feat], df['close'])
        axs[i%n_rows, j%n_cols].set_title(feat)
        j+=1
        if j%n_cols==0:
            i+=1
    plt.show() ## Force to show the plots
