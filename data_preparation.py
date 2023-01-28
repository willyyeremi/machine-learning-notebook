def load_data(data_path):
    '''load data from csv files'''
    import pandas
    data=pandas.read_csv(r+str(data_path))
    return data