def load_data(data_path):
    '''load data from csv files'''
    import pandas
    data=pandas.read_csv(data_path)
    return data