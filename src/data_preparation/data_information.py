def data_description(data):
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
    unique_value=data.agg(['count', 'size', 'nunique']).rename(index={'nunique':'unique (no null)'})
    have_null=[]
    for x in range(len(unique_value.columns)):
        if unique_value.iloc[0,x]==unique_value.iloc[1,x]:
            have_null.append(0+unique_value.iloc[2,x])
        else:
            have_null.append(1+unique_value.iloc[2,x])
    unique_value=unique_value.iloc[[2]].append(pandas.DataFrame(data=have_null,columns=['unique (with null)'],index=unique_value.columns.tolist()).transpose())
    desc_info=desc_info.append([IQR,mode,unique_value])
    print(desc_info)

def data_relation(data):
    '''further information about the feature and target with graphic'''
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
    
def measure_of_shape(data):
    '''information of continous feature skewness and kurtosis'''
    import matplotlib
    import seaborn