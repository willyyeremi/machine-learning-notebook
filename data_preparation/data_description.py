def data_description_1(data):
    '''data description and another information about data'''
    import numpy
    import pandas
    # data from top 20 rows
    print("\n20 top rows")
    print(data.head(20))
    # data type per column
    print("\ncolumn information")
    print(data.info())
    # statistic description of data
    print("\nstatistic description")
    desc_info=data.describe()
    IQR=pandas.DataFrame(data.select_dtypes(include='number').quantile(0.75)-data.select_dtypes(include='number').quantile(0.25),columns=['interquartile range']).transpose()
    mode=data.select_dtypes(include='number').mode().head(1).set_index(numpy.array(['mode']))
    desc_info=desc_info.append([IQR,mode])
    print(desc_info)

def data_description_2(data):
    '''further information about the data with graphic'''
    import pandas
    import matplotlib
    import seaborn
    # correlation value between numerical data
    print("\ndata correlation between each column")
    data_corr=data.select_dtypes(include='number').corr()
    matplotlib.pyplot.figure(figsize=(20,20))
    matplotlib.pyplot.imshow(data_corr,vmin=-1,vmax=1,cmap="rocket_r")
    matplotlib.pyplot.xticks(range(len(data_corr.columns)),data_corr.columns,fontdict={'fontsize':14},rotation=45)
    matplotlib.pyplot.yticks(range(len(data_corr.index)),data_corr.index,fontdict={'fontsize':14})
    matplotlib.pyplot.title(label="correlation between column",fontdict={'fontsize':30})
    for i in range(len(data_corr.index)):
        for j in range(len(data_corr.columns)):
            matplotlib.pyplot.text(x=j,y=i,s=round(data_corr.iloc[i,j],2),va='center',ha='center',color='w',fontsize=12)
    matplotlib.pyplot.colorbar(location='right',orientation='vertical').ax.tick_params(labelsize=20)
    matplotlib.pyplot.show()
    # skewness graphic
    