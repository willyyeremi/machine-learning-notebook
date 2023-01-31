def load_data(type_data,path):
    '''load data from csv files'''
    import pandas
    import glob
    if type_data not in [1,2]:
        print("choose between option 1 or 2")
        load_data()
    if type_data==1:
        data=pandas.read_csv(path)
        return data
    elif type_data==2:
        csv_files=glob.glob(path+"/*.csv")
        multidatalist=[pandas.read_csv(file) for file in csv_files]
        data=pandas.concat(multidatalist,ignore_index=True)
        return data