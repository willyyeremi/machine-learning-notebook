def load_data():
    '''load data from csv files'''
    import pandas
    import glob
    type_data=int(input("how many data files you use (answer with the number option)\n1:single file\n2:multi files\n"))
    if type_data not in [1,2]:
        print("choose between option 1 or 2")
        load_data()
    path=input("Write the data location. For example:\n"+"C:\\Users\\willy\\Documents\Database\\Kaggle\\Melbourne Housing Snapshot\\melb_data.csv\n")
    if type_data==1:
        data=pandas.read_csv(path)
        return data
    elif type_data==2:
        csv_files=glob.glob(path+"/*.csv")
        multidatalist=[pandas.read_csv(file) for file in csv_files]
        data=pandas.concat(multidatalist,ignore_index=True)
        return data